# Relatório de validação — Prédio Administrativo TP

Data da revisão: 17/09/2026  
Arquivo: `Predio-Administrativo-TP.pkt`  
Versão interna: `9.0.1.0858`

## Resultado

O arquivo foi gerado, revisado e aberto com sucesso no Cisco Packet Tracer 9.0.1. O verificador estrutural classificou a compatibilidade como exata, sem falhas nem avisos. A revisão específica do projeto aprovou 172 verificações.

Inventário final:

- 36 dispositivos;
- 33 enlaces físicos;
- 10 VLANs;
- 4 pools DHCP;
- 4 access points;
- 2 clientes Wi-Fi representativos;
- 3 servidores físicos representados, seus serviços em VMs, 1 NAS e 3 objetos que representam as segundas interfaces de storage;
- 1 servidor externo de DNS/Web para a Internet simulada.

SHA-256 do arquivo validado: `6d76e6cdcd4dbf979d91776fc08c3286eb18a5dc055d157ac87d0639da2959c6`.

## Conformidade com o relatório

- A topologia segue estrela hierárquica, com gateway, core e três switches de acesso.
- As VLANs 110 a 200 existem no banco interno dos quatro switches.
- Os trunks permitem somente as VLANs roteadas. A VLAN 180 fica restrita ao core e não possui subinterface nem gateway.
- Os gateways, máscaras e endereços fixos coincidem com o plano da seção 7.
- As exclusões DHCP produzem exatamente as faixas `.50–.199`, `.50–.149`, `.50–.229` e `.20–.229`.
- O enlace de trânsito usa campus `.1` e administrativo `.2`; há rota padrão para o campus e rota de retorno para `10.20.0.0/16`.
- Visitantes recebem DNS externo e são bloqueados para `10.20.0.0/16`.
- Câmeras alcançam DNS, NTP e NVR; o restante é negado.
- Controle de acesso alcança DNS, NTP e o servidor de gestão; o restante é negado.
- Dados e Wi-Fi corporativo não alcançam gerência nem storage.
- Os SSIDs, chaves e canais planejados estão gravados nos quatro APs; os dois clientes possuem apenas o perfil correspondente.
- Os serviços herdados dos modelos foram removidos. Somente os serviços planejados permanecem habilitados.
- Running-config e startup-config estão sincronizados nos equipamentos IOS.
- Não há interfaces repetidas, pools duplicados, portas com dois cabos, endereços IP ou MAC duplicados, trunks incompatíveis ou pools sem interface roteada.

## Exceções intencionais

O verificador geral registra quatro hosts sem gateway: `NAS01`, `SRV01-STG-NIC`, `SRV02-STG-NIC` e `SRV03-STG-NIC`. Esse resultado é esperado e comprova o requisito de isolamento da VLAN 180. Nenhum outro alerta de coerência permaneceu.

## Equivalências documentadas

- Os terminais são representativos, como orienta a seção 15 do relatório. As notas internas registram 40 postos, 46 telefones, 4 APs, 8 câmeras, 3 controles de acesso, 3 impressoras, 4 salas de videoconferência, 3 servidores e 1 NAS.
- O Packet Tracer não contém os modelos comerciais definidos no orçamento. Os modelos Cisco disponíveis representam as funções lógicas.
- O `Server-PT` básico não oferece duas interfaces Ethernet. Cada objeto `SRVxx-STG-NIC` representa a interface de storage do mesmo servidor físico, sem criar um quarto, quinto ou sexto servidor no projeto real.
- WPA2-PSK permite associação dos clientes no laboratório. A solução de produção descrita no documento continua usando WPA2/WPA3 Enterprise e RADIUS.
- O CME do gateway permite representar a função de telefonia; o equipamento real previsto continua sendo o UCM6301.

## Evidência executada

- decodificação e leitura integral do contêiner `.pkt`;
- compatibilidade exata com a versão instalada;
- inventário de dispositivos e enlaces;
- validação de workspace físico e referências internas;
- 172 verificações específicas do projeto;
- verificação cruzada de coerência;
- abertura real do arquivo no Cisco Packet Tracer 9.0.1, confirmada pelo título da janela em 9 segundos.

## Limite da revisão automatizada

O ambiente disponível não expôs a ponte de automação interna do Packet Tracer para emitir pings e capturar o painel de simulação. Por isso, os testes de tráfego da apresentação continuam no roteiro manual anexo. Não se declara como executado nenhum ping que não tenha sido observado. O arquivo contém toda a configuração necessária para esses testes.

A simulação lógica também não certifica cabo, PoE, cobertura de rádio, retenção de vídeo, autonomia elétrica nem desempenho dos equipamentos reais, em acordo com o próprio relatório.
