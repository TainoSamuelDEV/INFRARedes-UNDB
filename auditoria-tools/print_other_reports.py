import os

def examine_reports():
    files = {
        'Pera Ferroviaria': 'extracted_reports/pera_ferroviaria.txt',
        'Predio Inspetoria': 'extracted_reports/predio_inspetoria.txt',
        'Silo de Graos': 'extracted_reports/silo_graos.txt'
    }
    
    with open('all_other_reports.txt', 'w', encoding='utf-8') as out:
        for name, path in files.items():
            out.write(f"\n==================================================\n")
            out.write(f"CONTEÚDO COMPLETO: {name}\n")
            out.write(f"==================================================\n")
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    out.write(f.read())
            else:
                out.write(f"Arquivo {path} não encontrado.\n")

if __name__ == '__main__':
    examine_reports()
    print("Salvo all_other_reports.txt com sucesso.")
