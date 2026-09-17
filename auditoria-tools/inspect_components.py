import os

def read_inspect(name, filepath, out):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    out.write(f"\n=== {name} ({len(content)} chars) ===\n")
    lines = [l for l in content.splitlines() if l.strip()]
    for l in lines:
        if any(w in l.lower() for w in ['switch', 'router', 'cabo', 'fibra', 'distancia', 'metro', 'r$', 'orcamento', 'vlan', 'ip', 'porta', 'rack', 'poe', 'requisito', 'camera', 'telefone', 'ap', 'cat6', 'cat5']):
            out.write(f"  * {l.strip()}\n")

with open('components_out.txt', 'w', encoding='utf-8') as out:
    read_inspect("INSPETORIA", "extracted_reports/full_predio_inspetoria.txt", out)
    read_inspect("SILO", "extracted_reports/full_silo_de_graos.txt", out)
    read_inspect("PERA", "extracted_reports/full_pera_ferroviaria.txt", out)
    read_inspect("PORTARIA", "extracted_reports/portaria_tp.txt", out)
    read_inspect("ADMINISTRATIVO", "extracted_reports/predio_adm.txt", out)

print("Gravado components_out.txt com sucesso.")
