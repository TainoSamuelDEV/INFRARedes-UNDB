import sys
import os
import xml.etree.ElementTree as ET

sys.path.append(r'C:\Users\Admin\Documents\ChatGPT\New project\packet-tracer-skill\scripts')
from pkt_codec import decode_pkt_file, encode_xml_file
from lab_coherence import check_lab_coherence
from pkt_editor import decode_pkt_to_root

def finalize_master():
    master_xml = 'pkt_xmls/terminal_portuario_master.xml'
    tree = ET.parse(master_xml)
    root = tree.getroot()
    
    # Encontrar o GW-ADM-01
    gw_adm = None
    for dev in root.findall('.//DEVICE'):
        if dev.findtext('./ENGINE/NAME', default='').strip() == 'GW-ADM-01':
            gw_adm = dev
            break
            
    if gw_adm is not None:
        rc = gw_adm.find('.//RUNNINGCONFIG')
        if rc is not None:
            # Novas subinterfaces para responder pelos gateways de todos os setores integrados
            new_lines = [
                "!",
                "interface GigabitEthernet0/0.210",
                " description GATEWAY-PERA-FERROVIARIA",
                " encapsulation dot1Q 210",
                " ip address 10.100.16.1 255.255.255.0",
                "!",
                "interface GigabitEthernet0/0.310",
                " description GATEWAY-SILO-GRAOS",
                " encapsulation dot1Q 310",
                " ip address 10.100.24.1 255.255.255.0",
                "!",
                "interface GigabitEthernet0/0.410",
                " description GATEWAY-PORTARIA-TP",
                " encapsulation dot1Q 410",
                " ip address 10.100.28.1 255.255.255.240",
                "!",
                "interface GigabitEthernet0/0.510",
                " description GATEWAY-INSPETORIA-CCO",
                " encapsulation dot1Q 510",
                " ip address 10.100.32.1 255.255.255.0",
                "!"
            ]
            for nl in new_lines:
                elem = ET.SubElement(rc, 'LINE')
                elem.text = nl
                
    # Salvar XML atualizado
    tree.write(master_xml, encoding='utf-8', xml_declaration=True)
    
    # Re-encodar para .pkt
    master_pkt = 'Terminal-Portuario-Geral.pkt'
    encode_xml_file(master_xml, master_pkt)
    print(f"Master {master_pkt} atualizado com subinterfaces de campus!")
    
    # Testar coerência
    root_check = decode_pkt_to_root(master_pkt)
    findings = check_lab_coherence(root_check)
    print(f"Total de achados de coerência restantes: {len(findings)}")
    for f in findings:
        print("  -", f)

if __name__ == '__main__':
    finalize_master()
