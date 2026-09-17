# Roteiro de testes manuais no Packet Tracer

Espere cerca de 30 segundos após abrir o arquivo para DHCP, spanning tree e associação Wi-Fi convergirem. Descarte o primeiro ping de cada origem e registre a segunda tentativa.

## 1. Comunicação autorizada

1. Em `PC-DADOS-01`, confirme o endereço DHCP da rede `10.20.10.0/24`.
2. Execute `ping 10.20.10.1`.
3. Execute `ping 10.20.60.11` para alcançar o servidor de aplicação.
4. Execute `ping 10.20.100.10` para alcançar a impressora.

Critério: endereço entre `.50` e `.199` e respostas aos três destinos autorizados.

## 2. Isolamento de visitantes

1. Em `CLIENTE-VISITANTE`, confirme associação ao SSID `TP-VISITANTES` e endereço da rede `10.20.40.0/24`.
2. Execute `ping 203.0.113.53`.
3. Execute `ping 10.20.60.11`.
4. Execute `ping 10.20.70.2`.
5. Execute `ping 10.20.80.2`.

Critério: o destino externo responde; aplicação interna, gerência e storage falham.

## 3. Câmeras e controle físico

1. Em `CAM-REP-01`, execute `ping 10.20.60.13` e depois `ping 10.20.60.14`.
2. Em `AC-REP-01`, execute `ping 10.20.60.14` e depois `ping 10.20.60.13`.

Critério: a câmera alcança o NVR e não a gestão de acesso; o controle alcança a gestão de acesso e não o NVR.

## 4. Storage sem roteamento

1. Em `NAS01`, confirme `10.20.80.2/28` e gateway vazio.
2. Execute `ping 10.20.80.11`.
3. Execute `ping 10.20.60.2`.

Critério: a interface de storage do servidor responde na mesma VLAN; a rede de serviços não é alcançada pela VLAN 180.

## 5. Telefonia

1. Aguarde os telefones obterem endereço na VLAN 120.
2. Confirme os ramais 2101 e 2102.
3. Faça uma chamada entre os dois telefones.

Critério: registro e chamada interna concluídos.

## 6. Falha de uplink

1. Escolha o enlace `SW-ADM-01`–`CORE-ADM-01` e desligue uma das interfaces.
2. Repita o ping de `PC-DADOS-01` ao gateway.
3. Reative a interface e aguarde a convergência.
4. Repita o ping.

Critério: o acesso falha com o uplink desligado e volta após a reativação.

## Registro sugerido

Para cada teste, registre código, data, origem, destino, resultado esperado, resultado observado e captura de tela. Não salve o arquivo final com interfaces desligadas.
