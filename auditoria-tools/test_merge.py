import sys
import os
import copy
import xml.etree.ElementTree as ET

sys.path.append(r'C:\Users\Admin\Documents\ChatGPT\New project\packet-tracer-skill\scripts')
from pkt_codec import decode_pkt_file, encode_xml_file
from pkt_verify import structural_check

def test_merge():
    # Base: predio_adm_migrated.xml
    tree_adm = ET.parse('pkt_xmls/predio_adm_migrated.xml')
    root_adm = tree_adm.getroot()
    net_adm = root_adm.find('NETWORK')
    devices_adm = net_adm.find('DEVICES')
    links_adm = net_adm.find('LINKS')
    
    print(f"Base ADM: {len(devices_adm)} devices, {len(links_adm)} links")
    
    # Vamos inspecionar os nomes de devices do ADM
    adm_names = {d.findtext('./ENGINE/NAME', default='').strip() for d in devices_adm}
    print(f"Amostra de nomes no ADM: {list(adm_names)[:5]}")

if __name__ == '__main__':
    test_merge()
