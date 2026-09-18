"""
Gerador de Apresentação Executiva Ultra Resumida com Imagens Reais das Duplas
Estilo Gamma 16:9 (900pt x 507.12pt)
Arquitetura Estrela Centralizada no Prédio Administrativo (CPD Central)
Projeto de Infraestrutura de Redes - Terminal Portuário do Itaqui - UNDB 2026.2
"""
import os
import base64
import subprocess
import pypdfium2 as pdfium

HTML_FILE = os.path.abspath("auditoria-tools/apresentacao_resumo_source.html")
PDF_OUTPUT = os.path.abspath("Projeto-de-Infraestrutura-de-Redes-Apresentacao.pdf")

def to_base64(rel_path):
    full_path = os.path.abspath(rel_path)
    if os.path.exists(full_path):
        with open(full_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            ext = os.path.splitext(full_path)[1].lower().replace(".", "")
            if ext == "jpg": ext = "jpeg"
            return f"data:image/{ext};base64,{encoded}"
    return ""

img_adm = to_base64("auditoria-tools/imagens_duplas/adm_img_3.png")
img_portaria = to_base64("Portaria-TP(Taino Samuel e Victor Cabral)/02-Plantas/02-Topologia-fisica.png")
img_silo = to_base64("auditoria-tools/imagens_duplas/silo_diagrama_fisico.png")
img_pera = to_base64("auditoria-tools/imagens_duplas/pera_docx_img_1.png")
img_inspetoria = to_base64("auditoria-tools/imagens_duplas/inspetoria_diagrama_fisico.png")

html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Projeto de Infraestrutura de Redes - Terminal Portuário do Itaqui</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<style>
  @page {{
    size: 900pt 507.12pt;
    margin: 0;
  }}
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }}
  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background-color: #f1f5f9;
    color: #0f172a;
  }}
  .slide {{
    width: 900pt;
    height: 507.12pt;
    page-break-after: always;
    page-break-inside: avoid;
    background-color: #ffffff;
    position: relative;
    overflow: hidden;
    padding: 34pt 48pt 30pt 48pt;
    display: flex;
    flex-direction: column;
  }}
  .slide-cover {{
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 40pt 60pt;
  }}

  /* Badges & Titles */
  .badge {{
    display: inline-block;
    align-self: flex-start;
    background: #f1f5f9;
    color: #475569;
    font-size: 8pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    padding: 3pt 8pt;
    border-radius: 4pt;
    border: 1px solid #e2e8f0;
    margin-bottom: 4pt;
  }}
  .badge-blue {{ background: #e0f2fe; color: #0369a1; border-color: #bae6fd; }}
  .badge-green {{ background: #dcfce7; color: #15803d; border-color: #bbf7d0; }}
  .badge-amber {{ background: #fef3c7; color: #b45309; border-color: #fde68a; }}
  .badge-purple {{ background: #f3e8ff; color: #7e22ce; border-color: #e9d5ff; }}

  .slide-title {{
    font-size: 22pt;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.4px;
    line-height: 1.15;
    margin-bottom: 3pt;
  }}
  .slide-subtitle {{
    font-size: 9.5pt;
    color: #64748b;
    margin-bottom: 12pt;
    line-height: 1.35;
  }}

  /* Layout Grids */
  .grid-2 {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14pt;
    flex: 1;
  }}
  .grid-sector {{
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: 14pt;
    flex: 1;
    min-height: 0;
  }}
  .grid-4 {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10pt;
    flex: 1;
  }}

  /* Cards */
  .card {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8pt;
    padding: 10pt 13pt;
    display: flex;
    flex-direction: column;
  }}
  .card-white {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8pt;
    padding: 8pt 10pt;
  }}
  .card-header {{
    font-size: 10pt;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 5pt;
    display: flex;
    align-items: center;
    gap: 5pt;
  }}

  /* Image Containers */
  .img-frame {{
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 8pt;
    padding: 6pt;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    overflow: hidden;
  }}
  .img-frame img {{
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
    border-radius: 4pt;
  }}

  /* Bullet points */
  .bullet-list {{
    list-style: none;
    font-size: 8pt;
    color: #334155;
  }}
  .bullet-list li {{
    position: relative;
    padding-left: 10pt;
    margin-bottom: 4pt;
    line-height: 1.35;
  }}
  .bullet-list li::before {{
    content: "•";
    position: absolute;
    left: 1pt;
    color: #0284c7;
    font-weight: bold;
    font-size: 9pt;
  }}

  /* Pills & Tables */
  .pill {{
    display: inline-block;
    padding: 2pt 5pt;
    border-radius: 3pt;
    font-size: 7pt;
    font-weight: 700;
    font-family: 'JetBrains Mono', monospace;
  }}
  .pill-blue {{ background: #e0f2fe; color: #0369a1; }}
  .pill-green {{ background: #dcfce7; color: #15803d; }}
  .pill-purple {{ background: #f3e8ff; color: #7e22ce; }}
  .pill-amber {{ background: #fef3c7; color: #b45309; }}
  .pill-slate {{ background: #e2e8f0; color: #334155; }}

  .table-compact {{
    width: 100%;
    border-collapse: collapse;
    font-size: 7.5pt;
  }}
  .table-compact th {{
    text-align: left;
    color: #0f172a;
    font-weight: 700;
    padding: 4pt 6pt;
    border-bottom: 2px solid #e2e8f0;
    background: #f8fafc;
  }}
  .table-compact td {{
    padding: 4pt 6pt;
    border-bottom: 1px solid #f1f5f9;
    color: #334155;
  }}
  .table-compact tr:last-child td {{
    border-bottom: none;
  }}

  /* Footer */
  .slide-footer {{
    position: absolute;
    bottom: 10pt;
    left: 48pt;
    right: 48pt;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 7.5pt;
    color: #94a3b8;
    border-top: 1px solid #f1f5f9;
    padding-top: 4pt;
  }}
  .slide-footer-brand {{
    font-weight: 600;
    color: #64748b;
  }}
</style>
</head>
<body>

<!-- ==========================================
     SLIDE 1: CAPA OFICIAL
     ========================================== -->
<div class="slide slide-cover">
  <div style="font-size: 34pt; font-weight: 800; color: #0f172a; letter-spacing: -0.8px; margin-bottom: 6pt;">
    Projeto de Infraestrutura de Redes
  </div>
  <div style="font-size: 24pt; font-weight: 700; color: #0284c7; margin-bottom: 20pt;">
    Terminal Portuário do Itaqui
  </div>
  
  <div style="font-size: 11pt; font-weight: 600; color: #0f172a; margin-bottom: 3pt;">
    PBL — Infraestrutura de Redes | UNDB
  </div>
  <div style="font-size: 9pt; color: #64748b; margin-bottom: 28pt;">
    São Luís — MA | 2026.2 • Prof. Arlley Costa
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14pt; width: 100%; max-width: 760pt; text-align: left;">
    <div class="card" style="background: #f1f5f9; padding: 14pt 16pt;">
      <div style="font-size: 14pt; font-weight: 800; color: #0f172a; margin-bottom: 3pt;">5 Áreas Integradas</div>
      <div style="font-size: 8.5pt; color: #475569;">
        Backbone em estrela ancorado no CPD do Prédio Administrativo.
      </div>
    </div>
    
    <div class="card" style="background: #f1f5f9; padding: 14pt 16pt;">
      <div style="font-size: 14pt; font-weight: 800; color: #0f172a; margin-bottom: 3pt;">Topologias Reais</div>
      <div style="font-size: 8.5pt; color: #475569;">
        Plantas e esquemas de rede desenvolvidos pelas duplas de engenharia.
      </div>
    </div>

    <div class="card" style="background: #f1f5f9; padding: 14pt 16pt;">
      <div style="font-size: 14pt; font-weight: 800; color: #0f172a; margin-bottom: 3pt;">R$ 1.084.840,97</div>
      <div style="font-size: 8.5pt; color: #475569;">
        Orçamento total consolidado (com 20% de reserva técnica de contingência).
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span class="slide-footer-brand">PBL Infraestrutura de Redes • UNDB 4.0</span>
    <span>Apresentação Executiva Síntese</span>
  </div>
</div>

<!-- ==========================================
     SLIDE 2: CONTEXTO ESTRATÉGICO
     ========================================== -->
<div class="slide">
  <div class="badge badge-blue">CONTEXTO ESTRATÉGICO</div>
  <div class="slide-title">Contexto Portuário & Missão Crítica</div>
  <div class="slide-subtitle">
    O complexo do Itaqui escoa a safra de grãos do Arco Norte. A rede de dados é a espinha dorsal de sistemas operacionais de missão zero downtime (99,999%).
  </div>

  <div class="grid-4" style="margin-bottom: 10pt;">
    <div class="card">
      <div class="card-header" style="color: #0284c7;">
        <span>🌊</span> Calado de 23m
      </div>
      <ul class="bullet-list">
        <li>Atracação de graneleiros <strong>Panamax</strong> e <strong>Capesize</strong>.</li>
        <li>Marés de até 7m exigem monitoramento contínuo no píer.</li>
      </ul>
    </div>

    <div class="card">
      <div class="card-header" style="color: #15803d;">
        <span>🌾</span> Safra MATOPI
      </div>
      <ul class="bullet-list">
        <li><strong>3,7 milhões de ton/mês</strong> de grãos escoados.</li>
        <li>Integração rodoferroviária contínua 24/7/365.</li>
      </ul>
    </div>

    <div class="card">
      <div class="card-header" style="color: #b45309;">
        <span>⏱️</span> Demurrage Zero
      </div>
      <ul class="bullet-list">
        <li>Multa de <strong>US$ 50k a 80k/dia</strong> por navio retido.</li>
        <li>Falhas de rede paralisam balanças, OCR e despacho.</li>
      </ul>
    </div>

    <div class="card">
      <div class="card-header" style="color: #7e22ce;">
        <span>🏢</span> Núcleo Central (CPD)
      </div>
      <ul class="bullet-list">
        <li>CPD principal instalado no <strong>Prédio Administrativo</strong>.</li>
        <li>Servidores de ERP, Storage SAN e Gateway central.</li>
      </ul>
    </div>
  </div>

  <div class="card" style="background: #f8fafc; padding: 8pt 14pt;">
    <div style="font-size: 8pt; font-weight: 700; color: #0f172a; margin-bottom: 2pt;">Espinha Dorsal da Solução:</div>
    <div style="font-size: 7.5pt; color: #475569;">
      Backbone em estrela com Fibra Monomodo OS2 saindo do CPD do Administrativo • Switches PoE+ com redundância • 8 VLANs isoladas com ACLs • Cabeamento Cat6 100% Cobre • Nobreaks senoidais em todos os racks remotos.
    </div>
  </div>

  <div class="slide-footer">
    <span class="slide-footer-brand">Terminal Portuário do Itaqui • Contexto</span>
    <span>Slide 2</span>
  </div>
</div>

<!-- ==========================================
     SLIDE 3: ORÇAMENTO POR ORDEM DE GRANDEZA
     ========================================== -->
<div class="slide">
  <div class="badge">ORÇAMENTO GERAL</div>
  <div class="slide-title">Orçamento por Ordem de Grandeza</div>
  <div class="slide-subtitle">
    Consolidação financeira das 5 áreas operacionais (pesquisa de mercado de setembro de 2026). O Prédio Administrativo concentra 78,4% dos investimentos devido ao CPD central e servidores.
  </div>

  <div class="grid-2">
    <!-- Gráfico Visual de Barras -->
    <div class="card" style="justify-content: center; gap: 10pt;">
      <div class="card-header" style="margin-bottom: 2pt;">Distribuição por Área (R$)</div>
      
      <div>
        <div style="display: flex; justify-content: space-between; font-size: 8pt; font-weight: 600; margin-bottom: 2pt;">
          <span>Prédio Administrativo (CPD Central)</span>
          <span>R$ 708.624,00 (78,4%)</span>
        </div>
        <div style="background: #e2e8f0; height: 16pt; border-radius: 4pt; overflow: hidden;">
          <div style="background: #334155; width: 78.4%; height: 100%; display: flex; align-items: center; justify-content: flex-end; padding-right: 6pt; color: #fff; font-size: 7.5pt; font-weight: 700;">709k</div>
        </div>
      </div>

      <div>
        <div style="display: flex; justify-content: space-between; font-size: 8pt; font-weight: 600; margin-bottom: 2pt;">
          <span>Pera Ferroviária</span>
          <span>R$ 125.144,00 (13,8%)</span>
        </div>
        <div style="background: #e2e8f0; height: 16pt; border-radius: 4pt; overflow: hidden;">
          <div style="background: #475569; width: 13.8%; height: 100%; display: flex; align-items: center; justify-content: flex-end; padding-right: 4pt; color: #fff; font-size: 7.5pt; font-weight: 700;">125k</div>
        </div>
      </div>

      <div>
        <div style="display: flex; justify-content: space-between; font-size: 8pt; font-weight: 600; margin-bottom: 2pt;">
          <span>Portaria TP</span>
          <span>R$ 32.981,83 (3,6%)</span>
        </div>
        <div style="background: #e2e8f0; height: 16pt; border-radius: 4pt; overflow: hidden;">
          <div style="background: #64748b; width: 6.5%; height: 100%;"></div>
        </div>
      </div>

      <div>
        <div style="display: flex; justify-content: space-between; font-size: 8pt; font-weight: 600; margin-bottom: 2pt;">
          <span>Berço 098 / CCO</span>
          <span>R$ 18.891,32 (2,1%)</span>
        </div>
        <div style="background: #e2e8f0; height: 16pt; border-radius: 4pt; overflow: hidden;">
          <div style="background: #64748b; width: 4.5%; height: 100%;"></div>
        </div>
      </div>

      <div>
        <div style="display: flex; justify-content: space-between; font-size: 8pt; font-weight: 600; margin-bottom: 2pt;">
          <span>Silo de Grãos</span>
          <span>R$ 18.392,99 (2,0%)</span>
        </div>
        <div style="background: #e2e8f0; height: 16pt; border-radius: 4pt; overflow: hidden;">
          <div style="background: #64748b; width: 4.4%; height: 100%;"></div>
        </div>
      </div>
    </div>

    <!-- Tabela Sintética -->
    <div style="display: flex; flex-direction: column; gap: 8pt;">
      <div class="card">
        <div class="card-header" style="margin-bottom: 4pt;">Composição Financeira</div>
        <table class="table-compact">
          <thead>
            <tr><th>Área / Setor</th><th style="text-align: right;">Valor Direto</th></tr>
          </thead>
          <tbody>
            <tr><td>Prédio Administrativo (CPD Central)</td><td style="text-align: right; font-family: 'JetBrains Mono'; font-weight: 600;">R$ 708.624,00</td></tr>
            <tr><td>Pera Ferroviária</td><td style="text-align: right; font-family: 'JetBrains Mono'; font-weight: 600;">R$ 125.144,00</td></tr>
            <tr><td>Portaria TP</td><td style="text-align: right; font-family: 'JetBrains Mono'; font-weight: 600;">R$ 32.981,83</td></tr>
            <tr><td>Berço 098 / CCO</td><td style="text-align: right; font-family: 'JetBrains Mono'; font-weight: 600;">R$ 18.891,32</td></tr>
            <tr><td>Silo de Grãos</td><td style="text-align: right; font-family: 'JetBrains Mono'; font-weight: 600;">R$ 18.392,99</td></tr>
            <tr style="background: #f1f5f9; font-weight: 700;"><td>Subtotal Direto</td><td style="text-align: right; font-family: 'JetBrains Mono';">R$ 904.034,14</td></tr>
            <tr><td>Reserva Técnica (20%)</td><td style="text-align: right; font-family: 'JetBrains Mono';">R$ 180.806,83</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card" style="background: #f1f5f9; border: 1px solid #cbd5e1; padding: 10pt 14pt;">
        <div style="font-size: 7.5pt; font-weight: 700; color: #64748b; text-transform: uppercase;">TOTAL GERAL CONSOLIDADO</div>
        <div style="font-size: 20pt; font-weight: 800; color: #0f172a; font-family: 'JetBrains Mono'; margin-top: 2pt;">
          R$ 1.084.840,97
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span class="slide-footer-brand">Terminal Portuário do Itaqui • Orçamento Geral</span>
    <span>Slide 3</span>
  </div>
</div>

<!-- ==========================================
     SLIDE 4: TOPOLOGIA GERAL DE CAMPUS (CENTRALIZADA NO ADM)
     ========================================== -->
<div class="slide">
  <div class="badge">BACKBONE ÓPTICO</div>
  <div class="slide-title">Topologia Física Geral de Campus (Estrela)</div>
  <div class="slide-subtitle">
    Arquitetura em estrela centralizada no CPD do Prédio Administrativo (MDF Central). Enlaces ponto-a-ponto de fibra monomodo OS2 conectam todas as áreas operacionais com imunidade eletromagnética.
  </div>

  <div class="grid-2">
    <!-- SVG Vector Topology - ADM NO CENTRO -->
    <div class="card" style="padding: 6pt; background: #ffffff;">
      <div style="height: 195pt; display: flex; align-items: center; justify-content: center;">
        <svg viewBox="0 0 460 250" style="width: 100%; height: 100%;">
          <!-- Enlaces de fibra pontilhada azul convergindo ao ADM -->
          <line x1="230" y1="125" x2="65" y2="45" stroke="#0284c7" stroke-width="2.5" stroke-dasharray="4,3" />
          <line x1="230" y1="125" x2="395" y2="45" stroke="#0284c7" stroke-width="2.5" stroke-dasharray="4,3" />
          <line x1="230" y1="125" x2="65" y2="205" stroke="#0284c7" stroke-width="2.5" stroke-dasharray="4,3" />
          <line x1="230" y1="125" x2="395" y2="205" stroke="#0284c7" stroke-width="2.5" stroke-dasharray="4,3" />

          <!-- Distâncias -->
          <rect x="110" y="65" width="60" height="15" rx="4" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
          <text x="140" y="76" font-size="7.5" fill="#0369a1" font-weight="bold" text-anchor="middle">SMF 450m</text>

          <rect x="290" y="65" width="60" height="15" rx="4" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
          <text x="320" y="76" font-size="7.5" fill="#0369a1" font-weight="bold" text-anchor="middle">SMF 850m</text>

          <rect x="110" y="165" width="60" height="15" rx="4" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
          <text x="140" y="176" font-size="7.5" fill="#0369a1" font-weight="bold" text-anchor="middle">SMF 600m</text>

          <rect x="290" y="165" width="60" height="15" rx="4" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
          <text x="320" y="176" font-size="7.5" fill="#0369a1" font-weight="bold" text-anchor="middle">SMF 320m</text>

          <!-- NÓ CENTRAL: PRÉDIO ADMINISTRATIVO (CPD CENTRAL) -->
          <rect x="155" y="96" width="150" height="58" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="2" />
          <text x="230" y="117" font-size="9" fill="#ffffff" font-weight="bold" text-anchor="middle">PRÉDIO ADMINISTRATIVO</text>
          <text x="230" y="131" font-size="8" fill="#38bdf8" font-weight="bold" text-anchor="middle">CPD Central / Datacenter</text>
          <text x="230" y="144" font-size="6.5" fill="#94a3b8" text-anchor="middle">Servidores • Storage • Gateway</text>

          <!-- Node: Portaria TP -->
          <rect x="10" y="22" width="110" height="46" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5" />
          <text x="65" y="42" font-size="8.5" fill="#0f172a" font-weight="bold" text-anchor="middle">PORTARIA TP</text>
          <text x="65" y="56" font-size="7" fill="#64748b" text-anchor="middle">Switch 16p • LPR / Catracas</text>

          <!-- Node: Silo de Grãos -->
          <rect x="340" y="22" width="110" height="46" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5" />
          <text x="395" y="42" font-size="8.5" fill="#0f172a" font-weight="bold" text-anchor="middle">SILO DE GRÃOS</text>
          <text x="395" y="56" font-size="7" fill="#64748b" text-anchor="middle">Switch 24p • Sensores IoT</text>

          <!-- Node: Pera Ferroviária -->
          <rect x="10" y="182" width="110" height="46" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5" />
          <text x="65" y="202" font-size="8.5" fill="#0f172a" font-weight="bold" text-anchor="middle">PERA FERROVIÁRIA</text>
          <text x="65" y="216" font-size="7" fill="#64748b" text-anchor="middle">2x Switch IP67 • Balanças</text>

          <!-- Node: Berço 098 / CCO -->
          <rect x="340" y="182" width="110" height="46" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5" />
          <text x="395" y="202" font-size="8.5" fill="#0f172a" font-weight="bold" text-anchor="middle">BERÇO 098 / CCO</text>
          <text x="395" y="216" font-size="7" fill="#64748b" text-anchor="middle">NVR • Câmeras Cais • Telões</text>
        </svg>
      </div>
    </div>

    <!-- Destaques Técnicos -->
    <div style="display: flex; flex-direction: column; gap: 8pt;">
      <div class="card">
        <div class="card-header" style="font-size: 9pt;">Por que o Prédio Administrativo é o Centro?</div>
        <ul class="bullet-list" style="margin-top: 2pt;">
          <li><strong>Sala de CPD Dedicada:</strong> Rack fechado de 42U com controle de climatização e nobreak de 3 kVA.</li>
          <li><strong>Concentração de Serviços:</strong> Servidores de Banco de Dados, ERP portuário, Storage SAN/NAS e saída Internet.</li>
          <li><strong>Tolerância e Isolamento:</strong> Distante da agressividade direta de maresia do cais (Berço 098).</li>
        </ul>
      </div>

      <div class="card" style="flex: 1;">
        <div class="card-header" style="font-size: 9pt;">Volume de Ativos no Campus</div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6pt; margin-top: 3pt;">
          <div class="card-white" style="text-align: center;">
            <div style="font-size: 16pt; font-weight: 800; color: #0284c7;">104</div>
            <div style="font-size: 7pt; color: #64748b;">DISPOSITIVOS TOTAIS</div>
          </div>
          <div class="card-white" style="text-align: center;">
            <div style="font-size: 16pt; font-weight: 800; color: #15803d;">28</div>
            <div style="font-size: 7pt; color: #64748b;">CÂMERAS IP CFTV</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span class="slide-footer-brand">Terminal Portuário do Itaqui • Topologia de Campus</span>
    <span>Slide 4</span>
  </div>
</div>

<!-- ==========================================
     SLIDE 5: PRÉDIO ADMINISTRATIVO (IMAGEM REAL)
     ========================================== -->
<div class="slide">
  <div class="badge badge-purple">SETOR 1 • GABRIEL ORDONEZ & HIGOR GABRIEL</div>
  <div class="slide-title">Prédio Administrativo: CPD Central & Topologia</div>
  <div class="slide-subtitle">
    Núcleo central de processamento e telecomunicações com 108 pontos Cat6, 3 servidores, storage SAN e Wi-Fi 6.
  </div>

  <div class="grid-sector">
    <!-- Imagem Real da Dupla -->
    <div class="img-frame">
      <img src="{img_adm}" alt="Topologia Prédio Administrativo" />
    </div>

    <!-- Dados Sintéticos -->
    <div style="display: flex; flex-direction: column; gap: 8pt;">
      <div class="card">
        <div class="card-header" style="color: #7e22ce;">🏢 Ativos do CPD Central</div>
        <ul class="bullet-list">
          <li><strong>Switches:</strong> 3× Cisco Catalyst 2960-48P PoE+ (144 portas).</li>
          <li><strong>Core/Gateway:</strong> Agregador 10 Gb/s + Gateway ER8411.</li>
          <li><strong>Servidores:</strong> 3x PowerEdge (AD/DNS, ERP, Backup).</li>
          <li><strong>Storage:</strong> 1 SAN/NAS em rede isolada 10 Gb/s.</li>
          <li><strong>Wi-Fi & Pontos:</strong> 4 APs Wi-Fi 6 e 108 tomadas Cat6.</li>
        </ul>
      </div>

      <div class="card" style="flex: 1;">
        <div class="card-header" style="color: #0369a1;">⚙️ Segmentação Lógica</div>
        <table class="table-compact">
          <tr><th>VLAN</th><th>Aplicação</th><th>Faixa de IP</th></tr>
          <tr><td><span class="pill pill-blue">10</span></td><td>Dados Corp</td><td><code>10.100.10.0/24</code></td></tr>
          <tr><td><span class="pill pill-green">20</span></td><td>Voz VoIP (QoS)</td><td><code>10.100.20.0/24</code></td></tr>
          <tr><td><span class="pill pill-purple">50</span></td><td>Wi-Fi Corp</td><td><code>10.100.50.0/24</code></td></tr>
          <tr><td><span class="pill pill-slate">99</span></td><td>Gerência TI</td><td><code>10.100.99.0/24</code></td></tr>
        </table>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span class="slide-footer-brand">Terminal Portuário do Itaqui • Prédio Administrativo</span>
    <span>Slide 5</span>
  </div>
</div>

<!-- ==========================================
     SLIDE 6: PORTARIA TP (IMAGEM REAL)
     ========================================== -->
<div class="slide">
  <div class="badge badge-blue">SETOR 2 • TAINO SAMUEL & VICTOR CABRAL</div>
  <div class="slide-title">Portaria TP: Controle de Acesso & CFTV LPR</div>
  <div class="slide-subtitle">
    Triagem rodoferroviária perimetral com pesagem de caminhões, reconhecimento óptico de placas e controle biométrico.
  </div>

  <div class="grid-sector">
    <!-- Imagem Real da Dupla -->
    <div class="img-frame">
      <img src="{img_portaria}" alt="Topologia Portaria TP" />
    </div>

    <!-- Dados Sintéticos -->
    <div style="display: flex; flex-direction: column; gap: 8pt;">
      <div class="card">
        <div class="card-header" style="color: #0284c7;">🚧 Ativos de Campo</div>
        <ul class="bullet-list">
          <li><strong>Switch:</strong> 1× Cisco Catalyst 2960-16P PoE+ em rack 12U.</li>
          <li><strong>Uplink:</strong> Par de fibra OS2 direto ao CPD Central (450m).</li>
          <li><strong>Câmeras:</strong> 4 Câmeras IP Full HD LPR (Placas de carretas).</li>
          <li><strong>Acesso:</strong> 1 Catraca eletrônica biométrica/RFID IP.</li>
          <li><strong>Wi-Fi:</strong> 1 AP externo para motoristas e visitantes.</li>
        </ul>
      </div>

      <div class="card" style="flex: 1;">
        <div class="card-header" style="color: #15803d;">🛡️ Segmentação Lógica</div>
        <table class="table-compact">
          <tr><th>VLAN</th><th>Aplicação</th><th>Faixa de IP</th></tr>
          <tr><td><span class="pill pill-amber">40</span></td><td>Catracas / Acesso</td><td><code>10.100.40.0/24</code></td></tr>
          <tr><td><span class="pill pill-blue">30</span></td><td>CFTV LPR</td><td><code>10.100.30.0/24</code></td></tr>
          <tr><td><span class="pill pill-purple">60</span></td><td>Visitantes (Isolada)</td><td><code>10.100.60.0/24</code></td></tr>
          <tr><td><span class="pill pill-slate">99</span></td><td>Gerência TI</td><td><code>10.100.99.0/24</code></td></tr>
        </table>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span class="slide-footer-brand">Terminal Portuário do Itaqui • Portaria TP</span>
    <span>Slide 6</span>
  </div>
</div>

<!-- ==========================================
     SLIDE 7: SILO DE GRÃOS (IMAGEM REAL)
     ========================================== -->
<div class="slide">
  <div class="badge badge-amber">SETOR 3 • ASAFE & LUCAS</div>
  <div class="slide-title">Silo de Grãos: Automação Industrial & IoT</div>
  <div class="slide-subtitle">
    Área industrial classificada (Zona Ex) com monitoramento contínuo de temperatura de grãos, gases e esteiras de moega.
  </div>

  <div class="grid-sector">
    <!-- Imagem Real da Dupla -->
    <div class="img-frame" style="background: #0f172a;">
      <img src="{img_silo}" alt="Planta Silo de Grãos" />
    </div>

    <!-- Dados Sintéticos -->
    <div style="display: flex; flex-direction: column; gap: 8pt;">
      <div class="card">
        <div class="card-header" style="color: #b45309;">🌾 Ativos Industriais</div>
        <ul class="bullet-list">
          <li><strong>Switch:</strong> 1× Industrial Ruggedized 24p PoE+ (NEMA 4X / IP67).</li>
          <li><strong>Uplink:</strong> 850m de fibra OS2 subterrânea até o CPD Central.</li>
          <li><strong>Câmeras:</strong> 5 Câmeras antideflagrantes nos silos.</li>
          <li><strong>Sensores:</strong> Termometria de massa e gás (CO/Fosfina).</li>
          <li><strong>Cabos:</strong> Cat6 STP blindado com aterramento industrial.</li>
        </ul>
      </div>

      <div class="card" style="flex: 1;">
        <div class="card-header" style="color: #0369a1;">📊 Segmentação Lógica</div>
        <table class="table-compact">
          <tr><th>VLAN</th><th>Aplicação</th><th>Faixa de IP</th></tr>
          <tr><td><span class="pill pill-green">70</span></td><td>Sensores IoT Modbus</td><td><code>10.100.70.0/27</code></td></tr>
          <tr><td><span class="pill pill-blue">30</span></td><td>CFTV Moega / Silos</td><td><code>10.100.30.0/24</code></td></tr>
          <tr><td><span class="pill pill-purple">50</span></td><td>Wi-Fi Operacional</td><td><code>10.100.50.0/24</code></td></tr>
          <tr><td><span class="pill pill-slate">99</span></td><td>Gerência TI</td><td><code>10.100.99.0/24</code></td></tr>
        </table>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span class="slide-footer-brand">Terminal Portuário do Itaqui • Silo de Grãos</span>
    <span>Slide 7</span>
  </div>
</div>

<!-- ==========================================
     SLIDE 8: PERA FERROVIÁRIA (IMAGEM REAL)
     ========================================== -->
<div class="slide">
  <div class="badge badge-green">SETOR 4 • JOÃO LUCAS & JAYLON COELHO</div>
  <div class="slide-title">Pera Ferroviária: Pesagem & OCR de Vagões</div>
  <div class="slide-subtitle">
    Circuito ferroviário de 600 metros de linha com leitura automática de vagões e pesagem em movimento de eixos (WIM).
  </div>

  <div class="grid-sector">
    <!-- Imagem Real da Dupla -->
    <div class="img-frame">
      <img src="{img_pera}" alt="Planta Pera Ferroviária" />
    </div>

    <!-- Dados Sintéticos -->
    <div style="display: flex; flex-direction: column; gap: 8pt;">
      <div class="card">
        <div class="card-header" style="color: #15803d;">🚂 Ativos de Via</div>
        <ul class="bullet-list">
          <li><strong>Switches:</strong> 2× Industriais Cisco IE-3000/4000 PoE+ IP67.</li>
          <li><strong>Uplink:</strong> Fibra OS2 600m direto ao CPD Central do ADM.</li>
          <li><strong>OCR:</strong> 10 Câmeras especiais para identificação de vagões.</li>
          <li><strong>Balanças:</strong> 2 Balanças dinâmicas de pesagem de eixos.</li>
          <li><strong>Gabinete:</strong> Armários de inox 316 com amortecedores.</li>
        </ul>
      </div>

      <div class="card" style="flex: 1;">
        <div class="card-header" style="color: #0369a1;">⚖️ Segmentação Lógica</div>
        <table class="table-compact">
          <tr><th>VLAN</th><th>Aplicação</th><th>Faixa de IP</th></tr>
          <tr><td><span class="pill pill-blue">30</span></td><td>CFTV / OCR Vagões</td><td><code>10.100.30.0/24</code></td></tr>
          <tr><td><span class="pill pill-green">70</span></td><td>Balanças Dinâmicas</td><td><code>10.100.72.0/27</code></td></tr>
          <tr><td><span class="pill pill-slate">99</span></td><td>Gerência Switches</td><td><code>10.100.99.0/24</code></td></tr>
        </table>
        <div style="font-size: 7pt; color: #15803d; font-weight: 700; margin-top: 4pt;">
          ⚡ Latência estrita &lt; 10 ms para pesagem instantânea.
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span class="slide-footer-brand">Terminal Portuário do Itaqui • Pera Ferroviária</span>
    <span>Slide 8</span>
  </div>
</div>

<!-- ==========================================
     SLIDE 9: BERÇO 098 / CCO (IMAGEM REAL)
     ========================================== -->
<div class="slide">
  <div class="badge">SETOR 5 • MATEUS DANTAS & RENAN PIRES</div>
  <div class="slide-title">Berço 098 / CCO: Sala de Operações & Cais</div>
  <div class="slide-subtitle">
    Centro de comando de atracação marítima e monitoramento náutico. Conectado por fibra óptica direta ao CPD Central.
  </div>

  <div class="grid-sector">
    <!-- Imagem Real da Dupla -->
    <div class="img-frame">
      <img src="{img_inspetoria}" alt="Planta Inspetoria Berço 098" />
    </div>

    <!-- Dados Sintéticos -->
    <div style="display: flex; flex-direction: column; gap: 8pt;">
      <div class="card">
        <div class="card-header" style="color: #0f172a;">⚓ Sala de Operações & Cais</div>
        <ul class="bullet-list">
          <li><strong>Uplink:</strong> Fibra OS2 320m conectada direto ao CPD do ADM.</li>
          <li><strong>Switches:</strong> Switch 24p PoE+ para consoles de despacho.</li>
          <li><strong>NVR Central:</strong> 32 Canais (64 TB RAID 5 - Gravação contínua).</li>
          <li><strong>Cais:</strong> 4 Câmeras PTZ 40x monitorando atracação de navios.</li>
          <li><strong>VoIP:</strong> 5 Telefones IP para coordenação marítima.</li>
        </ul>
      </div>

      <div class="card" style="flex: 1;">
        <div class="card-header" style="color: #0284c7;">🧠 Integração Operacional</div>
        <ul class="bullet-list">
          <li><strong>Telões do CCO:</strong> Supervisão em tempo real de silos, trens e cais.</li>
          <li><strong>CFTV Centralizado:</strong> Recepção dos fluxos RTSP de todas as 28 câmeras.</li>
          <li><strong>QoS:</strong> Voz e despacho náutico com prioridade absoluta.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span class="slide-footer-brand">Terminal Portuário do Itaqui • Berço 098 / CCO</span>
    <span>Slide 9</span>
  </div>
</div>

<!-- ==========================================
     SLIDE 10: MATRIZ CONSOLIDADA DE VLANS
     ========================================== -->
<div class="slide">
  <div class="badge">SEGMENTAÇÃO LÓGICA</div>
  <div class="slide-title">Matriz Consolidada de VLANs do Complexo</div>
  <div class="slide-subtitle">
    Superbloco <code>10.100.0.0/16</code> distribuído de forma estanque entre os serviços, eliminando colisões de IP e vazamento de tráfego.
  </div>

  <div class="grid-2">
    <div class="card">
      <div class="card-header">Tabela Geral de Segmentação</div>
      <table class="table-compact" style="font-size: 7.5pt;">
        <thead>
          <tr><th>VLAN</th><th>Nome</th><th>Endereçamento</th><th>Escopo</th></tr>
        </thead>
        <tbody>
          <tr><td><span class="pill pill-blue">10</span></td><td>Dados Corp</td><td><code>10.100.10.0/24</code></td><td>PCs Administrativos</td></tr>
          <tr><td><span class="pill pill-green">20</span></td><td>Voz / VoIP</td><td><code>10.100.20.0/24</code></td><td>Telefonia (QoS Prioritário)</td></tr>
          <tr><td><span class="pill pill-amber">30</span></td><td>CFTV IP</td><td><code>10.100.30.0/24</code></td><td>28 Câmeras IP & NVR</td></tr>
          <tr><td><span class="pill pill-purple">40</span></td><td>Controle Acesso</td><td><code>10.100.40.0/24</code></td><td>Catracas da Portaria</td></tr>
          <tr><td><span class="pill pill-blue">50</span></td><td>Wi-Fi Corp</td><td><code>10.100.50.0/24</code></td><td>Tablets e Notebooks</td></tr>
          <tr><td><span class="pill pill-slate">60</span></td><td>Wi-Fi Visitantes</td><td><code>10.100.60.0/24</code></td><td>Motoristas (Isolada)</td></tr>
          <tr><td><span class="pill pill-green">70</span></td><td>IoT / Automação</td><td><code>10.100.70.0/24</code></td><td>Sensores e Balanças</td></tr>
          <tr><td><span class="pill pill-slate">99</span></td><td>Gerência TI</td><td><code>10.100.99.0/24</code></td><td>Switches e Roteadores</td></tr>
        </tbody>
      </table>
    </div>

    <div style="display: flex; flex-direction: column; gap: 8pt;">
      <div class="card">
        <div class="card-header" style="color: #0284c7;">Regras de Roteamento & ACLs</div>
        <ul class="bullet-list">
          <li><strong>Isolamento Total de Câmeras:</strong> VLAN 30 não possui rota para a Internet.</li>
          <li><strong>Segurança Industrial OT:</strong> Sensores e balanças acessam somente o servidor de pesagem.</li>
          <li><strong>Visitantes Estanques:</strong> Acesso restrito a navegação web pública sem acesso interno.</li>
        </ul>
      </div>

      <div class="card" style="flex: 1; background: #f0fdf4; border-color: #bbf7d0;">
        <div class="card-header" style="color: #15803d;">Conformidade Técnica</div>
        <div style="font-size: 7.5pt; color: #166534; line-height: 1.4;">
          ✓ Conflitos originais de IP <code>192.168.1.0/24</code> foram 100% saneados.<br>
          ✓ Falhas de DHCP/APIPA eliminadas com pools centralizados no Core do CPD.<br>
          ✓ 100% interoperável no laboratório consolidado <code>Terminal-Portuario-Geral.pkt</code>.
        </div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span class="slide-footer-brand">Terminal Portuário do Itaqui • Matriz Lógica</span>
    <span>Slide 10</span>
  </div>
</div>

<!-- ==========================================
     SLIDE 11: CONCLUSÃO & HOMOLOGAÇÃO
     ========================================== -->
<div class="slide">
  <div class="badge badge-green">CONCLUSÃO</div>
  <div class="slide-title">Conclusão & Homologação Técnica</div>
  <div class="slide-subtitle">
    Projeto consolidado e validado em conformidade estrita com todos os requisitos do edital da disciplina de Infraestrutura de Redes.
  </div>

  <div class="grid-2">
    <!-- 4 Pilares -->
    <div style="display: flex; flex-direction: column; gap: 6pt;">
      <div class="grid-2" style="gap: 6pt;">
        <div class="card" style="padding: 8pt 10pt;">
          <div style="font-size: 8.5pt; font-weight: 700; color: #0284c7;">Conectividade</div>
          <div style="font-size: 7pt; color: #475569; margin-top: 1pt;">Backbone em estrela com fibra OS2 ancorado no CPD do Administrativo.</div>
        </div>
        <div class="card" style="padding: 8pt 10pt;">
          <div style="font-size: 8.5pt; font-weight: 700; color: #15803d;">Segurança</div>
          <div style="font-size: 7pt; color: #475569; margin-top: 1pt;">8 VLANs isoladas com ACLs restritivas e Zero Trust.</div>
        </div>
        <div class="card" style="padding: 8pt 10pt;">
          <div style="font-size: 8.5pt; font-weight: 700; color: #b45309;">Disponibilidade</div>
          <div style="font-size: 7pt; color: #475569; margin-top: 1pt;">Switches industriais IP67 e Nobreaks UPS senoidais.</div>
        </div>
        <div class="card" style="padding: 8pt 10pt;">
          <div style="font-size: 8.5pt; font-weight: 700; color: #7e22ce;">Escalabilidade</div>
          <div style="font-size: 7pt; color: #475569; margin-top: 1pt;">Estrela modular pronta para expansão de berços e silos.</div>
        </div>
      </div>

      <div class="card" style="background: #eff6ff; border: 1px solid #bfdbfe; padding: 8pt 12pt;">
        <div style="font-size: 8pt; font-weight: 700; color: #1e40af;">Impacto Operacional Comprovado:</div>
        <div style="font-size: 7.5pt; color: #1e3a8a; margin-top: 2pt;">
          Garante operação contínua 24/7/365, elimina riscos de demurrage marítimo de até US$ 80k/dia e integra telemetria, pesagem e faturamento em tempo real.
        </div>
      </div>
    </div>

    <!-- Indicadores -->
    <div class="card">
      <div class="card-header" style="margin-bottom: 4pt;">Quadro Consolidado de Indicadores</div>
      <table class="table-compact" style="font-size: 8pt;">
        <thead>
          <tr><th>Indicador</th><th style="text-align: right;">Resultado Final</th></tr>
        </thead>
        <tbody>
          <tr><td>Áreas Operacionais Integradas</td><td style="text-align: right; font-weight: 700;">5 Áreas</td></tr>
          <tr><td>Total de Dispositivos Homologados</td><td style="text-align: right; font-weight: 700;">104 Ativos</td></tr>
          <tr><td>Câmeras IP de Alta Definição</td><td style="text-align: right; font-weight: 700;">28 Câmeras</td></tr>
          <tr><td>Segmentos de VLAN Lógica</td><td style="text-align: right; font-weight: 700;">8 VLANs</td></tr>
          <tr><td>Extensão de Fibra Óptica OS2</td><td style="text-align: right; font-weight: 700;">~2.220 Metros</td></tr>
          <tr><td>Subtotal de Ativos de Rede</td><td style="text-align: right; font-family: 'JetBrains Mono';">R$ 904.034,14</td></tr>
          <tr><td>Reserva Técnica (20%)</td><td style="text-align: right; font-family: 'JetBrains Mono';">R$ 180.806,83</td></tr>
          <tr style="background: #f1f5f9; font-weight: 800; font-size: 9pt;">
            <td>Orçamento Global Estimado</td>
            <td style="text-align: right; font-family: 'JetBrains Mono'; color: #0284c7;">R$ 1.084.840,97</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="slide-footer">
    <span class="slide-footer-brand">PBL Infraestrutura de Redes • UNDB São Luís - MA</span>
    <span>Homologado para Defesa Final de Projeto • 2026.2</span>
  </div>
</div>

</body>
</html>
"""

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML gerado em: {HTML_FILE}")

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(EDGE_PATH):
    EDGE_PATH = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

file_url = f"file:///{HTML_FILE.replace(os.sep, '/')}"

cmd = [
    EDGE_PATH,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={PDF_OUTPUT}",
    file_url
]

print("Executando renderizacao do PDF via Microsoft Edge...")
res = subprocess.run(cmd, capture_output=True, text=True)

if os.path.exists(PDF_OUTPUT):
    doc = pdfium.PdfDocument(PDF_OUTPUT)
    print(f"\nPDF RECOMPILADO COM SUCESSO (CENTRALIZADO NO ADM)!")
    print(f"  Arquivo: {os.path.basename(PDF_OUTPUT)}")
    print(f"  Tamanho: {os.path.getsize(PDF_OUTPUT)} bytes")
    print(f"  Total de Paginas: {len(doc)}")
else:
    print("ERRO ao gerar PDF!")
    print(res.stderr)
