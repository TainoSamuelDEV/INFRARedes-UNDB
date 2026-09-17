import json
import re
import os

def load_file(path):
    if not os.path.exists(path):
        return ""
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def parse_all():
    sectors = {
        'portaria': {
            'name': 'Portaria TP (Taino Samuel e Victor Cabral)',
            'path': 'extracted_reports/portaria_tp.txt',
            'pkt': 'Portaria-TP(Taino Samuel e Victor Cabral)/03-Packet-Tracer/Portaria-TP-Taino-Victor.pkt',
            'orcamento_csv': 'Portaria-TP(Taino Samuel e Victor Cabral)/04-Orcamento/Orcamento-Portaria-TP.csv',
            'dados_json': 'Portaria-TP(Taino Samuel e Victor Cabral)/04-Orcamento/dados-orcamento.json',
            'validacao': 'Portaria-TP(Taino Samuel e Victor Cabral)/05-Validacao/Relatorio-de-validacao.md',
            'memoria_cabos': 'Portaria-TP(Taino Samuel e Victor Cabral)/02-Plantas/Memoria-de-cabos.csv'
        },
        'predio_adm': {
            'name': 'Prédio Administrativo (Gabriel Ordonez e Higor Gabriel)',
            'path': 'extracted_reports/predio_adm.txt',
            'pkt': 'Predio-Administrativo(Gabriel Ordonez e Higor Gabriel)/03-Packet-Tracer/Predio-Administrativo-TP.pkt',
            'validacao': 'Predio-Administrativo(Gabriel Ordonez e Higor Gabriel)/05-Validacao/Relatorio-de-validacao.md',
            'roteiro': 'Predio-Administrativo(Gabriel Ordonez e Higor Gabriel)/05-Validacao/Roteiro-de-testes-manuais.md',
            'resultado': 'Predio-Administrativo(Gabriel Ordonez e Higor Gabriel)/05-Validacao/resultado-verificacao.json'
        },
        'pera_ferroviaria': {
            'name': 'Pera Ferroviária (João Lucas e Jaylon Coelho)',
            'path': 'extracted_reports/full_pera_ferroviaria.txt',
            'pkt': 'Pera-Ferroviaria(João Lucas e Jaylon Coelho)/Pera Ferroviária.pkt'
        },
        'predio_inspetoria': {
            'name': 'Prédio Inspetoria | Berço 098 (Mateus Dantas e Renan Pires)',
            'path': 'extracted_reports/full_predio_inspetoria.txt',
            'pkt': 'Predio-Inspetoria(Mateus Dantas e Renan Pires)/Predio-Inspetoria-Berco-098-mapa-estrela.pkt'
        },
        'silo_graos': {
            'name': 'Silo de Grãos (Asafe e Lucas)',
            'path': 'extracted_reports/full_silo_de_graos.txt',
            'pkt': 'Silo-Grãos(Asafe e Lucas)/Estrutura_Silo_de_Graos.pkt'
        }
    }
    
    audit_data = {}
    for key, data in sectors.items():
        txt = load_file(data['path'])
        
        # Extrair dados de orçamento se houver
        budget_items = []
        budget_total = "Não consolidado formalmente"
        
        # Buscar totais no texto
        totals = re.findall(r'total[^\n]*R\$\s*[\d\.,]+', txt, re.IGNORECASE)
        all_prices = re.findall(r'R\$\s*[\d\.,]+', txt)
        
        # Buscar VLANs e sub-redes
        vlans = re.findall(r'vlan\s*(\d+)', txt, re.I)
        subnets = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2})', txt)
        switches = re.findall(r'([A-Za-z0-9\-]+(?:2960|3560|3650|3850|3750|9200|9300|CBS[0-9]+|switch|industrial)[A-Za-z0-9\-]*)', txt, re.I)
        
        audit_data[key] = {
            'meta': data,
            'text_len': len(txt),
            'totals_found': totals,
            'prices_count': len(all_prices),
            'vlans': sorted(list(set(vlans))),
            'subnets': sorted(list(set(subnets))),
            'raw_text': txt
        }
        
    with open('parsed_audit_data.json', 'w', encoding='utf-8') as out:
        # Don't dump raw text to json to keep it readable
        dumpable = {}
        for k, v in audit_data.items():
            dumpable[k] = {
                'name': v['meta']['name'],
                'text_len': v['text_len'],
                'totals_found': v['totals_found'],
                'vlans': v['vlans'],
                'subnets': v['subnets']
            }
        json.dump(dumpable, out, indent=2, ensure_ascii=False)
        
    print("Parsed audit data concluído.")

if __name__ == '__main__':
    parse_all()
