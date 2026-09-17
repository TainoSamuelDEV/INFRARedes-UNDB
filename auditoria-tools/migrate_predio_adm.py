import sys
import os
import xml.etree.ElementTree as ET

sys.path.append(r'C:\Users\Admin\Documents\ChatGPT\New project\packet-tracer-skill\scripts')
from pkt_codec import encode_xml_file
from pkt_verify import structural_check

def migrate_predio_adm():
    xml_path = 'pkt_xmls/predio_adm.xml'
    out_xml = 'pkt_xmls/predio_adm_migrated.xml'
    target_pkt = r'Predio-Administrativo(Gabriel Ordonez e Higor Gabriel)\03-Packet-Tracer\Predio-Administrativo-TP.pkt'
    
    with open(xml_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Adicionar rotas para o bloco 10.100.0.0/16 do campus no RTR-CAMPUS
    old_route = '<LINE>ip route 10.20.0.0 255.255.0.0 10.255.20.2</LINE>'
    new_routes = (
        '<LINE>ip route 10.20.0.0 255.255.0.0 10.255.20.2</LINE>\n'
        '  <LINE>ip route 10.100.0.0 255.255.0.0 10.255.20.2</LINE>'
    )
    
    content = content.replace(old_route, new_routes, 1)
    
    with open(out_xml, 'w', encoding='utf-8') as f:
        f.write(content)
        
    encode_xml_file(out_xml, target_pkt)
    print(f"Prédio Administrativo atualizado com sucesso para: {target_pkt}")
    
    report = structural_check(target_pkt)
    print("Verificação estrutural:", report.device_count, "dispositivos,", report.link_count, "enlaces.")

if __name__ == '__main__':
    migrate_predio_adm()
