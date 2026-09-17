import os
import json
import pdfplumber

def read_inventory():
    with open('inventario_pastas.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for folder, files in data.items():
        print(f"\n==========================================")
        print(f"PASTA: {folder} (Total: {len(files)} arquivos)")
        print(f"==========================================")
        for item in files:
            print(f"  - {item['name']} ({item['size']:,} bytes)")

if __name__ == '__main__':
    read_inventory()
