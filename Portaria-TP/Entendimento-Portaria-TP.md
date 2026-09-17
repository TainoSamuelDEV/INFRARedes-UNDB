# Portaria TP — entendimento do desafio e base para a solução

Análise em 15/09/2026. Disciplina: Infraestrutura de Redes, UNDB, semestre 2026.2.

## 1. Conclusão principal

O desafio pede um projeto de infraestrutura de rede justificável, dimensionado e documentado. A simulação no Cisco Packet Tracer deve demonstrar a parte lógica e a conectividade, acompanhada dos documentos físicos e financeiros exigidos.

O recorte inicial da dupla é **Portaria TP**, dentro de uma equipe responsável pelo complexo inteiro, conforme esclarecido pelo aluno. Portanto, os demais prédios serão projetados pela equipe e a portaria deverá integrar-se a essa solução. O enunciado geral fala em equipes de 5 a 10 alunos; a divisão interna em duplas não representa uma entrega isolada do complexo.

Este documento é uma análise preparatória. Não constitui arquivo .pkt, orçamento cotado, projeto executivo ou relatório de testes realizados.

## 2. O que é exigido expressamente

### Portaria — página 4 do enunciado

- Uma mesa com computador e telefone para a recepcionista.
- Uma impressora.
- Uma catraca para controle de acesso.
- Duas câmeras internas.
- Duas câmeras externas: uma na fachada A e outra na fachada B.

### Requisito geral que também alcança a portaria — página 3

As áreas terão rede cabeada para estações, impressoras, câmeras e controle de acesso, além de Wi-Fi por access points. Portanto, omitir Wi-Fi deixaria a proposta incompleta. A quantidade de APs não é definida pelo professor.

### Seis entregáveis — página 6

1. Descritivo textual e metodologia aplicada ao projeto.
2. Levantamento de requisitos e riscos, com justificativa para o Business Case.
3. Orçamento por ordem de grandeza, incluindo lista e justificativa dos materiais, marcas e especificações.
4. Ilustração e justificativa do percurso dos cabos, denominada “As built” no enunciado.
5. Ilustração da topologia física dos ativos de rede.
6. Ilustração da topologia lógica dos ativos de rede.

O texto ainda pede, na página 3, estimativa de metragem, quantidade de portas e localização dos equipamentos. Uma captura do Packet Tracer não cobre sozinha esses itens.

O PDF informa entrega e apresentação em **17/09**, no contexto do semestre 2026.2, e valor de **8 pontos**, repartidos em 4 pontos no qualis da P1 e 4 no da P2. Não detalha uma distribuição dos pontos entre os seis entregáveis. Também não menciona nominalmente o Packet Tracer; seu uso é uma informação trazida pelo aluno.

## 3. Leitura da planta

Na página 4, a fachada A aparece na parte inferior e a fachada B à direita. A recepção e a mesa ficam na região inferior esquerda; o sanitário ocupa parte da lateral esquerda; a espera aparece na região superior. A passagem com controle de acesso fica aproximadamente na divisão central.

As cotas aparentes de 4,63 m e 5,33 m indicam uma construção pequena, da ordem de 25 m². Essa leitura é aproximada e não substitui conferir as cotas no desenho original. Não é correto multiplicar a área por um fator e apresentar o resultado como metragem medida de cabo.

Consequências para o projeto:

- Um AP interno é uma hipótese inicial proporcional ao ambiente. Cobertura e capacidade ainda dependem de paredes, posição e número de usuários simultâneos.
- Posicionar um pequeno rack em área protegida da recepção, com acesso para manutenção, ventilação e energia. A planta não define um rack existente.
- Evitar trajetos por áreas molhadas e interferências com portas, circulação e catraca.
- Posicionar as câmeras internas para observar recepção e circulação/controle de acesso. Não orientar câmera para dentro do sanitário.
- Identificar as externas como CAM-EXT-A e CAM-EXT-B. Altura, lente, contraluz, obstáculos e campo de visão exigem definição posterior.
- A metragem deve resultar de cada percurso, incluindo trechos horizontais, subidas/descidas e folgas técnicas.

O enunciado usa “As built”. Para a entrega acadêmica, apresentar a planta de encaminhamento solicitado e esclarecer que é uma proposta de instalação; a documentação final do que foi efetivamente instalado só existe após a execução.

## 4. Inventário e dimensionamento inicial

### Quantidade de conexões

Adotando computador, telefone IP, impressora de rede, controlador de catraca e câmeras IP com conexões independentes:

- Computador: 1 porta.
- Telefone: 1 porta.
- Impressora: 1 porta.
- Controlador de acesso da catraca: 1 porta.
- Câmeras internas: 2 portas.
- Câmeras externas: 2 portas.
- AP: 1 porta.

**Total: 9 portas de acesso e 9 enlaces de cobre.** Oito equipamentos decorrem do inventário específico; o AP decorre do requisito geral. Há ainda o enlace de subida para a rede central, preferencialmente em porta óptica própria.

Telefone IP, câmeras IP e controlador Ethernet são escolhas propostas; o texto não fixa essas tecnologias. A catraca pode exigir controlador externo e alimentação própria. É o controlador que utiliza a conexão de dados, não necessariamente o mecanismo da catraca diretamente.

Não acrescentar mais uma porta apenas por o switch ter endereço de gerenciamento: ele utiliza sua própria interface lógica. Notebook ou celular de demonstração via Wi-Fi não acrescenta porta cabeada ao switch.

Alguns telefones permitem conectar o computador através de sua porta PC, economizando uma porta ativa. Para este projeto, duas tomadas independentes na mesa tornam a instalação mais simples de documentar e seguem a orientação didática da aula de cabeamento, página 35.

### Switch e energia

Um switch de 8 portas não comporta os 9 enlaces da opção adotada. A base de especificação é um **switch gerenciável com pelo menos 16 portas de acesso, suporte a VLANs, PoE/PoE+ compatível e uplink óptico**. Um modelo de 24 portas pode ser escolhido por disponibilidade, expansão ou catálogo do simulador, com justificativa de custo.

Precisam de avaliação PoE, inicialmente, quatro câmeras, um telefone e um AP: seis dispositivos. Não presumir que a catraca inteira será alimentada pelo switch.

Exemplo exclusivamente de cálculo: quatro câmeras de 10 W, telefone de 7 W e AP de 15 W resultariam em 62 W de consumo dos dispositivos; 25% de margem elevaria esse valor a 77,5 W. Esses valores **não são especificações de produtos escolhidos**. O dimensionamento definitivo deve usar potência máxima, classes/negociação PoE, perdas e reserva indicada pelo fabricante, além do limite de cada porta. Um switch com muitas portas PoE pode ter orçamento total insuficiente.

Prever nobreak para os ativos essenciais e dimensionar pela carga em watts e autonomia desejada. A capacidade em VA, isoladamente, não determina quantos minutos o sistema permanece ligado. A impressora deve ter sua carga tratada separadamente para não consumir desnecessariamente a autonomia da rede.

## 5. Arquitetura recomendada como base

### Desenho físico conceitual

```text
Rede central do terminal / CPD
    │
    │ Enlace óptico proposto; distância e interfaces a definir
    │
Rack da Portaria TP
    ├── Terminação óptica e organização do enlace
    ├── Switch gerenciável PoE
    ├── Patch panel e organização do cobre
    └── Energia protegida
            │
            ├── PC da recepção
            ├── Telefone IP
            ├── Impressora de rede
            ├── Controlador da catraca
            ├── 2 câmeras internas
            ├── Câmera externa — fachada A
            ├── Câmera externa — fachada B
            └── AP ── clientes Wi-Fi
```

Os equipamentos finais ligam-se ao switch por meio do cabeamento estruturado. Patch panel organiza terminações; não substitui switch nem executa roteamento.

Topologia local: **estrela**. A integração ao complexo forma uma estrela hierárquica. A portaria tem uma LAN cabeada e uma WLAN; a ligação entre prédios do mesmo terminal não precisa ser chamada de WAN apenas por sair do prédio.

Cobre Cat 6 é uma base de projeto para os pontos locais. A escolha do tipo de cabo e proteção externa deve considerar o trajeto. A aula de cabeamento orienta priorizar fibra no backbone, página 25, e trata de 90 m para cabeamento horizontal na página 30. A metragem efetiva e os limites do sistema completo devem ser conferidos no projeto executivo.

Fibra é uma proposta coerente para o enlace entre edifícios no ambiente portuário. Ainda faltam distância, dutos disponíveis, tipo de fibra, transceptores, conectores e condições da outra ponta. Não declarar que há fibra instalada nem estipular centenas de metros a partir da imagem aérea sem escala verificada.

### Serviços centrais

Propor integração com a rede corporativa para DHCP/DNS, telefonia, gravação/consulta de imagens, controle de acesso e saída para a Internet quando necessária.

O enunciado prevê três servidores multifunção e um storage no prédio administrativo, mas **não atribui explicitamente a eles essas funções**. Usá-los é uma premissa de arquitetura que deve ser combinada com quem projeta a rede central.

Uma portaria não exige automaticamente um roteador dedicado, um servidor local ou um novo contrato de Internet. O gateway pode estar no núcleo da rede. Se o laboratório usar um roteador para representar o núcleo, identificá-lo como infraestrutura compartilhada para não inseri-lo indevidamente no orçamento local.

## 6. Organização lógica proposta

VLAN é uma separação lógica dentro da infraestrutura comutada. O enunciado não exige números de VLAN, endereçamento, ACLs ou protocolo de roteamento específicos; são decisões que podem tornar a solução justificável e demonstrável.

Plano didático inicial, a compatibilizar com a rede do terminal:

- VLAN 10 — recepção e impressora: 192.168.10.0/24, gateway 192.168.10.1.
- VLAN 20 — voz: 192.168.20.0/24, gateway 192.168.20.1.
- VLAN 30 — câmeras: 192.168.30.0/24, gateway 192.168.30.1.
- VLAN 40 — controle de acesso: 192.168.40.0/24, gateway 192.168.40.1.
- VLAN 50 — Wi-Fi de usuários autorizados: 192.168.50.0/24, gateway 192.168.50.1.
- VLAN 99 — gerenciamento dos ativos: 192.168.99.0/24, gateway 192.168.99.1.

Essas redes são exemplos privados sem sobreposição entre si. /24 favorece legibilidade no exercício e deixa muitos endereços livres; não é o tamanho mínimo necessário. Não existe exigência de VLSM no enunciado. A rede central pode já usar esses prefixos, exigindo substituição.

Usar endereços fixos ou reservas para impressora, câmeras, controlador e gerenciamento; DHCP para estações e clientes sem fio, e para telefonia conforme o serviço adotado. Não duplicar IPs nem atribuir a clientes o endereço da rede, broadcast ou gateway.

O uplink transportará as VLANs necessárias se a opção for trunk até o núcleo. O roteamento entre VLANs ocorrerá em dispositivo de camada 3. Não presumir que um switch de camada 2 roteia entre redes.

Política inicial de comunicação:

- Recepção acessa a impressora e os serviços corporativos autorizados.
- Câmeras trocam tráfego com o sistema de vídeo autorizado e serviços técnicos necessários.
- Controlador da catraca comunica-se com o sistema de acesso autorizado.
- Telefone utiliza o serviço de telefonia e os fluxos de mídia necessários.
- Usuários Wi-Fi não administram câmeras, catraca, switches ou roteadores.
- Somente uma origem administrativa autorizada gerencia os ativos.

Separar VLANs não basta para bloquear tráfego depois de habilitar o roteamento. Aplicar ACLs ou política de firewall conforme a implementação, contemplando respostas, DHCP, DNS e outros serviços realmente usados. A matriz final precisa identificar origem, destino, protocolo, porta e regra. Um ping bloqueado não prova que todos os serviços estão bloqueados.

Wi-Fi de visitantes é uma extensão possível, **não uma exigência expressa**. Se incluído, deve ter segmento e restrições próprios. Na topologia final, o AP-PT atende somente o SSID `PORTARIA-TP` pela VLAN 50. O equipamento real proposto mantém gerenciamento separado na VLAN 99.

## 7. Como transformar em uma demonstração no Packet Tracer

### Componentes do laboratório

Representar os nove pontos previstos, um cliente Wi-Fi de teste, o switch e a integração ao núcleo. Acrescentar serviços e equipamentos externos apenas quando necessários à demonstração, identificados como “rede central simulada”.

Selecionar os modelos e módulos após conferir a versão instalada. Um equipamento existente no Packet Tracer não equivale automaticamente ao modelo comercial que será orçado, nem garante PoE ou portas ópticas compatíveis.

Na topologia final, as quatro câmeras usam Webcams IoT nativas e o controlador da catraca usa o RFID Reader nativo. Isso demonstra a conectividade e o fluxo até o servidor; não valida gravação de vídeo, biometria ou o mecanismo físico de liberação da catraca.

Para provar telefonia funcionando, prever serviço de registro/controle de chamadas e um segundo ramal de teste na rede central. Apenas conectar um telefone ou atribuir IP não demonstra uma chamada. O segundo ramal de teste não altera o requisito de um telefone na portaria.

### Sequência de montagem e validação

1. Inserir e nomear equipamentos com identificação correspondente à planta.
2. Cabear e verificar interfaces e alimentação.
3. Configurar VLANs e portas de acesso; configurar trunk onde necessário.
4. Configurar gateway/roteamento e endereçamento.
5. Configurar DHCP, DNS e serviços utilizados no laboratório.
6. Configurar Wi-Fi e associação do cliente.
7. Validar a comunicação permitida antes de aplicar restrições.
8. Aplicar as restrições e repetir testes positivos e negativos.
9. Salvar configurações, salvar o .pkt e reabrir o arquivo para conferir persistência.
10. Capturar evidências e registrar o que cada teste comprova.

### Critérios de aceitação sugeridos — ainda não executados

- Inventário visual: nove pontos de acesso identificados, incluindo quatro câmeras e AP.
- Endereçamento: clientes recebem ou usam IP, máscara, gateway e DNS coerentes.
- Recepção: alcança impressora e serviço corporativo permitido; testar aplicação quando suportada.
- Wi-Fi: cliente associa-se e usa o serviço permitido; não alcança a administração dos ativos.
- Câmeras: cada endereço alcança o destino de vídeo representado; sem afirmar que houve gravação real.
- Catraca: controlador alcança o serviço representado; sem afirmar que a mecânica foi validada.
- Telefonia: registro e chamada com ramal de teste, se incluídos na implementação.
- Segmentação: tentativa autorizada funciona; tentativa proibida falha para o protocolo relevante.
- Diagnóstico: mostrar um fluxo ARP/ICMP e outro DNS/HTTP no modo Simulation, quando disponíveis.
- Persistência: configurações permanecem após reabrir o arquivo.

Ping é evidência de conectividade ICMP. Não é prova suficiente de impressão, áudio, gravação, controle de acesso, vazão ou segurança completa. Packet Tracer utiliza modelos simplificados; cobertura de rádio, autonomia elétrica, certificação de cabos e capacidade real de gravação exigem verificações próprias.

## 8. Levantamentos necessários para fechar materiais e orçamento

### Itens locais

- 1 switch gerenciável, com portas, PoE e uplink especificados.
- 1 AP, incluindo alimentação e montagem.
- 1 rack dimensionado para os equipamentos e manutenção.
- 1 patch panel com capacidade compatível e organizadores.
- 9 terminações de ponto conforme os equipamentos e proteção necessária.
- Cabos Cat 6 medidos por percurso e identificados nas duas pontas.
- Até 18 patch cords no arranjo com patch panel e tomada em cada ponto; ajustar a terminação de câmeras/AP ao sistema efetivamente especificado.
- Eletrodutos/canaletas, caixas, curvas, fixadores e identificação.
- Terminação óptica, cordões e transceptores compatíveis; conferir o que já existe no núcleo.
- Nobreak, distribuição elétrica e proteções pertinentes.
- PC, telefone, impressora, quatro câmeras e catraca/controlador, ou identificação explícita de que serão fornecidos por outro escopo.
- Instalação, configuração, testes/certificação, documentação e eventuais licenças.

O orçamento precisa dizer o que inclui. Não misturar “somente rede” com “portaria completa”, omitindo silenciosamente catraca, câmeras ou computador. Custos compartilhados devem aparecer identificados para evitar cobrança duplicada entre grupos.

### Método de quantificação

Para cada ponto PT-01 a PT-09, registrar origem, destino, trajeto, comprimento horizontal, trechos verticais, folga e total. Somar os comprimentos e acrescentar reserva declarada para aquisição. Diferenciar cabo comprado de cabo instalado e de patch cords.

Para cada produto, registrar marca/modelo, característica necessária, quantidade, preço unitário, subtotal, fornecedor e data da consulta. Adicionar mão de obra e reserva de contingência explicitada. Não há teto de orçamento de rede no enunciado: os R$ 2,5 bilhões são do empreendimento logístico inteiro.

### Vídeo e disponibilidade

A retenção de imagens não foi informada. Exemplo de ordem de grandeza: 4 câmeras a 4 Mb/s contínuos totalizam 16 Mb/s; em 30 dias, cerca de 5,184 TB decimais de dados, antes de margens, RAID e outras despesas de armazenamento. É apenas um cenário: codec, resolução, FPS, bitrate e gravação por evento alteram o resultado.

Definir quem fornece e administra a gravação. Uma câmera com IP não resolve retenção, consulta e armazenamento. Da mesma forma, definir destino das chamadas e comportamento do controlador quando perde conexão com a central.

## 9. Riscos ligados ao negócio

- Falta de energia: afeta recepção, telefonia e monitoramento. Mitigação: alimentação protegida e autonomia definida para equipamentos essenciais.
- Falha do switch ou uplink: pode interromper toda a portaria. Mitigação: procedimentos de contingência, reposição e avaliação do custo de redundância. Um switch com um enlace continua sendo ponto único de falha.
- Chuva, calor, poeira e maresia: podem degradar pontos externos. Mitigação: produtos e instalação adequados ao ambiente, vedação e manutenção. Índice IP isolado não comprova resistência à corrosão salina.
- Acesso indevido: ameaça imagens, controle de entrada e gestão da rede. Mitigação: segmentação, regras de acesso, credenciais próprias e administração restrita.
- Falta de gravação: dificulta consultar ocorrências. Mitigação: definir armazenamento, retenção, monitoramento e responsáveis.
- Interferência/obstáculos no Wi-Fi: reduzem disponibilidade dos clientes. Mitigação: posição planejada e validação de cobertura/capacidade.
- Cabos sem identificação ou trajetos incorretos: aumentam falhas e manutenção. Mitigação: desenho, identificação, organização e testes.
- Premissas não combinadas com a rede central: podem gerar incompatibilidade de IP, VLAN, fibra ou serviços. Mitigação: documentar a interface entre os escopos.

Esses riscos justificam investimento por impacto na operação: filas na entrada, perda de comunicação e indisponibilidade de evidências. Não há dados para afirmar uma probabilidade numérica, SLA específico ou retorno financeiro calculado.

## 10. Metodologia adequada ao trabalho

Usar uma abordagem orientada pelas necessidades da operação: levantamento → requisitos e riscos → desenho lógico → desenho físico → dimensionamento e orçamento → simulação → validação e documentação.

Explicar cada escolha por sua função: PoE simplifica alimentação dos dispositivos compatíveis; VLANs organizam os serviços; políticas de acesso restringem comunicações; fibra integra prédios; organização dos cabos facilita manutenção. O Business Case deve conectar cada gasto ao risco ou requisito que ele atende.

A aula de projeto sustenta cabeamento estruturado, patch panels, backbone, rack, proteção e organização. A aula de topologias diferencia desenhos físicos e lógicos. Fundamentos sustenta convergência de voz, dados e vídeo, segurança, crescimento e disponibilidade. As aulas de protocolos sustentam DHCP, DNS, endereçamento e testes. A UA III oferece o roteiro de explicação do fluxo por camadas.

Na apresentação, acompanhar um caso: a recepcionista acessa o sistema de entrada. O computador precisa de configuração IP, encontra o serviço por DNS quando usa nome, alcança o próximo salto, envia quadros pela LAN e utiliza os protocolos de transporte/aplicação correspondentes. Identificar o papel do switch, gateway e servidor nesse percurso.

Não é necessário implementar todos os protocolos citados nos slides. Correio, FTP e outros serviços só devem entrar se houver requisito. Para explicar TCP/IP, a UA III adota quatro camadas e distingue essa referência da representação didática de cinco camadas.

## 11. Pontos ainda em aberto

1. Divisão de responsabilidades da equipe: quem entrega núcleo, enlace e cada serviço compartilhado. O recorte inicial da dupla na Portaria TP já está esclarecido.
2. Local, interface, VLANs e serviços fornecidos pela rede central definitiva.
3. Distância e trajeto do enlace entre prédios.
4. Usuários Wi-Fi simultâneos e eventual atendimento a visitantes.
5. Modelos definitivos de telefone, câmeras e pacote da catraca na compra.
6. Retenção de imagens, autonomia de energia e comportamento em falhas.
7. Equipamentos já disponíveis que poderão ser retirados do orçamento.

Essas lacunas não impedem o estudo e a preparação da topologia. Devem ficar registradas como premissas até serem confirmadas; não podem ser apresentadas como informações fornecidas pelo professor.

## 12. Fontes e rastreabilidade

Fontes locais, com páginas contadas desde a primeira página do PDF:

- **PROBLEMA 1 [ALUNO] – DESAFIOS PARA CONECTIVIDADE EMPRESARIAL 2026 2.pdf**: p. 3, escopo e Wi-Fi; p. 4, Portaria TP e planta; p. 5, servidores/storage do administrativo; p. 6, entregáveis, equipe e entrega.
- **UA I - Projeto de infraestrutura de redes_compressed.pdf**: p. 3–4, cabeamento estruturado; p. 20 e 27, ambiente/energia; p. 24–25, patch panel/backbone; p. 29–35, rack, cabeamento horizontal e tomadas; p. 38–41, estrela hierárquica.
- **UA I - Topologias, tipos e meios de comunicação_compressed.pdf**: p. 23–27, Wi-Fi; p. 34–39, topologias; p. 44–45, switch/roteador; p. 53–56, documentação física e lógica.
- **UA I - Fundamentos redes de computadores_compressed.pdf**: p. 24, LAN/WAN; p. 37–42, convergência e arquitetura; p. 43–50, disponibilidade, crescimento, QoS e segurança.
- **UA II - Principais Protocolos da Internet.pdf**: p. 7–11, DNS, DHCP e HTTP/HTTPS.
- **UA II - Protocolos e modelos.pdf**: p. 4–9, IP, gateway e diagnóstico; p. 29–32, TCP/IP.
- **UA III - Modelos em Camadas OSI e TCP 2026.2.pdf**: p. 8–19, responsabilidades; p. 21–24, TCP/IP e serviços; p. 25–34, encapsulamento e fluxo de comunicação.

Conferências técnicas complementares, revisadas em 16/09/2026:

- [Cisco — Introdução ao Packet Tracer](https://tutorials.ptnetacad.net/help/default/intro.htm): modelos de simulação simplificados.
- [Cisco — Roteamento entre VLANs](https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/41260-189.html): comunicação entre VLANs e restrições por listas de acesso.
- [Cisco — Catalyst 1200, ficha técnica](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-1200-series-switches/nb-06-cat1200-ser-data-sheet-cte-en.html): distinção entre capacidades de porta PoE e orçamento total. Consulta técnica, sem seleção definitiva de produto.

Os textos extraídos e imagens das páginas do enunciado estão nesta mesma pasta para consulta. Os PDFs originais permanecem na pasta informada pelo aluno.
