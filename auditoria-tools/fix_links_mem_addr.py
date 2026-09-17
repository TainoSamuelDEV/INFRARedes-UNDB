import sys
import os
import xml.etree.ElementTree as ET

sys.path.append(r'C:\Users\Admin\Documents\ChatGPT\New project\packet-tracer-skill\scripts')
from workspace_repair import sanitize_generated_physical_workspace, inspect_workspace_integrity
from pkt_codec import encode_xml_file

def fix_links_mem_addr():
    master_xml = 'pkt_xmls/terminal_portuario_master.xml'
    tree = ET.parse(master_xml)
    root = tree.getroot()
    
    # 1. Mapear cada save_ref_id para o MEM_ADDR do seu dispositivo
    device_map = {}
    for dev in root.findall('.//DEVICES/DEVICE'):
        ref = dev.findtext('.//SAVE_REF_ID', default='').strip()
        mem = dev.findtext('./WORKSPACE/LOGICAL/MEM_ADDR', default='').strip()
        if not mem:
            # Se não tiver MEM_ADDR, criar um número hexadecimal/inteiro estável
            mem_node = dev.find('./WORKSPACE/LOGICAL/MEM_ADDR')
            if mem_node is None:
                ws_log = dev.find('./WORKSPACE/LOGICAL')
                if ws_log is not None:
                    mem_node = ET.SubElement(ws_log, 'MEM_ADDR')
            if mem_node is not None:
                mem = str(abs(hash(ref)) % 9000000000000 + 1000000000000)
                mem_node.text = mem
        if ref and mem:
            device_map[ref] = mem
            
    print(f"Dispositivos mapeados com MEM_ADDR: {len(device_map)}")
    
    # 2. Atribuir os MEM_ADDR correspondentes em cada link
    links = root.findall('.//LINKS/LINK')
    for l in links:
        cable = l.find('CABLE')
        if cable is not None:
            from_ref = cable.findtext('FROM', default='').strip()
            to_ref = cable.findtext('TO', default='').strip()
            
            from_mem = device_map.get(from_ref, "")
            to_mem = device_map.get(to_ref, "")
            
            # Limpar nós existentes
            for tag in ['FROM_DEVICE_MEM_ADDR', 'TO_DEVICE_MEM_ADDR', 'FROM_PORT_MEM_ADDR', 'TO_PORT_MEM_ADDR']:
                for node in cable.findall(tag):
                    cable.remove(node)
                    
            if from_mem and to_mem:
                f_node = ET.SubElement(cable, 'FROM_DEVICE_MEM_ADDR')
                f_node.text = from_mem
                t_node = ET.SubElement(cable, 'TO_DEVICE_MEM_ADDR')
                t_node.text = to_mem
                
    # 3. Executar sanitize_generated_physical_workspace
    sanitize_generated_physical_workspace(root)
    
    # 4. Validar integridade do workspace
    res = inspect_workspace_integrity(root)
    print("Resultado da inspeção do workspace com MEM_ADDR corrigidos:")
    print("  workspace_mode:", res.workspace_mode)
    print("  logical_status:", res.logical_status)
    print("  physical_status:", res.physical_status)
    print("  blocking_issues count:", len(res.blocking_issues))
    for iss in res.blocking_issues:
        print("   -", iss)
        
    # Salvar XML e encode .pkt
    tree.write(master_xml, encoding='utf-8', xml_declaration=True)
    encode_xml_file(master_xml, 'Terminal-Portuario-Geral.pkt')
    print("Terminal-Portuario-Geral.pkt gerado e salvo com sucesso!")

if __name__ == '__main__':
    fix_links_mem_addr()
