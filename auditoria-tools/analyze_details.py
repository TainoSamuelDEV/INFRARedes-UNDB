import json
import re

def analyze_sector(name, filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    print(f"\n=======================================================")
    print(f"RESUMO COMPLETO DE AUDITORIA: {name}")
    print(f"=======================================================")
    
    # 1. Metodologia
    has_ppdioo = 'ppdioo' in text.lower()
    has_tia = bool(re.search(r'tia|eia', text, re.I))
    has_nbr = 'nbr' in text.lower()
    has_iso = 'iso' in text.lower()
    print(f"Normas/Metodologias citadas:")
    print(f"  PPDIOO: {has_ppdioo} | TIA/EIA: {has_tia} | ABNT NBR: {has_nbr} | ISO: {has_iso}")
    
    # 2. Requisitos verificados
    print("\nTrechos de Topologia Lógica / IPs / VLANs:")
    for line in text.splitlines():
        if any(k in line.lower() for k in ['vlan', '192.168.', '10.20.', 'switch', 'cat6', 'cat5', 'fibra', 'orçamento', 'total', 'r$']):
            if len(line.strip()) < 120 and len(line.strip()) > 5:
                print("  ", line.strip())

analyze_sector("PERA FERROVIÁRIA", "extracted_reports/full_pera_ferroviaria.txt")
analyze_sector("PREDIO INSPETORIA", "extracted_reports/full_predio_inspetoria.txt")
analyze_sector("SILO DE GRÃOS", "extracted_reports/full_silo_de_graos.txt")
