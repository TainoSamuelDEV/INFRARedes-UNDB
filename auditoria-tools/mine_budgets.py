import os

def dump_budget_tables():
    files = {
        'Portaria TP': 'extracted_reports/portaria_tp.txt',
        'Prédio Adm': 'extracted_reports/predio_adm.txt',
        'Pera Ferroviária': 'extracted_reports/full_pera_ferroviaria.txt',
        'Prédio Inspetoria': 'extracted_reports/full_predio_inspetoria.txt',
        'Silo de Grãos': 'extracted_reports/full_silo_de_graos.txt'
    }
    
    with open('tabelas_orcamento_mineradas.txt', 'w', encoding='utf-8') as out:
        for name, path in files.items():
            out.write(f"\n=======================================================\n")
            out.write(f"ORÇAMENTO E MATERIAIS: {name}\n")
            out.write(f"=======================================================\n")
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                recording = False
                for l in lines:
                    low = l.lower()
                    if any(k in low for k in ['orçamento', 'lista de materiais', '7 lista', '11 lista', '12 lista', '13 consolidação']):
                        recording = True
                    if recording:
                        out.write(l)
                        if any(k in low for k in ['conclusão', 'referências', '8 plano de', '14 cronograma', '15 riscos']):
                            if len(l.strip()) < 50 and not 'r$' in low:
                                recording = False

dump_budget_tables()
print("Tabelas mineradas salvas.")
