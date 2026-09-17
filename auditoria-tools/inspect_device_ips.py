import xml.etree.ElementTree as ET

def inspect_ips(name, xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    print(f"\n==========================================")
    print(f"DISPOSITIVOS E IPs: {name.upper()}")
    print(f"==========================================")
    for dev in root.findall('.//DEVICE'):
        d_name = dev.findtext('./ENGINE/NAME', default='').strip()
        d_type = dev.findtext('./ENGINE/TYPE', default='').strip()
        gw = dev.findtext('./ENGINE/GATEWAY', default='').strip()
        
        ports = []
        for p in dev.findall('.//PORT'):
            p_name = p.findtext('NAME', default='').strip()
            ip = p.findtext('IP', default='').strip()
            subnet = p.findtext('SUBNET', default='').strip()
            if ip and ip != '0.0.0.0':
                ports.append(f"{p_name}: {ip}/{subnet}")
        
        # Check CLI/config
        config_lines = []
        for line_node in dev.findall('.//CONFIG/LINE'):
            if line_node.text and any(k in line_node.text.lower() for k in ['ip address', 'vlan', 'interface', 'ip dhcp pool']):
                config_lines.append(line_node.text.strip())
        
        if ports or gw or config_lines:
            print(f"- {d_name} ({d_type}) [GW: {gw or 'nenhum'}]:")
            if ports:
                print(f"    Ports: {', '.join(ports)}")
            if config_lines:
                print(f"    Config ({len(config_lines)} lines): {config_lines[:4]}...")

inspect_ips('portaria', 'pkt_xmls/portaria.xml')
inspect_ips('pera', 'pkt_xmls/pera.xml')
inspect_ips('silo', 'pkt_xmls/silo.xml')
inspect_ips('inspetoria', 'pkt_xmls/inspetoria.xml')
