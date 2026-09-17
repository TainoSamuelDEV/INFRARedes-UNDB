import sys
import os
import copy
import uuid
from pathlib import Path
import xml.etree.ElementTree as ET

sys.path.append(r'C:\Users\Admin\Documents\ChatGPT\New project\packet-tracer-skill\scripts')
from pkt_codec import decode_pkt_auto, encode_xml_file
from workspace_repair import inspect_workspace_integrity
from pkt_verify import structural_check

def update_with_adm_alterado():
    print("=== Passo 1: Processando Predio-Administrativo-TP-ALTERADO.pkt ===")
    p_alt = Path(r'Predio-Administrativo(Gabriel Ordonez e Higor Gabriel)\03-Packet-Tracer\Predio-Administrativo-TP-ALTERADO.pkt')
    p_target = Path(r'Predio-Administrativo(Gabriel Ordonez e Higor Gabriel)\03-Packet-Tracer\Predio-Administrativo-TP.pkt')
    
    xml_alt, _ = decode_pkt_auto(p_alt.read_bytes())
    adm_root = ET.fromstring(xml_alt)
    
    # Injetar rota 10.100.0.0/16 no RTR-CAMPUS
    rtr = None
    for d in adm_root.findall('.//DEVICES/DEVICE'):
        if d.findtext('./ENGINE/NAME') == 'RTR-CAMPUS':
            rtr = d
            break
            
    if rtr is not None:
        for tag in ['RUNNINGCONFIG', 'STARTUPCONFIG']:
            cfg = rtr.find(f'.//{tag}')
            if cfg is not None:
                has_route = any('10.100.0.0' in (l.text or '') for l in cfg.findall('LINE'))
                if not has_route:
                    # Encontrar a linha de 10.20.0.0
                    children = list(cfg)
                    inserted = False
                    for idx, child in enumerate(children):
                        if child.tag == 'LINE' and 'ip route 10.20.0.0' in (child.text or ''):
                            new_line = ET.Element('LINE')
                            new_line.text = 'ip route 10.100.0.0 255.255.0.0 10.255.20.2'
                            cfg.insert(idx + 1, new_line)
                            inserted = True
                            break
                    if not inserted:
                        new_line = ET.Element('LINE')
                        new_line.text = 'ip route 10.100.0.0 255.255.0.0 10.255.20.2'
                        cfg.append(new_line)
        print("Rota do campus 10.100.0.0/16 garantida em RTR-CAMPUS.")
    
    # Salvar predio_adm_migrated.xml e atualizar Predio-Administrativo-TP.pkt
    adm_tree = ET.ElementTree(adm_root)
    adm_xml_path = 'pkt_xmls/predio_adm_migrated.xml'
    adm_tree.write(adm_xml_path, encoding='utf-8', xml_declaration=True)
    encode_xml_file(adm_xml_path, str(p_target))
    print(f"Predio-Administrativo-TP.pkt atualizado ({len(adm_root.findall('.//DEVICES/DEVICE'))} dispositivos).")
    
    print("\n=== Passo 2: Mesclando todos os setores no Master ===")
    adm_net = adm_root.find('NETWORK')
    adm_devices = adm_net.find('DEVICES')
    adm_links = adm_net.find('LINKS')
    
    existing_names = set()
    for d in adm_devices:
        name = d.findtext('./ENGINE/NAME', default='').strip()
        if name:
            existing_names.add(name)
            
    sectors_config = [
        {
            'name': 'PORTARIA',
            'xml': 'pkt_xmls/portaria_migrated.xml',
            'offset_x': -650,
            'offset_y': 250,
            'prefix': 'PT-',
            'skip_devices': ['GW-CENTRAL', 'SW-CENTRAL', 'SRV-CENTRAL', 'RAMAL-TESTE']
        },
        {
            'name': 'INSPETORIA',
            'xml': 'pkt_xmls/inspetoria_migrated.xml',
            'offset_x': 900,
            'offset_y': 350,
            'prefix': 'INSP-',
            'skip_devices': []
        },
        {
            'name': 'PERA',
            'xml': 'pkt_xmls/pera_migrated.xml',
            'offset_x': -350,
            'offset_y': 750,
            'prefix': 'PERA-',
            'skip_devices': ['ROTEADOR CCO', 'Multilayer Switch2']
        },
        {
            'name': 'SILO',
            'xml': 'pkt_xmls/silo_migrated.xml',
            'offset_x': 850,
            'offset_y': -150,
            'prefix': 'SILO-',
            'skip_devices': ['Rede Portuaria']
        }
    ]
    
    ref_counter = 1000000000000000000
    
    for sec in sectors_config:
        sec_tree = ET.parse(sec['xml'])
        sec_root = sec_tree.getroot()
        sec_net = sec_root.find('NETWORK')
        if sec_net is None:
            continue
        sec_devices = sec_net.find('DEVICES')
        sec_links = sec_net.find('LINKS')
        
        ref_map = {}
        
        for dev in list(sec_devices):
            orig_name = dev.findtext('./ENGINE/NAME', default='').strip()
            if orig_name in sec['skip_devices']:
                continue
                
            new_name = orig_name
            if new_name in existing_names or 'Power Distribution' in new_name or new_name in ['Switch', 'Access Point']:
                new_name = f"{sec['prefix']}{orig_name}"
            existing_names.add(new_name)
            
            name_node = dev.find('./ENGINE/NAME')
            if name_node is not None:
                name_node.text = new_name
                
            ref_node = dev.find('.//SAVE_REF_ID')
            if ref_node is not None and ref_node.text:
                orig_ref = ref_node.text.strip()
                ref_counter += 1
                new_ref = f"save-ref-id:{ref_counter}"
                ref_map[orig_ref] = new_ref
                ref_node.text = new_ref
                
            x_node = dev.find('./WORKSPACE/LOGICAL/X')
            y_node = dev.find('./WORKSPACE/LOGICAL/Y')
            if x_node is not None and x_node.text:
                try:
                    val_x = float(x_node.text) + sec['offset_x']
                    x_node.text = str(val_x)
                except:
                    pass
            if y_node is not None and y_node.text:
                try:
                    val_y = float(y_node.text) + sec['offset_y']
                    y_node.text = str(val_y)
                except:
                    pass
                    
            adm_devices.append(copy.deepcopy(dev))
            
        if sec_links is not None:
            for link in list(sec_links):
                cable = link.find('CABLE')
                if cable is None:
                    continue
                from_node = cable.find('FROM')
                to_node = cable.find('TO')
                if from_node is None or to_node is None:
                    continue
                orig_from = from_node.text.strip() if from_node.text else ''
                orig_to = to_node.text.strip() if to_node.text else ''
                
                if orig_from in ref_map and orig_to in ref_map:
                    from_node.text = ref_map[orig_from]
                    to_node.text = ref_map[orig_to]
                    for mem_tag in ['FROM_DEVICE_MEM_ADDR', 'TO_DEVICE_MEM_ADDR', 'FROM_PORT_MEM_ADDR', 'TO_PORT_MEM_ADDR']:
                        node = cable.find(mem_tag)
                        if node is not None:
                            cable.remove(node)
                    adm_links.append(copy.deepcopy(link))

    print(f"Total de dispositivos combinados: {len(adm_devices)}")
    print(f"Total de enlaces combinados: {len(adm_links)}")
    
    print("\n=== Passo 3: Sincronizando Physical Workspace ===")
    prefix = "{251f5ba0-2db6-4fde-80b9-ee56a89f298f},{6849e979-1ba7-4ac4-8988-8bf6922d44a2},{2bc7a571-40bb-429c-80e6-3eb7b0593ea3},{cc8f961a-b57e-487a-8bfa-0d4aa9b79aef},{eeff34e2-8b1a-49f4-bd0f-6459e2db0bd2}"
    
    parent_node = None
    pw = adm_root.find('.//PHYSICALWORKSPACE')
    for n in pw.iter('NODE'):
        u = n.findtext('UUID_STR', '')
        if u == '{eeff34e2-8b1a-49f4-bd0f-6459e2db0bd2}':
            parent_node = n
            break
            
    if parent_node is None:
        raise RuntimeError("Nó pai do closet/rack não encontrado!")
        
    children_elem = parent_node.find('CHILDREN')
    if children_elem is None:
        children_elem = ET.SubElement(parent_node, 'CHILDREN')
        
    leaf_template = None
    for child in children_elem.findall('NODE'):
        if child.findtext('TYPE', '') == '6':
            leaf_template = child
            break
            
    existing_phys_names = {}
    for child in children_elem.findall('NODE'):
        d_name = child.findtext('NAME', '')
        u_str = child.findtext('UUID_STR', '')
        if d_name and u_str:
            existing_phys_names[d_name] = u_str
            
    added_nodes = 0
    all_devices = adm_root.findall('.//DEVICES/DEVICE')
    for dev in all_devices:
        name = dev.findtext('./ENGINE/NAME', default='').strip()
        ws = dev.find('WORKSPACE')
        if ws is None:
            ws = ET.SubElement(dev, 'WORKSPACE')
            
        for cpur in ws.findall('PHYSICAL_CPUR'):
            ws.remove(cpur)
            
        phys_node = ws.find('PHYSICAL')
        if phys_node is None:
            phys_node = ET.SubElement(ws, 'PHYSICAL')
            
        if name in existing_phys_names:
            dev_uuid = existing_phys_names[name]
        else:
            dev_uuid = f"{{{str(uuid.uuid4())}}}"
            new_node = copy.deepcopy(leaf_template)
            n_name = new_node.find('NAME')
            if n_name is not None:
                n_name.text = name
            n_uuid = new_node.find('UUID_STR')
            if n_uuid is not None:
                n_uuid.text = dev_uuid
            children_elem.append(new_node)
            existing_phys_names[name] = dev_uuid
            added_nodes += 1
            
        phys_node.text = f"{prefix},{dev_uuid}"
        
    print(f"Nós físicos adicionados: {added_nodes}. Total físico: {len(existing_phys_names)} nós.")
    
    print("\n=== Passo 4: Sincronizando MEM_ADDR dos Enlaces ===")
    device_map = {}
    for dev in all_devices:
        ref = dev.findtext('.//SAVE_REF_ID', default='').strip()
        mem = dev.findtext('./WORKSPACE/LOGICAL/MEM_ADDR', default='').strip()
        if not mem:
            ws_log = dev.find('./WORKSPACE/LOGICAL')
            if ws_log is not None:
                mem_node = ws_log.find('MEM_ADDR')
                if mem_node is None:
                    mem_node = ET.SubElement(ws_log, 'MEM_ADDR')
                mem = str(abs(hash(ref)) % 9000000000000 + 1000000000000)
                mem_node.text = mem
        if ref and mem:
            device_map[ref] = mem
            
    for l in adm_root.findall('.//LINKS/LINK'):
        cable = l.find('CABLE')
        if cable is not None:
            from_ref = cable.findtext('FROM', default='').strip()
            to_ref = cable.findtext('TO', default='').strip()
            from_mem = device_map.get(from_ref, "")
            to_mem = device_map.get(to_ref, "")
            
            for tag in ['FROM_DEVICE_MEM_ADDR', 'TO_DEVICE_MEM_ADDR', 'FROM_PORT_MEM_ADDR', 'TO_PORT_MEM_ADDR']:
                for node in cable.findall(tag):
                    cable.remove(node)
                    
            if from_mem and to_mem:
                f_node = ET.SubElement(cable, 'FROM_DEVICE_MEM_ADDR')
                f_node.text = from_mem
                t_node = ET.SubElement(cable, 'TO_DEVICE_MEM_ADDR')
                t_node.text = to_mem

    # Salvar XML Master
    master_xml = 'pkt_xmls/terminal_portuario_master.xml'
    adm_tree.write(master_xml, encoding='utf-8', xml_declaration=True)
    
    # Encode Terminal-Portuario-Geral.pkt
    master_pkt = 'Terminal-Portuario-Geral.pkt'
    encode_xml_file(master_xml, master_pkt)
    print(f"\nTerminal-Portuario-Geral.pkt gerado com sucesso: {master_pkt}")
    
    # Validação de integridade do workspace
    res = inspect_workspace_integrity(adm_root)
    print(f"\nResultado da Validação de Integridade:")
    print(f"  workspace_mode: {res.workspace_mode}")
    print(f"  logical_status: {res.logical_status}")
    print(f"  physical_status: {res.physical_status}")
    print(f"  blocking_issues: {len(res.blocking_issues)}")
    for iss in res.blocking_issues:
        print(f"    - {iss}")

if __name__ == '__main__':
    update_with_adm_alterado()
