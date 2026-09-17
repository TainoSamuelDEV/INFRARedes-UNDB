import sys
import os
import re
import xml.etree.ElementTree as ET

sys.path.append(r'C:\Users\Admin\Documents\ChatGPT\New project\packet-tracer-skill\scripts')
from pkt_codec import encode_xml_file
from pkt_verify import structural_check

def migrate_silo():
    xml_path = 'pkt_xmls/silo.xml'
    out_xml = 'pkt_xmls/silo_migrated.xml'
    target_pkt = r'Silo-Grãos(Asafe e Lucas)\Estrutura_Silo_de_Graos.pkt'
    
    with open(xml_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 1. Substituir o gateway linksys padrão 192.168.0.1 por 10.100.24.1
    replacements = [
        ('<LAN_IP_ADDRESS>192.168.0.1</LAN_IP_ADDRESS>', '<LAN_IP_ADDRESS>10.100.24.1</LAN_IP_ADDRESS>'),
        ('<NETWORK>192.168.0.0</NETWORK>', '<NETWORK>10.100.24.0</NETWORK>'),
        ('<START_IP>192.168.0.100</START_IP>', '<START_IP>10.100.24.100</START_IP>'),
        ('<END_IP>192.168.0.149</END_IP>', '<END_IP>10.100.24.149</END_IP>'),
        ('<DHCP_SERVER_IP>192.168.0.1</DHCP_SERVER_IP>', '<DHCP_SERVER_IP>10.100.24.1</DHCP_SERVER_IP>'),
        ('<GATEWAY>192.168.0.1</GATEWAY>', '<GATEWAY>10.100.24.1</GATEWAY>'),
        ('<IP_ADDRESS>192.168.0.100</IP_ADDRESS>', '<IP_ADDRESS>10.100.24.100</IP_ADDRESS>'),
        ('<IP_ADDRESS>192.168.0.102</IP_ADDRESS>', '<IP_ADDRESS>10.100.24.102</IP_ADDRESS>'),
        
        # Eliminar IPs de APIPA 169.254.x.x que estavam soltos
        ('169.254.84.147', '10.100.24.111'),
        ('169.254.55.150', '10.100.24.112'),
        ('169.254.51.221', '10.100.24.113'),
        ('169.254.215.171', '10.100.24.114'),
        ('169.254.139.120', '10.100.24.115'),
        
        # Ajustar hostname do switch
        ('<LINE>hostname Switch</LINE>', '<LINE>hostname SW-SILO-01</LINE>'),
    ]
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(out_xml, 'w', encoding='utf-8') as f:
        f.write(content)
        
    encode_xml_file(out_xml, target_pkt)
    print(f"Silo de Grãos migrado com sucesso para: {target_pkt}")
    
    report = structural_check(target_pkt)
    print("Verificação estrutural:", report.device_count, "dispositivos,", report.link_count, "enlaces.")

if __name__ == '__main__':
    migrate_silo()
