import os

with open('components_out.txt', 'r', encoding='utf-8') as f:
    text = f.read()

sections = text.split('=== ')
for s in sections[1:]:
    lines = s.splitlines()
    header = lines[0]
    items = lines[1:]
    print(f"SEÇÃO: {header} | Total de linhas relevantes: {len(items)}")
    # vamos exibir os 20 primeiros de Silo e Pera para conferir
    if 'SILO' in header or 'PERA' in header or 'INSPETORIA' in header:
        print(f"--- Amostra de {header} ---")
        for it in items[:25]:
            print("  ", it[:100].encode('ascii', errors='replace').decode('ascii'))
