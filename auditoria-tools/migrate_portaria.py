import sys
import os
import re
import xml.etree.ElementTree as ET

sys.path.append(r'C:\Users\Admin\Documents\ChatGPT\New project\packet-tracer-skill\scripts')
from pkt_codec import encode_xml_file
from pkt_verify import structural_check

def migrate_portaria():
    xml_path = 'pkt_xmls/portaria.xml'
    out_xml = 'pkt_xmls/portaria_migrated.xml'
    target_pkt = r'Portaria-TP(Taino Samuel e Victor Cabral)\03-Packet-Tracer\Portaria-TP-Taino-Victor.pkt'
    
    with open(xml_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Substituições textuais
    replacements = [
        # Sub-redes e máscaras
        ('192.168.10.0 255.255.255.0', '10.100.28.0 255.255.255.240'),
        ('192.168.20.0 255.255.255.0', '10.100.28.16 255.255.255.240'),
        ('192.168.30.0 255.255.255.0', '10.100.28.32 255.255.255.240'),
        ('192.168.40.0 255.255.255.0', '10.100.28.48 255.255.255.240'),
        ('192.168.50.0 255.255.255.0', '10.100.28.64 255.255.255.240'),
        ('192.168.99.0 255.255.255.0', '10.100.28.128 255.255.255.240'),
        ('192.168.200.0 255.255.255.0', '10.100.28.144 255.255.255.240'),
        
        # Excluded addresses
        ('192.168.20.1 192.168.20.99', '10.100.28.17 10.100.28.19'),
        ('192.168.50.1 192.168.50.99', '10.100.28.65 10.100.28.69'),
        
        # Gateways / IPs de interface
        ('192.168.10.1 255.255.255.0', '10.100.28.1 255.255.255.240'),
        ('192.168.20.1 255.255.255.0', '10.100.28.17 255.255.255.240'),
        ('192.168.30.1 255.255.255.0', '10.100.28.33 255.255.255.240'),
        ('192.168.40.1 255.255.255.0', '10.100.28.49 255.255.255.240'),
        ('192.168.50.1 255.255.255.0', '10.100.28.65 255.255.255.240'),
        ('192.168.99.1 255.255.255.0', '10.100.28.129 255.255.255.240'),
        ('192.168.200.1 255.255.255.0', '10.100.28.145 255.255.255.240'),

        # Default routers e DNS
        ('default-router 192.168.20.1', 'default-router 10.100.28.17'),
        ('option 150 ip 192.168.20.1', 'option 150 ip 10.100.28.17'),
        ('default-router 192.168.50.1', 'default-router 10.100.28.65'),
        ('dns-server 192.168.200.10', 'dns-server 10.100.28.150'),

        # Hosts fixos
        ('192.168.10.10', '10.100.28.10'), # PC Recepção
        ('192.168.10.20', '10.100.28.11'), # Impressora
        ('192.168.40.10', '10.100.28.50'), # Catraca
        ('192.168.30.11', '10.100.28.35'), # Cam Int 01
        ('192.168.30.12', '10.100.28.36'), # Cam Int 02
        ('192.168.30.13', '10.100.28.37'), # Cam Ext A
        ('192.168.30.14', '10.100.28.38'), # Cam Ext B
        ('192.168.200.10', '10.100.28.150'), # SRV Central
        ('192.168.99.2', '10.100.28.130'), # SW-CENTRAL
        ('192.168.99.3', '10.100.28.131'), # SW-TP
        
        # Gateways individuais restantes
        ('192.168.10.1', '10.100.28.1'),
        ('192.168.20.1', '10.100.28.17'),
        ('192.168.30.1', '10.100.28.33'),
        ('192.168.40.1', '10.100.28.49'),
        ('192.168.50.1', '10.100.28.65'),
        ('192.168.99.1', '10.100.28.129'),
        ('192.168.200.1', '10.100.28.145'),
    ]
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(out_xml, 'w', encoding='utf-8') as f:
        f.write(content)
        
    encode_xml_file(out_xml, target_pkt)
    print(f"Portaria TP migrada com sucesso para: {target_pkt}")
    
    report = structural_check(target_pkt)
    print("Verificação estrutural:", report.device_count, "dispositivos,", report.link_count, "enlaces.")

if __name__ == '__main__':
    migrate_portaria()
