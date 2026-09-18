# GUIA DE AVALIAÇÃO DO PROJETO — PROFESSOR ME. ARLLEY COSTA
### PBL: Desafios para Conectividade Empresarial 2026.2 • UNDB

Prezado Professor Arlley Costa,

Este guia tem como objetivo facilitar a sua avaliação dos produtos entregues pelo conjunto de equipes para a infraestrutura de redes do **Terminal Portuário do Itaqui / Ponta da Madeira**.

---

## 📌 Checklist de Verificação dos 6 Itens do Edital

| Item Obrigatório (Edital Pág. 6) | Onde Verificar no Repositório | Status da Homologação |
| :--- | :--- | :---: |
| **1. Metodologia Aplicada** | `Projeto-de-Infraestrutura-de-Redes-Apresentacao.pdf` (Slide 1 e Slide 4) | **Conforme** |
| **2. Requisitos e Riscos / Business Case** | `Projeto-de-Infraestrutura-de-Redes-Apresentacao.pdf` (Slide 2: Calado, MATOPI, Demurrage) | **Conforme** |
| **3. Orçamento por Ordem de Grandeza** | `Projeto-de-Infraestrutura-de-Redes-Apresentacao.pdf` (Slide 3: R$ 1.084.840,97) | **Conforme** |
| **4. As-Built e Infraestrutura Passiva** | `Projeto-de-Infraestrutura-de-Redes-Apresentacao.pdf` (Slide 4 e pastas setoriais) | **Conforme** |
| **5. Topologia Física dos Ativos** | `Projeto-de-Infraestrutura-de-Redes-Apresentacao.pdf` (Slides 4 a 9 com as plantas das duplas) | **Conforme** |
| **6. Topologia Lógica e VLANs** | `Projeto-de-Infraestrutura-de-Redes-Apresentacao.pdf` (Slide 10) e `Terminal-Portuario-Geral.pkt` | **Conforme** |

---

## 🚀 Roteiro de Testes Rápidos no Cisco Packet Tracer

Para validar a interoperabilidade entre as 5 áreas operacionais:

1. **Abra o arquivo:** `Terminal-Portuario-Geral.pkt`.
2. **Pressione:** `Fast Forward Time` (Alt + D) duas vezes para acelerar a convergência do Spanning Tree (STP).
3. **Teste 1 — Roteamento Inter-VLAN no Prédio Administrativo:**
   - Abra o terminal do `PC-Diretoria` (VLAN 10: `10.100.10.15`).
   - Ping para o servidor de ERP (VLAN 10): `ping 10.100.10.10` ➔ **Sucesso (0% loss)**.
   - Ping para o telefone IP da recepção (VLAN 20): `ping 10.100.20.10` ➔ **Sucesso (0% loss)**.
4. **Teste 2 — Integração do Campus com Setores Remotos:**
   - No `PC-Diretoria`, execute o ping para a catraca da Portaria: `ping 10.100.40.10` ➔ **Sucesso**.
   - Ping para o sensor de temperatura do Silo de Grãos: `ping 10.100.70.10` ➔ **Sucesso**.
   - Ping para a balança dinâmica da Pera Ferroviária: `ping 10.100.72.10` ➔ **Sucesso**.
5. **Teste 3 — Políticas de Segurança e Isolamento (Zero Trust):**
   - No `Laptop-Visitante` da Portaria (VLAN 60: `10.100.60.25`), tente pingar o servidor interno: `ping 10.100.10.10` ➔ **Destino Inalcançável / Timeout (Bloqueio por ACL validado)**.

---

## 📊 Síntese dos Indicadores Globais do Projeto

- **Áreas Operacionais Integradas:** 5 Áreas (Prédio Adm, Portaria TP, Silo de Grãos, Pera Ferroviária, Berço 098/CCO).
- **Total de Dispositivos Conectados:** 104 Ativos.
- **Câmeras IP em Operação:** 28 Câmeras (CFTV, LPR e OCR).
- **Segmentos Lógicos:** 8 VLANs ativas (Superbloco `10.100.0.0/16`).
- **Extensão de Fibra Óptica Monomodo OS2:** ~2.220 Metros de canalização subterrânea.
- **Orçamento Consolidado:** R$ 1.084.840,97 (R$ 904.034,14 em ativos + R$ 180.806,83 de reserva técnica de 20%).

Agradecemos a condução da disciplina e nos colocamos à disposição durante a apresentação em sala!
