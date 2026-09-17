import json

def parse_full_sections():
    with open('all_other_reports.txt', 'r', encoding='utf-8', errors='ignore') as f:
        txt = f.read()

    parts = txt.split('==================================================\nCONTEÚDO COMPLETO: ')
    reports = {}
    for p in parts[1:]:
        lines = p.splitlines()
        name = lines[0].strip()
        body = '\n'.join(lines[2:])
        reports[name] = body

    # Let's save each cleanly
    for name, body in reports.items():
        clean_name = name.lower().replace(' ', '_')
        with open(f'extracted_reports/full_{clean_name}.txt', 'w', encoding='utf-8') as f_out:
            f_out.write(body)

parse_full_sections()
print("Relatórios salvos individualmente.")
