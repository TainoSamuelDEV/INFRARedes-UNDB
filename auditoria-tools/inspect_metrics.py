import os
import re

def summarize_file(filepath):
    if not os.path.exists(filepath):
        return f"Arquivo {filepath} não encontrado."
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Extract some key phrases
    ips = set(re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}(?:/\d{1,2})?\b', content))
    vlans = set(re.findall(r'vlan\s*\d+', content, re.IGNORECASE))
    prices = set(re.findall(r'R\$\s*[\d\.,]+', content))
    
    return {
        'chars': len(content),
        'lines': len(content.splitlines()),
        'ips_found': sorted(list(ips))[:15],
        'vlans_found': sorted(list(vlans))[:10],
        'sample_prices': list(prices)[:8],
        'preview': content[:1500]
    }

for name in ['pera_ferroviaria', 'portaria_tp', 'predio_adm', 'predio_inspetoria', 'silo_graos']:
    path = f'extracted_reports/{name}.txt'
    res = summarize_file(path)
    print(f"==================================================")
    print(f"RELATÓRIO: {name}")
    print(f"Tamanho: {res['chars']} caracteres, {res['lines']} linhas")
    print(f"IPs encontrados ({len(res['ips_found'])}): {res['ips_found']}")
    print(f"VLANs encontradas ({len(res['vlans_found'])}): {res['vlans_found']}")
    print(f"Preços encontrados: {res['sample_prices']}")
    print(f"Preview inicial:\n{res['preview'][:500]}...\n")
