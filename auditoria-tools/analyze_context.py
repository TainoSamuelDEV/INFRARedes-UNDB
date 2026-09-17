import pdfplumber
import glob
import os
import json

def analyze_uas():
    uas = sorted(glob.glob('UA *.pdf'))
    with open('resumo_uas.txt', 'w', encoding='utf-8') as out:
        for u in uas:
            out.write(f'=== ARQUIVO: {u} ===\n')
            with pdfplumber.open(u) as pdf:
                out.write(f'Total de paginas: {len(pdf.pages)}\n')
                for i, page in enumerate(pdf.pages):
                    text = page.extract_text() or ''
                    lines = [l.strip() for l in text.split('\n') if l.strip()]
                    if lines:
                        out.write(f'P{i+1}: {lines[0]}\n')
                        for line in lines:
                            low = line.lower()
                            if any(k in low for k in ['norma', 'tia', 'eia', 'iso', 'nbr', 'cat5', 'cat6', 'cat6a', 'cat7', 'fibra', 'par tran', 'switch', 'router', 'vlan', 'subnet', 'sub-rede', 'ppdioo', 'topologia', 'rack', 'patch', 'horizontal', 'backbone', 'osi', 'tcp', 'distancia', '90m', '100m', 'canal', 'enlace']):
                                out.write(f'   -> {line}\n')

def analyze_all_files():
    data = {}
    # Let's inspect each directory
    dirs = [d for d in os.listdir('.') if os.path.isdir(d) and not d.startswith('.')]
    for d in sorted(dirs):
        data[d] = []
        for root, _, files in os.walk(d):
            for f in files:
                path = os.path.join(root, f)
                sz = os.path.getsize(path)
                data[d].append({'path': path, 'size': sz, 'name': f})
    
    with open('inventario_pastas.json', 'w', encoding='utf-8') as out:
        json.dump(data, out, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    analyze_uas()
    analyze_all_files()
    print("Concluído levantamento inicial.")
