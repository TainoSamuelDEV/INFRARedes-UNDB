import sys
import json
import os

sys.path.append(r'C:\Users\Admin\Documents\ChatGPT\New project\packet-tracer-skill\scripts')
from pkt_editor import decode_pkt_to_root, inventory_root

pkts = {
    'portaria': r'Portaria-TP(Taino Samuel e Victor Cabral)\03-Packet-Tracer\Portaria-TP-Taino-Victor.pkt',
    'predio_adm': r'Predio-Administrativo(Gabriel Ordonez e Higor Gabriel)\03-Packet-Tracer\Predio-Administrativo-TP.pkt',
    'pera': r'Pera-Ferroviaria(João Lucas e Jaylon Coelho)\Pera Ferroviária.pkt',
    'inspetoria': r'Predio-Inspetoria(Mateus Dantas e Renan Pires)\Predio-Inspetoria-Berco-098-mapa-estrela.pkt',
    'silo': r'Silo-Grãos(Asafe e Lucas)\Estrutura_Silo_de_Graos.pkt'
}

all_invs = {}
for name, path in pkts.items():
    if os.path.exists(path):
        root = decode_pkt_to_root(path)
        inv = inventory_root(root)
        all_invs[name] = inv
        print(f"=== {name.upper()} ===")
        print(f"Dispositivos ({len(inv.get('devices', []))}): {[d['name'] for d in inv.get('devices', [])]}")
        print(f"VLANs: {inv.get('vlans', {})}")
        print(f"DHCP Pools: {inv.get('dhcp_pools', {})}")
        print(f"Routing: {inv.get('routing', {})}")
        print(f"Voice: {inv.get('voice', {})}")
        print(f"Wireless: {inv.get('wireless', {})}")

with open('auditoria-tools/all_pkt_inventories.json', 'w', encoding='utf-8') as f:
    json.dump(all_invs, f, indent=2, ensure_ascii=False)

print("\nInventários salvos em auditoria-tools/all_pkt_inventories.json")
