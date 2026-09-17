import sys
import os
import re
import xml.etree.ElementTree as ET

sys.path.append(r'C:\Users\Admin\Documents\ChatGPT\New project\packet-tracer-skill\scripts')
from pkt_codec import encode_xml_file
from pkt_verify import structural_check

def migrate_pera():
    xml_path = 'pkt_xmls/pera.xml'
    out_xml = 'pkt_xmls/pera_migrated.xml'
    target_pkt = r'Pera-Ferroviaria(João Lucas e Jaylon Coelho)\Pera Ferroviária.pkt'
    
    with open(xml_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 1. Substituir o gateway linksys padrão 192.168.0.1 por 10.100.16.1
    replacements = [
        ('<LAN_IP_ADDRESS>192.168.0.1</LAN_IP_ADDRESS>', '<LAN_IP_ADDRESS>10.100.16.1</LAN_IP_ADDRESS>'),
        ('<NETWORK>192.168.0.0</NETWORK>', '<NETWORK>10.100.16.0</NETWORK>'),
        ('<START_IP>192.168.0.100</START_IP>', '<START_IP>10.100.16.100</START_IP>'),
        ('<END_IP>192.168.0.149</END_IP>', '<END_IP>10.100.16.149</END_IP>'),
        
        # Eliminar IPs de APIPA das 10 câmeras da Pera
        ('169.254.236.33', '10.100.16.111'),
        ('169.254.225.206', '10.100.16.112'),
        ('169.254.11.53', '10.100.16.113'),
        ('169.254.10.131', '10.100.16.114'),
        ('169.254.231.102', '10.100.16.115'),
        ('169.254.216.217', '10.100.16.116'),
        ('169.254.218.203', '10.100.16.117'),
        ('169.254.80.8', '10.100.16.118'),
        ('169.254.112.14', '10.100.16.119'),
        ('169.254.131.109', '10.100.16.120'),
    ]
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(out_xml, 'w', encoding='utf-8') as f:
        f.write(content)
        
    encode_xml_file(out_xml, target_pkt)
    print(f"Pera Ferroviária migrada com sucesso para: {target_pkt}")
    
    report = structural_check(target_pkt)
    print("Verificação estrutural:", report.device_count, "dispositivos,", report.link_count, "enlaces.")

if __name__ == '__main__':
    migrate_pera()
