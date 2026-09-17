# Relatório de validação — Portaria TP

**Data:** 16/09/2026  
**Autores:** Taino Samuel Lima Ribeiro e Victor Eduard Rodrigues Cabral  
**Arquivo:** `03-Packet-Tracer/Portaria-TP-Taino-Victor.pkt`

## Resultado geral

O arquivo final foi aberto no Cisco Packet Tracer 9.0.1 sem alerta de incompatibilidade. A inspeção interna identificou 15 dispositivos, 13 enlaces cabeados e os nove pontos locais da Portaria TP. A estrutura lógica e a estrutura física internas foram aprovadas pelo verificador, sem itens bloqueadores. A análise de coerência não encontrou contradições.

## Conferência dos requisitos do desafio

| Requisito da Portaria TP | Evidência no pacote | Situação |
|---|---|---|
| Um computador | PC-PT `PC-RECEPCAO`, Fa0/1, VLAN 10 | Conferido |
| Um telefone | IPPhone 7960 `TEL-RECEPCAO`, Fa0/2, VLAN 20 | Conferido |
| Uma impressora | Printer-PT `IMP-RECEPCAO`, Fa0/3, VLAN 10 | Conferido |
| Catraca | RFID Reader `CTRL-CATRACA`, Fa0/4, VLAN 40 | Conferido para conectividade do controlador |
| Duas câmeras internas | `CAM-INT-01` e `CAM-INT-02`, VLAN 30 | Conferido |
| Câmera externa A | `CAM-EXT-A`, VLAN 30 | Conferido |
| Câmera externa B | `CAM-EXT-B`, VLAN 30 | Conferido |
| Wi-Fi por AP | `AP-PORTARIA`, SSID `PORTARIA-TP`, cliente associado | Conferido em configuração |
| Metragem e caminhos | Planta e `Memoria-de-cabos.csv` | Conferido |
| Topologias física e lógica | PDFs e PNGs em `02-Plantas` | Conferido |
| Orçamento por ordem de grandeza | CSV e JSON em `04-Orcamento` | Conferido |

## Verificações executadas

- Abertura real no Packet Tracer 9.0.1: **aprovada**.
- Inventário: **15 dispositivos e 13 enlaces**.
- Pontos locais no `SW-TP`: **Fa0/1 a Fa0/9**.
- Dispositivos nativos: PC, dois telefones IP, impressora, leitor RFID, quatro webcams, AP e laptop.
- VLANs no `SW-CENTRAL` e no `SW-TP`: **10, 20, 30, 40, 50, 99, 200 e 999**.
- DHCP no gateway: pools **VOZ-TP** e **WIFI-TP**.
- Políticas no gateway: **ACL-WIFI-TP**, **ACL-CFTV-TP** e **ACL-CONTROLE-TP**.
- Wi-Fi: AP e cliente com SSID **PORTARIA-TP**.
- Serviços do servidor: **DNS, HTTP e HTTPS**; serviços herdados desnecessários foram desativados.
- Telefonia: ramais **1001 e 1002** e origem CME `192.168.20.1:2000`.
- Validação do workspace lógico: **aprovada**.
- Validação do workspace físico: **aprovada**.
- Coerência declarativa: **sem contradições**.

## Testes que a equipe deve demonstrar no aplicativo

As verificações acima provam abertura, estrutura e configuração. Elas não substituem a demonstração interativa. Antes da apresentação, executar e registrar:

1. PC para impressora na VLAN 10;
2. cliente Wi-Fi obtendo endereço por DHCP e acessando `portal.tp.test`;
3. tentativa do Wi-Fi contra a VLAN de gerência ou controle, esperando bloqueio;
4. câmeras e leitor RFID alcançando apenas o servidor central permitido;
5. registro e chamada entre os ramais 1001 e 1002;
6. visualização de ARP, ICMP, DNS e HTTP no modo Simulation.

Não foram declarados resultados de ping, chamada ou tráfego que não tenham sido executados interativamente. A cobertura de rádio, a alimentação PoE real, a autonomia do nobreak, a gravação de vídeo e a liberação mecânica da catraca permanecem verificações de implantação.


## Integridade do arquivo

SHA-256 do `Portaria-TP-Taino-Victor.pkt`: `20122d6fe82ca47ccbd2354cdd47e2f45ad485c5f28c25a1499743f247b9757b`.

