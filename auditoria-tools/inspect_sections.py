import os

def read_full(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

files = {
    'Pera Ferroviária': 'extracted_reports/pera_ferroviaria.txt',
    'Portaria TP': 'extracted_reports/portaria_tp.txt',
    'Prédio Adm': 'extracted_reports/predio_adm.txt',
    'Prédio Inspetoria': 'extracted_reports/predio_inspetoria.txt',
    'Silo de Grãos': 'extracted_reports/silo_graos.txt'
}

for name, p in files.items():
    txt = read_full(p)
    print(f"\n=======================================================")
    print(f"ANÁLISE DETALHADA: {name.upper()}")
    print(f"=======================================================")
    # Print headings and sections
    lines = txt.splitlines()
    for l in lines:
        l_str = l.strip()
        if l_str.startswith('#') or (len(l_str) > 3 and l_str[0].isdigit() and l_str[1] in '. ') or 'orçamento' in l_str.lower() or 'requisitos' in l_str.lower() or 'topologia' in l_str.lower() or 'risco' in l_str.lower():
            if len(l_str) < 100:
                print("  SECTION:", l_str)
