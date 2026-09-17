import sys
import os
import uuid
import copy
import xml.etree.ElementTree as ET

sys.path.append(r'C:\Users\Admin\Documents\ChatGPT\New project\packet-tracer-skill\scripts')
from pkt_codec import encode_xml_file

def sync_physical_workspace():
    master_xml = 'pkt_xmls/terminal_portuario_master.xml'
    tree = ET.parse(master_xml)
    root = tree.getroot()
    
    prefix = "{251f5ba0-2db6-4fde-80b9-ee56a89f298f},{6849e979-1ba7-4ac4-8988-8bf6922d44a2},{2bc7a571-40bb-429c-80e6-3eb7b0593ea3},{cc8f961a-b57e-487a-8bfa-0d4aa9b79aef},{eeff34e2-8b1a-49f4-bd0f-6459e2db0bd2}"
    
    # 1. Encontrar o nó pai {eeff34e2-8b1a-49f4-bd0f-6459e2db0bd2}
    parent_node = None
    pw = root.find('.//PHYSICALWORKSPACE')
    for n in pw.iter('NODE'):
        u = n.findtext('UUID_STR', '')
        if u == '{eeff34e2-8b1a-49f4-bd0f-6459e2db0bd2}':
            parent_node = n
            break
            
    if parent_node is None:
        print("ERRO: Nó pai do closet físico não encontrado!")
        return
        
    children_elem = parent_node.find('CHILDREN')
    if children_elem is None:
        children_elem = ET.SubElement(parent_node, 'CHILDREN')
        
    # Encontrar um template de folha existente
    leaf_template = None
    for child in children_elem.findall('NODE'):
        if child.findtext('TYPE', '') == '6':
            leaf_template = child
            break
            
    if leaf_template is None:
        print("ERRO: Template de folha não encontrado!")
        return
        
    # Dispositivos já existentes na árvore física
    existing_phys_names = {}
    for child in children_elem.findall('NODE'):
        d_name = child.findtext('NAME', '')
        u_str = child.findtext('UUID_STR', '')
        if d_name and u_str:
            existing_phys_names[d_name] = u_str
            
    print(f"Dispositivos já presentes na árvore física: {len(existing_phys_names)}")
    
    # 2. Percorrer todos os 101 dispositivos em NETWORK/DEVICES
    devices = root.findall('.//DEVICES/DEVICE')
    added_count = 0
    
    for dev in devices:
        name = dev.findtext('./ENGINE/NAME', default='').strip()
        ws = dev.find('WORKSPACE')
        if ws is None:
            ws = ET.SubElement(dev, 'WORKSPACE')
            
        # Remover nós PHYSICAL_CPUR
        for cpur in ws.findall('PHYSICAL_CPUR'):
            ws.remove(cpur)
            
        phys_node = ws.find('PHYSICAL')
        if phys_node is None:
            phys_node = ET.SubElement(ws, 'PHYSICAL')
            
        if name in existing_phys_names:
            dev_uuid = existing_phys_names[name]
        else:
            # Criar novo nó físico
            dev_uuid = f"{{{str(uuid.uuid4())}}}"
            new_node = copy.deepcopy(leaf_template)
            
            # Atualizar propriedades do novo nó
            n_name = new_node.find('NAME')
            if n_name is not None:
                n_name.text = name
            n_uuid = new_node.find('UUID_STR')
            if n_uuid is not None:
                n_uuid.text = dev_uuid
                
            children_elem.append(new_node)
            existing_phys_names[name] = dev_uuid
            added_count += 1
            
        # Atualizar a tag PHYSICAL do dispositivo com o caminho exato
        phys_node.text = f"{prefix},{dev_uuid}"
        
    print(f"Novos nós físicos adicionados à árvore: {added_count}")
    print(f"Total de dispositivos sincronizados: {len(devices)} dispositivos")
    
    # Salvar e codificar .pkt
    tree.write(master_xml, encoding='utf-8', xml_declaration=True)
    master_pkt = 'Terminal-Portuario-Geral.pkt'
    encode_xml_file(master_xml, master_pkt)
    print(f"Master {master_pkt} regerado e sincronizado com o Physical Workspace!")

if __name__ == '__main__':
    sync_physical_workspace()
