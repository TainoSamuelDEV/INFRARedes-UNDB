import sys
import os
import re
import xml.etree.ElementTree as ET

sys.path.append(r'C:\Users\Admin\Documents\ChatGPT\New project\packet-tracer-skill\scripts')
from pkt_codec import encode_xml_file
from pkt_verify import structural_check

def migrate_inspetoria():
    xml_path = 'pkt_xmls/inspetoria.xml'
    out_xml = 'pkt_xmls/inspetoria_migrated.xml'
    target_pkt = r'Predio-Inspetoria(Mateus Dantas e Renan Pires)\Predio-Inspetoria-Berco-098-mapa-estrela.pkt'
    
    with open(xml_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    replacements = [
        # Excluded addresses
        ('ip dhcp excluded-address 192.168.10.1 192.168.10.20', 'ip dhcp excluded-address 10.100.32.1 10.100.32.20'),
        ('ip dhcp excluded-address 192.168.20.1 192.168.20.20', 'ip dhcp excluded-address 10.100.34.1 10.100.34.20'),
        ('ip dhcp excluded-address 192.168.30.1 192.168.30.20', 'ip dhcp excluded-address 10.100.36.1 10.100.36.20'),
        ('ip dhcp excluded-address 192.168.40.1 192.168.40.20', 'ip dhcp excluded-address 10.100.33.1 10.100.33.20'),
        
        # Networks e Default Routers
        ('network 192.168.10.0 255.255.255.0', 'network 10.100.32.0 255.255.255.0'),
        ('default-router 192.168.10.1', 'default-router 10.100.32.1'),
        ('network 192.168.20.0 255.255.255.0', 'network 10.100.34.0 255.255.255.0'),
        ('default-router 192.168.20.1', 'default-router 10.100.34.1'),
        ('network 192.168.30.0 255.255.255.0', 'network 10.100.36.0 255.255.255.0'),
        ('default-router 192.168.30.1', 'default-router 10.100.36.1'),
        ('network 192.168.40.0 255.255.255.0', 'network 10.100.33.0 255.255.255.0'),
        ('default-router 192.168.40.1', 'default-router 10.100.33.1'),
        
        # IP addresses nas subinterfaces
        ('ip address 192.168.10.1 255.255.255.0', 'ip address 10.100.32.1 255.255.255.0'),
        ('ip address 192.168.20.1 255.255.255.0', 'ip address 10.100.34.1 255.255.255.0'),
        ('ip address 192.168.30.1 255.255.255.0', 'ip address 10.100.36.1 255.255.255.0'),
        ('ip address 192.168.40.1 255.255.255.0', 'ip address 10.100.33.1 255.255.255.0'),
        ('ip address 192.168.99.1 255.255.255.0', 'ip address 10.100.39.241 255.255.255.240'),
        
        # Switch SW-01
        ('ip address 192.168.99.2 255.255.255.0', 'ip address 10.100.39.242 255.255.255.240'),
        ('ip default-gateway 192.168.99.1', 'ip default-gateway 10.100.39.241'),
        
        # Textos de anotações
        ('192.168.99.2/24', '10.100.39.242/28'),
        ('192.168.99.1', '10.100.39.241'),
    ]
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(out_xml, 'w', encoding='utf-8') as f:
        f.write(content)
        
    encode_xml_file(out_xml, target_pkt)
    print(f"Inspetoria migrada com sucesso para: {target_pkt}")
    
    report = structural_check(target_pkt)
    print("Verificação estrutural:", report.device_count, "dispositivos,", report.link_count, "enlaces.")

if __name__ == '__main__':
    migrate_inspetoria()
