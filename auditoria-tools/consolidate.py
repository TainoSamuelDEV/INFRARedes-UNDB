import json
import re

# Consolidar dados precisos de cada setor
sectors_data = {
    'Portaria-TP': {
        'dupla': 'Taino Samuel Lima Ribeiro e Victor Eduard Rodrigues Cabral',
        'documentos': ['Entendimento-Portaria-TP.md', 'Relatorio-Portaria-TP.md', 'Relatorio-Portaria-TP.pdf', 'Relatorio-Portaria-TP.docx', '01-Planta-encaminhamento.png', '02-Topologia-fisica.png', '03-Topologia-logica.png', 'Memoria-de-cabos.csv', 'Orcamento-Portaria-TP.csv', 'dados-orcamento.json', 'Relatorio-de-validacao.md', 'Portaria-TP-Taino-Victor.pkt'],
        'orcamento_local': 29347.83,
        'orcamento_enlace': 3634.00,
        'orcamento_total': 32981.83,
        'switches': '1x Switch PoE+ 24 portas (reserva 9 portas locais)',
        'pontos_enunciado': 9, # 1 PC, 1 Tel, 1 Imp, 1 Catraca, 2 Cam Int, 2 Cam Ext, 1 AP
        'vlans': {'10': 'Dados (PC/Imp)', '20': 'Voz (Tel)', '30': 'CFTV (4 câmeras)', '40': 'Controle de Acesso', '50': 'Wi-Fi Corporativo', '99': 'Gerência', '200': 'Trânsito Núcleo'},
        'subnets': {'VLAN 10': '192.168.10.0/24', 'VLAN 20': '192.168.20.0/24', 'VLAN 30': '192.168.30.0/24', 'VLAN 40': '192.168.40.0/24', 'VLAN 50': '192.168.50.0/24', 'VLAN 99': '192.168.99.0/24', 'VLAN 200': '192.168.200.0/24'},
        'pkt_devices': 15,
        'pkt_links': 13
    },
    'Predio-Administrativo': {
        'dupla': 'Gabriel Ordonez e Higor Gabriel',
        'documentos': ['Projeto_de_Redes_Predio_Administrativo_TP.docx', 'Predio-Administrativo-TP.pkt', 'Relatorio-de-validacao.md', 'Roteiro-de-testes-manuais.md', 'resultado-verificacao.json', 'inventario-validacao.json'],
        'orcamento_passivos': 48120.00,
        'orcamento_ativos': 48100.00,
        'orcamento_servidores_energia': 206100.00,
        'orcamento_implantacao': 53700.00,
        'orcamento_terminais': 234500.00,
        'orcamento_subtotal': 590520.00,
        'orcamento_total_com_contingencia': 708624.00,
        'switches': '1x Core L3 3560-24PS + 3x Acesso 3560-24PS + 1x Gateway 1941',
        'pontos_enunciado': '40 postos, 4 VC, 46 VoIP, 3 Imp, 3 Acesso, 8 Câmeras (6 int + 2 ext), 3 Servidores + 1 Storage NAS, 4 APs',
        'vlans': {'110': 'Diretoria/Admin', '120': 'Staff', '130': 'Reunião/VC', '140': 'Wi-Fi Visitantes', '150': 'Wi-Fi Corp', '160': 'Serviços/CFTV/Acesso', '170': 'Gerência', '180': 'Storage SAN/NAS', '190': 'Voz VoIP', '200': 'Impressoras'},
        'subnets': {'VLAN 110': '10.20.10.0/24', 'VLAN 120': '10.20.20.0/24', 'VLAN 130': '10.20.30.0/24', 'VLAN 140': '10.20.40.0/24', 'VLAN 150': '10.20.50.0/27', 'VLAN 160': '10.20.60.0/27', 'VLAN 170': '10.20.70.0/27', 'VLAN 180': '10.20.80.0/28', 'VLAN 190': '10.20.90.0/27', 'VLAN 200': '10.20.100.0/27', 'Trânsito': '10.255.20.0/30'},
        'pkt_devices': 36,
        'pkt_links': 33
    },
    'Pera-Ferroviaria': {
        'dupla': 'João Lucas Magalhães Gomes e Jaylon Coelho Saldanha',
        'documentos': ['Relatório Geral - Pera Ferroviária.pdf', 'Relatório Geral - Pera Ferroviária.docx', 'Pera Ferroviária.pkt'],
        'orcamento_subtotal': 113740.00,
        'orcamento_total_com_contingencia': 125114.00,
        'switches': '2x Switches Industriais Outdoor IP67 + Conexão ao Switch Core CCO',
        'pontos_enunciado': '10 câmeras IP PoE+ e 2 balanças ferroviárias (600m x 30m)',
        'vlans': {'20': 'CFTV (10 câmeras)', '30': 'Automação (Balanças)', '99': 'Gerência'},
        'subnets': {'VLAN 20': '192.168.20.0/24', 'VLAN 30': '192.168.30.0/24', 'VLAN 99': '192.168.99.0/24'}
    },
    'Predio-Inspetoria': {
        'dupla': 'Mateus Dantas e Renan Pires',
        'documentos': ['relatorioinspetoriaberco098.pdf', 'Predio-Inspetoria-Berco-098-mapa-estrela.pkt'],
        'orcamento_subtotal': 17173.93,
        'orcamento_total_com_contingencia': 18891.32,
        'switches': '1x TP-Link TL-SG3428MP PoE+ 24 portas + 1x Roteador TP-Link ER7206',
        'pontos_enunciado': '8 mesas operadores com telefonia, 1 mesa sala equipamentos, 2 postos automação, 2 câmeras int, 8 câmeras ext, 1 controle acesso',
        'vlans': {'10': 'Dados (PCs/Imp)', '20': 'Voz (Telefones IP)', '30': 'Wi-Fi Corp/Visitantes', '40': 'CFTV (10 câmeras)', '99': 'Gerência'},
        'subnets': {'VLAN 10': '192.168.10.0/24', 'VLAN 20': '192.168.20.0/24', 'VLAN 30': '192.168.30.0/24', 'VLAN 40': '192.168.40.0/24', 'VLAN 99': '192.168.99.0/24'}
    },
    'Silo-Graos': {
        'dupla': 'Asafe e Lucas',
        'documentos': ['Projeto de Rede do Silo de Grãos.pdf', 'Estrutura_Silo_de_Graos.pkt'],
        'orcamento_total': 16720.90,
        'switches': '1x Switch PoE+ TP-Link TL-SG3428MP 24 portas + Gateway IoT + AP Outdoor',
        'pontos_enunciado': 'Estrutura circular R=25m H=30m, 1 controle acesso, 4 câmeras int, 1 ext, IoT, Wi-Fi',
        'vlans': {'10': 'Dados/Admin', '50': 'CFTV (5 câmeras)', '60': 'Controle de Acesso', '70': 'Wi-Fi Operacional', '80': 'Sensores IoT'},
        'subnets': {'VLAN 10': '192.168.10.0/24', 'VLAN 50': '192.168.50.0/24', 'VLAN 60': '192.168.60.0/24', 'VLAN 70': '192.168.70.0/24', 'VLAN 80': '192.168.80.0/24'}
    }
}

with open('consolidated_data.json', 'w', encoding='utf-8') as f:
    json.dump(sectors_data, f, indent=2, ensure_ascii=False)
print("Dados consolidados salvos.")
