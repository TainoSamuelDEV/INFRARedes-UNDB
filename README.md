# Projeto de Infraestrutura de Redes — Terminal Portuário do Itaqui
### Centro Universitário UNDB • Engenharia de Software / Ciência da Computação
**Disciplina:** Infraestrutura de Redes (2026.2)  
**Professor:** Me. Arlley Costa  
**Metodologia:** Aprendizagem Baseada em Problemas (PBL — Problema 1: Desafios para Conectividade Empresarial)  
**Data da Entrega:** 17 de Setembro de 2026  

---

## 👥 Equipes & Integrantes (Divisão por Áreas Operacionais)

O projeto de infraestrutura de redes do Terminal Portuário Ponta da Madeira / Itaqui foi executado de forma integrada por 5 equipes setoriais, consolidando a infraestrutura de dados de um complexo de **125.340 m²** e **104 ativos de rede**:

| Setor Operacional | Integrantes Responsáveis | Escopo Técnico Principal |
| :--- | :--- | :--- |
| **01. Prédio Administrativo (CPD Central)** | Gabriel Ordonez & Higor Gabriel | Hub central de telecomunicações, sala climatizada de CPD (42U), 3 Servidores (ERP, AD/DNS, Backup), Storage SAN 10 Gb/s, 3 switches 48p PoE+, Wi-Fi 6 e 108 pontos Cat6. |
| **02. Portaria TP** | Taino Samuel & Victor Cabral | Triagem perimetral, pesagem de carretas, 4 câmeras LPR Full HD (leitura de placas), catraca biométrica IP, switch 16p PoE+ e AP externo isolado para motoristas. |
| **03. Silo de Grãos** | Asafe & Lucas | Área industrial classificada (Zona Ex), switch industrial ruggedized NEMA 4X / IP67, 5 câmeras antideflagrantes, sensores IoT (temperatura de grãos e gás) e telemetria Modbus-TCP. |
| **04. Pera Ferroviária** | João Lucas & Jaylon Coelho | Circuito de 600m de trilhos, 2 switches industriais IP67 com coxins antivibração, 10 câmeras OCR de leitura de vagões, 2 balanças dinâmicas de pesagem de eixos (WIM) e latência < 10 ms. |
| **05. Berço 098 / CCO** | Mateus Dantas & Renan Pires | Centro de Controle Operacional náutico e cais, NVR corporativo 32 canais (64 TB RAID 5), 4 câmeras PTZ 40x de atracação, 5 telefones IP de despacho e enlace óptico direto ao CPD. |

---

## 🎯 Entregáveis Oficiais do Projeto

Todos os produtos exigidos no edital estão consolidados e prontos para consulta:

| Artefato de Entrega | Descrição do Documento | Formato / Link Direto |
| :--- | :--- | :--- |
| 📊 **Apresentação Executiva Oficial** | **Apresentação em 11 slides widescreen 16:9** contendo contexto portuário, prevenção de demurrage, orçamento geral, topologia estrela centralizada no CPD e as **plantas e diagramas reais de cada dupla**. | [`Projeto-de-Infraestrutura-de-Redes-Apresentacao.pdf`](Projeto-de-Infraestrutura-de-Redes-Apresentacao.pdf) |
| 🧪 **Laboratório Master Consolidado** | **Arquivo mestre do Cisco Packet Tracer** com todos os 104 ativos interligados, roteamento inter-VLAN validado, superbloco `10.100.0.0/16` sem sobreposições e testes de ping 100% funcionais. | [`Terminal-Portuario-Geral.pkt`](Terminal-Portuario-Geral.pkt) |
| 📋 **Guia de Avaliação do Professor** | Roteiro prático com checklist do edital e comandos de teste de conectividade e segurança no Packet Tracer. | [`GUIA-DE-AVALIACAO-PROFESSOR.md`](GUIA-DE-AVALIACAO-PROFESSOR.md) |
| 📦 **Pacote Compactado de Entrega** | Arquivo compactado contendo todos os entregáveis finais para download direto. | [`ENTREGA-PROJETO-TERMINAL-PORTUARIO-UNDB.zip`](ENTREGA-PROJETO-TERMINAL-PORTUARIO-UNDB.zip) |

---

## 📋 Matriz de Conformidade com o Edital (100% dos Requisitos Atendidos)

| Requisito do Edital (Página 6) | Como Foi Atendido no Projeto | Artefato Comprobatório |
| :--- | :--- | :--- |
| **1. Metodologia Aplicada** | Abordagem Top-Down estruturada em 4 etapas (Levantamento de Requisitos ➔ Análise de Riscos ➔ Topologias Física/Lógica ➔ Orçamento e Simulação). | Slides 1 e 4 da Apresentação + Relatórios Setoriais |
| **2. Requisitos e Riscos / Business Case** | Business Case com justificativa econômica: calado natural de 23m, safra MATOPI (3,7 mi ton/mês) e prevenção de multas marítimas de *demurrage* (US$ 50k a 80k/dia). Matriz de riscos ambientais (maresia, EMI, atmosfera explosiva e poeira). | Slides 2 e 3 da Apresentação |
| **3. Orçamento por Ordem de Grandeza (BOM)** | Orçamento consolidado com pesquisa de mercado de setembro de 2026, marcas homologadas (Cisco, Furukawa, Dell, APC), subtotal de R$ 904.034,14 + Reserva Técnica de 20% (R$ 180.806,83) = **R$ 1.084.840,97**. | Slide 3 da Apresentação |
| **4. As-Built / Infraestrutura de Cabeamento** | Metragens de cabos Cat6 100% cobre (~4.800m totais), backbone de fibra óptica monomodo OS2 (~2.220m), identificação de pontos norma ANSI/TIA-606 e armários IP66/IP67. | Slide 4 da Apresentação + Pastas Setoriais |
| **5. Topologia Física dos Ativos** | Diagrama vetorial em estrela centralizado no CPD do Prédio Administrativo + plantas e topologias físicas individualizadas de cada dupla. | Slides 4 a 9 da Apresentação |
| **6. Topologia Lógica dos Ativos** | Superbloco `10.100.0.0/16`, 8 VLANs segmentadas, Trunks 802.1Q, priorização QoS para Voz e Telemetria, DHCP pools e ACLs de segurança Zero Trust. | Slide 10 da Apresentação + `Terminal-Portuario-Geral.pkt` |

---

## 🌐 Arquitetura Lógica & Endereçamento IP Consolidado

O projeto unificou o plano de endereçamento, sanando os conflitos originais e estabelecendo um superbloco estanque:

| VLAN ID | Nome do Segmento | Sub-rede IPv4 | Gateway (SVI) | Dispositivos Atendidos | Políticas / QoS |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **10** | **Dados Corporativos** | `10.100.10.0/24` | `10.100.10.1` | PCs, impressoras e estações de trabalho | Best-effort, acesso ao ERP |
| **20** | **Voz / Telefonia IP** | `10.100.20.0/24` | `10.100.20.1` | Telefones IP (CCO, Inspetoria, Adm) | **QoS Estrito (CoS 5 / DSCP EF)** |
| **30** | **CFTV / Videomonitoramento** | `10.100.30.0/24` | `10.100.30.1` | 28 Câmeras IP, NVR Central 32ch, LPR e OCR | Tráfego isolado, sem rota Internet |
| **40** | **Controle de Acesso** | `10.100.40.0/24` | `10.100.40.1` | Catracas biométricas e RFID da Portaria | Restrito à base de credenciais |
| **50** | **Wi-Fi Corporativo** | `10.100.50.0/24` | `10.100.50.1` | Notebooks corporativos e tablets de campo | Autenticação WPA3 / 802.1X |
| **60** | **Wi-Fi Visitantes** | `10.100.60.0/24` | `10.100.60.1` | Motoristas de caminhões na Portaria | **Isolamento perimetral total** |
| **70** | **IoT / Automação Industrial** | `10.100.70.0/24` | `10.100.70.1` | Sensores de silos e balanças ferroviárias | **Prioridade de alarme Modbus-TCP** |
| **99** | **Gerência de Rede** | `10.100.99.0/24` | `10.100.99.1` | Interfaces de gerência de switches e roteadores | Acesso restrito via SSH v2 / TI |

---

## 💰 Resumo Financeiro Consolidado (BOM)

| Área / Setor Operacional | Investimento Direto (R$) | Participação (%) | Justificativa Técnica |
| :--- | :---: | :---: | :--- |
| **Prédio Administrativo (CPD Central)** | R$ 708.624,00 | 78,4% | CPD climatizado 42U, 3 Servidores PowerEdge, Storage SAN, 3 switches 48p PoE+, 4 APs e 108 pontos. |
| **Pera Ferroviária** | R$ 125.144,00 | 13,8% | 600m de fibra OS2, 2 switches industriais IP67 antivibração, 10 câmeras OCR e 2 balanças dinâmicas. |
| **Portaria TP** | R$ 32.981,83 | 3,6% | Switch 16p PoE+, 4 câmeras LPR para placas de caminhões, catraca biométrica e enlace de fibra 450m. |
| **Berço 098 / CCO** | R$ 18.891,32 | 2,1% | Switch 24p PoE+, NVR 32 canais (64 TB RAID 5), 4 câmeras PTZ 40x de cais e 5 telefones IP de despacho. |
| **Silo de Grãos** | R$ 18.392,99 | 2,0% | Switch industrial ruggedized NEMA 4X / IP67, 5 câmeras antideflagrantes e sensores IoT de temperatura e gás. |
| **Subtotal Direto em Ativos e Passivos** | **R$ 904.034,14** | **100,0%** | Orçamento base levantado junto a distribuidores autorizados Cisco/Furukawa. |
| **Reserva Técnica de Contingência (20%)** | **R$ 180.806,83** | — | Provisão para variações cambiais, insumos de campo, ancoragens e certificações Fluke. |
| **VALOR TOTAL GLOBAL CONSOLIDADO** | **R$ 1.084.840,97** | — | **0,043% do valor global de Capex do Terminal Portuário (R$ 2,5 Bilhões).** |

---

## 🧪 Como Executar a Simulação no Cisco Packet Tracer

1. Abra o arquivo mestre: [`Terminal-Portuario-Geral.pkt`](Terminal-Portuario-Geral.pkt).
2. Aguarde a convergência do Spanning Tree (STP).
3. **Testes de Validação:**
   - No PC da Diretoria (`10.100.10.x`), execute `ping 10.100.10.1` (Gateway local).
   - Teste a comunicação inter-setorial com a Portaria: `ping 10.100.40.10` (Catraca da Portaria).
   - Teste a telemetria com a Pera Ferroviária: `ping 10.100.72.10` (Balança Ferroviária).
   - Verifique o isolamento de segurança: computadores na VLAN 60 (Visitantes) não conseguem acessar as redes corporativas.

---

## 📁 Estrutura de Diretórios do Repositório

```text
INFRARedes-UNDB/
│
├── README.md                                           # Apresentação executiva do repositório
├── GUIA-DE-AVALIACAO-PROFESSOR.md                     # Guia passo a passo de homologação e notas técnicas
├── Projeto-de-Infraestrutura-de-Redes-Apresentacao.pdf # APRESENTAÇÃO OFICIAL EM PDF (11 Slides 16:9)
├── Terminal-Portuario-Geral.pkt                        # LABORATÓRIO MASTER UNIFICADO (Packet Tracer)
├── ENTREGA-PROJETO-TERMINAL-PORTUARIO-UNDB.zip        # PACOTE COMPACTADO PARA DOWNLOAD
│
├── Predio-Administrativo(Gabriel Ordonez e Higor Gabriel)/
│   ├── 01-Relatorio/                                  # Relatório técnico em .docx
│   └── 03-Packet-Tracer/                              # Arquivos de simulação do setor
│
├── Portaria-TP(Taino Samuel e Victor Cabral)/
│   ├── 01-Relatorio/                                  # Relatório técnico (.docx e .pdf)
│   ├── 02-Plantas/                                    # Plantas de encaminhamento e topologias (.png e .pdf)
│   └── 03-Packet-Tracer/                              # Simulação do setor
│
├── Silo-Grãos(Asafe e Lucas)/
│   ├── Projeto de Rede do Silo de Grãos.pdf           # Relatório técnico e plantas
│   └── Simulação Packet Tracer/                       # Simulação do setor
│
├── Pera-Ferroviaria(João Lucas e Jaylon Coelho)/
│   ├── Relatório Geral - Pera Ferroviária.pdf         # Relatório técnico completo
│   ├── Relatório Geral - Pera Ferroviária.docx        # Fonte do relatório
│   └── Simulação Packet Tracer/                       # Simulação do setor
│
└── Predio-Inspetoria(Mateus Dantas e Renan Pires)/
    ├── relatorioinspetoriaberco098.pdf                # Relatório técnico e planta
    └── Simulação Packet Tracer/                       # Simulação do setor
```

---

<div align="center">
  <sub>Projeto de Infraestrutura de Redes • Terminal Portuário do Itaqui • UNDB São Luís - MA • 2026.2</sub>
</div>
