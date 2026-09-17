import xml.etree.ElementTree as ET

def find_configs(xml_file):
    tree = ET.parse(xml_file)
    configs = {}
    for dev in tree.iter('DEVICE'):
        name = dev.findtext('./ENGINE/NAME', default='').strip()
        rc = dev.find('.//RUNNINGCONFIG')
        if rc is not None:
            lines = [l.text for l in rc.findall('LINE') if l.text]
            configs[name] = lines
    return configs

for name in ['portaria', 'inspetoria', 'pera', 'silo', 'predio_adm']:
    cfgs = find_configs(f'pkt_xmls/{name}.xml')
    print(f"\n==========================================")
    print(f"DISPOSITIVOS COM RUNNINGCONFIG EM: {name.upper()}")
    print(f"==========================================")
    for dev_name, lines in cfgs.items():
        print(f"Dispositivo: {dev_name} ({len(lines)} linhas)")
        for l in lines:
            if any(k in l.lower() for k in ['hostname', 'interface fast', 'interface gig', 'ip address', 'network', 'default-router', 'vlan ']):
                print(f"   {l.strip()}")
