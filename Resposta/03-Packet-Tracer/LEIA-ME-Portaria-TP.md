# Laboratório Cisco Packet Tracer — Portaria TP

## Arquivo principal

`Portaria-TP-Taino-Victor.pkt`

Validado no Cisco Packet Tracer 9.0.1 em 16/09/2026. O arquivo foi aberto pelo aplicativo sem alerta de incompatibilidade.

## Escopo representado

A topologia contém 15 dispositivos e 13 enlaces cabeados. Os nove pontos locais exigidos para a portaria estão ligados ao `SW-TP`:

1. `PC-RECEPCAO` — Fa0/1, VLAN 10;
2. `TEL-RECEPCAO` — Fa0/2, VLAN 20;
3. `IMP-RECEPCAO` — Fa0/3, VLAN 10;
4. `CTRL-CATRACA` — Fa0/4, VLAN 40, leitor RFID nativo;
5. `CAM-INT-01` — Fa0/5, VLAN 30;
6. `CAM-INT-02` — Fa0/6, VLAN 30;
7. `CAM-EXT-A` — Fa0/7, VLAN 30;
8. `CAM-EXT-B` — Fa0/8, VLAN 30;
9. `AP-PORTARIA` — Fa0/9, VLAN 50.

O `SW-CENTRAL`, o `GW-CENTRAL`, o `SRV-CENTRAL` e o `RAMAL-TESTE` formam o núcleo mínimo de laboratório. Eles permitem testar roteamento, DHCP, DNS, HTTP/HTTPS e telefonia sem antecipar a arquitetura definitiva da equipe.

Todos os terminais da portaria usam objetos próprios do Packet Tracer: PC-PT, IPPhone 7960, Printer-PT, RFID Reader, quatro Webcams IoT, AccessPoint-PT e Laptop-PT. O leitor RFID representa o controlador eletrônico conectado à catraca; a parte mecânica da catraca não é simulada.

## Configuração principal

- VLANs: 10 recepção, 20 voz, 30 CFTV, 40 controle, 50 Wi-Fi, 99 gerência, 200 serviços e 999 nativa sem usuários.
- Gateways: `192.168.<VLAN>.1/24` no `GW-CENTRAL`.
- IPs fixos: PC `.10`, impressora `.20`, câmeras `.11` a `.14`, leitor RFID `.10`, servidor `192.168.200.10` e switches na VLAN 99.
- DHCP: voz e Wi-Fi, com endereços a partir de `.100`.
- Wi-Fi: SSID `PORTARIA-TP`, WPA2-PSK, chave acadêmica `PortariaTP2026`.
- Telefonia: ramais 1001 e 1002, com CME no `GW-CENTRAL`.
- ACLs: `ACL-WIFI-TP`, `ACL-CFTV-TP` e `ACL-CONTROLE-TP`.
- Serviços centrais ativos: DNS, HTTP e HTTPS.

## Como revisar

1. Abra o `.pkt` no Packet Tracer 9.0.1.
2. Confira o `SW-TP`, as portas Fa0/1 a Fa0/9 e o trunk G0/1.
3. Confira as subinterfaces e ACLs do `GW-CENTRAL`.
4. Verifique a associação do `CLIENTE-WIFI` ao SSID `PORTARIA-TP`.
5. Use Realtime e Simulation para executar os testes T03 a T09 descritos no relatório.
6. Salve uma cópia após qualquer ajuste feito pela equipe.

## Arquivos de apoio

- `inventario-validacao.json`: inventário conferido do laboratório.
- `plano-dispositivos.json`: pontos, VLANs, endereços e medidas usados na documentação.
- `../05-Validacao/Relatorio-de-validacao.md`: verificações concluídas e pendências de demonstração.

