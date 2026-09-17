import sys
import os
import copy
import xml.etree.ElementTree as ET

sys.path.append(r'C:\Users\Admin\Documents\ChatGPT\New project\packet-tracer-skill\scripts')
from pkt_codec import encode_xml_file
from pkt_verify import structural_check

def merge_all_sectors():
    print("Iniciando construção robusta do Laboratório Centralizado: Terminal-Portuario-Geral.pkt...")
    
    # Base: Prédio Administrativo
    adm_tree = ET.parse('pkt_xmls/predio_adm_migrated.xml')
    adm_root = adm_tree.getroot()
    adm_net = adm_root.find('NETWORK')
    adm_devices = adm_net.find('DEVICES')
    adm_links = adm_net.find('LINKS')
    
    existing_names = set()
    for d in adm_devices:
        name = d.findtext('./ENGINE/NAME', default='').strip()
        if name:
            existing_names.add(name)
            
    # Configuração dos setores
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
        
        # 1. Processar dispositivos
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
                
            # Mapear SAVE_REF_ID recursivamente
            ref_node = dev.find('.//SAVE_REF_ID')
            if ref_node is not None and ref_node.text:
                orig_ref = ref_node.text.strip()
                ref_counter += 1
                new_ref = f"save-ref-id:{ref_counter}"
                ref_map[orig_ref] = new_ref
                ref_node.text = new_ref
                
            # Ajustar coordenadas lógicas
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
            
        # 2. Processar links internos do setor
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

    print(f"Total consolidado no Master: {len(adm_devices)} dispositivos, {len(adm_links)} enlaces.")
    
    out_xml = 'pkt_xmls/terminal_portuario_master.xml'
    adm_tree.write(out_xml, encoding='utf-8', xml_declaration=True)
    
    master_pkt = 'Terminal-Portuario-Geral.pkt'
    encode_xml_file(out_xml, master_pkt)
    print(f"Laboratório Mestre gerado com sucesso: {master_pkt}")
    
    report = structural_check(master_pkt)
    print(f"Relatório de Validação Estrutural:")
    print(f"  Dispositivos: {report.device_count}")
    print(f"  Enlaces: {report.link_count}")
    print(f"  Container: {report.container}")
    print(f"  Versão: {report.version}")

if __name__ == '__main__':
    merge_all_sectors()
