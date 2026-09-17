# Simulação do prédio administrativo

## Arquivo

Abra `Predio-Administrativo-TP.pkt` no Cisco Packet Tracer 9.0.1 ou versão compatível.

## O que está configurado

- roteador do campus, enlace de trânsito `10.255.20.0/30` e rotas de ida e volta;
- gateway do administrativo com subinterfaces 802.1Q;
- core de camada 2 e três switches de acesso;
- VLANs 110, 120, 130, 140, 150, 160, 170, 180, 190 e 200;
- quatro pools DHCP com as faixas definidas no relatório;
- endereços fixos para servidores, serviços, storage e terminais especiais;
- ACLs para dados, Wi-Fi corporativo, visitantes, câmeras e controle físico;
- DNS, RADIUS/AAA, HTTP/HTTPS, NTP e syslog nos servidores previstos;
- dois SSIDs e quatro access points;
- CME no gateway para representar a telefonia do PABX;
- servidor externo `203.0.113.53` para DNS/Web da Internet simulada.

## Leitura da topologia

Os computadores, telefones, câmeras, impressora, controle de acesso e videoconferência são amostras funcionais. A topologia não replica os 108 pontos físicos, porque o roteiro do relatório pede terminais representativos por VLAN e anotações com os quantitativos reais.

A VLAN 180 não possui gateway. Os objetos `SRV01-STG-NIC`, `SRV02-STG-NIC` e `SRV03-STG-NIC` representam a segunda interface de storage dos três servidores físicos, pois o `Server-PT` básico possui uma interface Ethernet.

## Equivalências do simulador

- `3560-24PS` representa os switches propostos; a simulação verifica VLANs, trunks e políticas, sem afirmar equivalência de portas, capacidade PoE ou desempenho.
- `AccessPoint-PT` usa WPA2-PSK para permitir associação no simulador. O projeto de produção permanece WPA2/WPA3 Enterprise com RADIUS.
- o CME do roteador representa a função de chamadas do PABX UCM6301.
- o servidor externo representa um destino de Internet autorizado para visitantes.

As chaves Wi-Fi existem apenas para o laboratório acadêmico e não devem ser reutilizadas em uma implantação real.
