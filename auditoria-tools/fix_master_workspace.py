import sys
import os
import xml.etree.ElementTree as ET

sys.path.append(r'C:\Users\Admin\Documents\ChatGPT\New project\packet-tracer-skill\scripts')
from workspace_repair import sanitize_generated_physical_workspace, inspect_workspace_integrity
from pkt_codec import encode_xml_file

def fix_master():
    master_xml = 'pkt_xmls/terminal_portuario_master.xml'
    tree = ET.parse(master_xml)
    root = tree.getroot()
    
    # 1. Remover TODOS os nós de ponteiros de memória de tempo de execução de TODOS os links
    links = root.findall('.//LINKS/LINK')
    for l in links:
        cable = l.find('CABLE')
        if cable is not None:
            for tag in ['FROM_DEVICE_MEM_ADDR', 'TO_DEVICE_MEM_ADDR', 'FROM_PORT_MEM_ADDR', 'TO_PORT_MEM_ADDR']:
                for node in cable.findall(tag):
                    cable.remove(node)
                    
    # 2. Remover qualquer PHYSICAL_CPUR residual de todos os dispositivos
    for dev in root.findall('.//DEVICES/DEVICE'):
        ws = dev.find('WORKSPACE')
        if ws is not None:
            cpur = ws.find('PHYSICAL_CPUR')
            if cpur is not None:
                ws.remove(cpur)
                
    # 3. Executar sanitize_generated_physical_workspace
    sanitize_generated_physical_workspace(root)
    
    # 4. Validar integridade do workspace
    res = inspect_workspace_integrity(root)
    print("Resultado da inspeção do workspace:")
    print("  workspace_mode:", res.workspace_mode)
    print("  logical_status:", res.logical_status)
    print("  physical_status:", res.physical_status)
    print("  blocking_issues count:", len(res.blocking_issues))
    for iss in res.blocking_issues[:10]:
        print("   -", iss)
        
    # 5. Salvar e re-encodar se estiver ok
    if not res.blocking_issues:
        tree.write(master_xml, encoding='utf-8', xml_declaration=True)
        encode_xml_file(master_xml, 'Terminal-Portuario-Geral.pkt')
        print("Terminal-Portuario-Geral.pkt gerado e salvo com workspace 100% íntegro!")

if __name__ == '__main__':
    fix_master()
