# -*- coding: utf-8 -*-
"""
Gerador da Auditoria Técnica Completa - Infraestrutura de Redes UNDB 4.0
Projeto: Terminal Portuário de São Luís (Problema 1 - 2026.2)
Professor: Me. Arlley Costa
"""

import os
import json

output_file = "Auditoria-Geral-InfraRedes-UNDB.html"

# Carregar dados consolidados
with open('consolidated_data.json', 'r', encoding='utf-8') as f:
    sectors_data = json.load(f)

html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Auditoria Técnica e Revisão Geral de Infraestrutura de Redes | Terminal Portuário UNDB</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-main: #0b0f19;
      --bg-card: #111827;
      --bg-card-hover: #1f2937;
      --bg-card-alt: #162032;
      --border-color: #1e293b;
      --border-accent: #334155;
      
      --text-primary: #f8fafc;
      --text-secondary: #94a3b8;
      --text-muted: #64748b;
      
      --accent-cyan: #06b6d4;
      --accent-blue: #3b82f6;
      --accent-indigo: #6366f1;
      --accent-emerald: #10b981;
      --accent-amber: #f59e0b;
      --accent-rose: #f43f5e;
      --accent-purple: #a855f7;
      
      --badge-danger-bg: rgba(244, 63, 94, 0.15);
      --badge-danger-text: #fb7185;
      --badge-danger-border: rgba(244, 63, 94, 0.3);
      
      --badge-warn-bg: rgba(245, 158, 11, 0.15);
      --badge-warn-text: #fbbf24;
      --badge-warn-border: rgba(245, 158, 11, 0.3);
      
      --badge-success-bg: rgba(16, 185, 129, 0.15);
      --badge-success-text: #34d399;
      --badge-success-border: rgba(16, 185, 129, 0.3);
      
      --badge-info-bg: rgba(6, 182, 212, 0.15);
      --badge-info-text: #22d3ee;
      --badge-info-border: rgba(6, 182, 212, 0.3);
      
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.2);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.4), 0 4px 6px -2px rgba(0, 0, 0, 0.25);
      --shadow-glow: 0 0 25px -5px rgba(6, 182, 212, 0.25);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: var(--bg-main);
      color: var(--text-primary);
      line-height: 1.6;
      font-size: 15px;
      overflow-x: hidden;
    }

    /* Reading progress bar */
    #progress-bar {
      position: fixed;
      top: 0;
      left: 0;
      height: 3px;
      background: linear-gradient(90deg, var(--accent-cyan), var(--accent-blue), var(--accent-indigo));
      z-index: 1000;
      width: 0%;
      transition: width 0.1s ease;
    }

    /* Header */
    header.hero-header {
      background: linear-gradient(180deg, #0f172a 0%, #0b0f19 100%);
      border-bottom: 1px solid var(--border-color);
      padding: 45px 30px 40px;
      position: relative;
      overflow: hidden;
    }
    header.hero-header::before {
      content: '';
      position: absolute;
      top: -100px;
      right: -100px;
      width: 400px;
      height: 400px;
      background: radial-gradient(circle, rgba(6, 182, 212, 0.15) 0%, rgba(0,0,0,0) 70%);
      pointer-events: none;
    }

    .container {
      max-width: 1380px;
      margin: 0 auto;
      padding: 0 24px;
    }

    .hero-top-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
      margin-bottom: 18px;
    }

    .meta-tag {
      font-size: 12px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      padding: 4px 12px;
      border-radius: 9999px;
      background: var(--bg-card);
      border: 1px solid var(--border-accent);
      color: var(--text-secondary);
    }
    .meta-tag.highlight {
      background: rgba(6, 182, 212, 0.12);
      color: var(--accent-cyan);
      border-color: rgba(6, 182, 212, 0.4);
    }
    .meta-tag.danger {
      background: var(--badge-danger-bg);
      color: var(--badge-danger-text);
      border-color: var(--badge-danger-border);
    }

    h1.hero-title {
      font-size: 2.3rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      line-height: 1.25;
      margin-bottom: 14px;
      background: linear-gradient(135deg, #ffffff 30%, #94a3b8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    p.hero-subtitle {
      font-size: 1.1rem;
      color: var(--text-secondary);
      max-width: 980px;
      margin-bottom: 24px;
      line-height: 1.6;
    }

    .hero-quick-stats {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      margin-top: 25px;
    }

    .stat-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 16px 20px;
      position: relative;
      transition: all 0.2s ease;
    }
    .stat-card:hover {
      border-color: var(--accent-cyan);
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
    }
    .stat-label {
      font-size: 12px;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      font-weight: 600;
      margin-bottom: 6px;
    }
    .stat-value {
      font-size: 1.8rem;
      font-weight: 700;
      color: var(--text-primary);
      font-family: 'JetBrains Mono', monospace;
    }
    .stat-desc {
      font-size: 12px;
      margin-top: 4px;
      color: var(--text-secondary);
    }

    /* Layout Principal: Sidebar + Conteúdo */
    .app-layout {
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 32px;
      margin-top: 36px;
      margin-bottom: 80px;
    }

    @media (max-width: 1080px) {
      .app-layout {
        grid-template-columns: 1fr;
      }
      .sticky-sidebar {
        display: none;
      }
    }

    /* Sidebar Navegação */
    .sticky-sidebar {
      position: sticky;
      top: 24px;
      height: fit-content;
      max-height: calc(100vh - 48px);
      overflow-y: auto;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 20px;
      scrollbar-width: thin;
    }

    .sidebar-title {
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
      font-weight: 700;
      margin-bottom: 14px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--border-color);
    }

    .nav-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .nav-item a {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 12px;
      color: var(--text-secondary);
      text-decoration: none;
      font-size: 13.5px;
      font-weight: 500;
      border-radius: 8px;
      transition: all 0.15s ease;
    }
    .nav-item a:hover {
      background: var(--bg-card-hover);
      color: var(--text-primary);
    }
    .nav-item a.active {
      background: rgba(6, 182, 212, 0.15);
      color: var(--accent-cyan);
      font-weight: 600;
      border-left: 3px solid var(--accent-cyan);
    }
    .nav-badge {
      margin-left: auto;
      font-size: 11px;
      padding: 2px 7px;
      border-radius: 9999px;
      background: var(--bg-card-hover);
      color: var(--text-muted);
      font-family: 'JetBrains Mono', monospace;
    }

    /* Conteúdo Principal */
    .main-content {
      min-width: 0; /* Previne overflow de flex/grid */
    }

    /* Seções */
    section.audit-section {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 32px 36px;
      margin-bottom: 32px;
      box-shadow: var(--shadow-sm);
      scroll-margin-top: 30px;
    }

    .section-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 22px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border-color);
    }

    .section-header-left {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .section-number {
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      font-weight: 700;
      color: var(--accent-cyan);
      background: rgba(6, 182, 212, 0.12);
      padding: 4px 10px;
      border-radius: 6px;
      border: 1px solid rgba(6, 182, 212, 0.25);
    }

    h2.section-title {
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--text-primary);
      letter-spacing: -0.01em;
    }

    p.section-intro {
      font-size: 14.5px;
      color: var(--text-secondary);
      margin-bottom: 24px;
      line-height: 1.65;
    }

    /* Alertas Callouts */
    .callout {
      border-radius: 10px;
      padding: 16px 20px;
      margin: 20px 0;
      display: flex;
      gap: 16px;
      border-left: 4px solid;
    }
    .callout-icon {
      font-size: 20px;
      line-height: 1;
      margin-top: 2px;
      flex-shrink: 0;
    }
    .callout-content {
      font-size: 14px;
      color: var(--text-primary);
    }
    .callout-content strong {
      display: block;
      margin-bottom: 4px;
      font-size: 14.5px;
    }
    
    .callout.danger {
      background: rgba(244, 63, 94, 0.08);
      border-color: var(--accent-rose);
    }
    .callout.danger strong { color: var(--badge-danger-text); }

    .callout.warning {
      background: rgba(245, 158, 11, 0.08);
      border-color: var(--accent-amber);
    }
    .callout.warning strong { color: var(--badge-warn-text); }

    .callout.info {
      background: rgba(6, 182, 212, 0.08);
      border-color: var(--accent-cyan);
    }
    .callout.info strong { color: var(--accent-cyan); }

    .callout.success {
      background: rgba(16, 185, 129, 0.08);
      border-color: var(--accent-emerald);
    }
    .callout.success strong { color: var(--badge-success-text); }

    /* Tabelas */
    .table-container {
      overflow-x: auto;
      margin: 20px 0;
      border-radius: 10px;
      border: 1px solid var(--border-color);
      background: var(--bg-main);
    }

    table.data-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 13.5px;
    }

    table.data-table th {
      background: #131d2e;
      color: var(--text-secondary);
      font-weight: 600;
      text-transform: uppercase;
      font-size: 11.5px;
      letter-spacing: 0.05em;
      padding: 12px 16px;
      border-bottom: 1px solid var(--border-accent);
      white-space: nowrap;
    }

    table.data-table td {
      padding: 12px 16px;
      border-bottom: 1px solid var(--border-color);
      color: var(--text-primary);
      vertical-align: middle;
    }

    table.data-table tbody tr:last-child td {
      border-bottom: none;
    }

    table.data-table tbody tr:hover {
      background: var(--bg-card-hover);
    }

    /* Badges */
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 11.5px;
      font-weight: 600;
      padding: 3px 10px;
      border-radius: 6px;
      white-space: nowrap;
    }
    .badge-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
    }
    .badge.danger {
      background: var(--badge-danger-bg);
      color: var(--badge-danger-text);
      border: 1px solid var(--badge-danger-border);
    }
    .badge.danger .badge-dot { background: var(--badge-danger-text); }

    .badge.warning {
      background: var(--badge-warn-bg);
      color: var(--badge-warn-text);
      border: 1px solid var(--badge-warn-border);
    }
    .badge.warning .badge-dot { background: var(--badge-warn-text); }

    .badge.success {
      background: var(--badge-success-bg);
      color: var(--badge-success-text);
      border: 1px solid var(--badge-success-border);
    }
    .badge.success .badge-dot { background: var(--badge-success-text); }

    .badge.info {
      background: var(--badge-info-bg);
      color: var(--badge-info-text);
      border: 1px solid var(--badge-info-border);
    }
    .badge.info .badge-dot { background: var(--badge-info-text); }

    .badge.neutral {
      background: rgba(148, 163, 184, 0.1);
      color: #cbd5e1;
      border: 1px solid rgba(148, 163, 184, 0.2);
    }
    .badge.neutral .badge-dot { background: #94a3b8; }

    /* Code snippets */
    code, .code-font {
      font-family: 'JetBrains Mono', monospace;
      font-size: 12.5px;
      background: #090d16;
      color: #38bdf8;
      padding: 2px 6px;
      border-radius: 4px;
      border: 1px solid rgba(56, 189, 248, 0.15);
    }

    pre {
      background: #080c14;
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 16px 20px;
      overflow-x: auto;
      margin: 16px 0;
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      color: #e2e8f0;
      line-height: 1.5;
    }

    /* Cards de Setores (Grid e Detalhes) */
    .sector-card {
      background: var(--bg-card-alt);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 24px;
      margin-bottom: 24px;
      transition: all 0.2s ease;
    }
    .sector-card:hover {
      border-color: var(--border-accent);
      box-shadow: var(--shadow-md);
    }

    .sector-card-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 16px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border-color);
    }

    .sector-card-title {
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--text-primary);
    }

    .sector-card-authors {
      font-size: 13px;
      color: var(--accent-cyan);
      margin-top: 2px;
    }

    .sector-grid-metrics {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
      margin: 16px 0;
    }

    .metric-box {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 12px 14px;
    }
    .metric-box-title {
      font-size: 11px;
      color: var(--text-muted);
      text-transform: uppercase;
      font-weight: 600;
      letter-spacing: 0.04em;
    }
    .metric-box-val {
      font-size: 14px;
      font-weight: 600;
      color: var(--text-primary);
      margin-top: 4px;
      font-family: 'JetBrains Mono', monospace;
    }

    /* Diagramas SVG Containers */
    .diagram-container {
      background: #080d1a;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 20px;
      margin: 24px 0;
      overflow-x: auto;
      text-align: center;
    }
    .diagram-caption {
      margin-top: 12px;
      font-size: 12.5px;
      color: var(--text-muted);
      font-style: italic;
    }

    /* Tabs / Filter buttons */
    .filter-bar {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 20px;
    }

    .filter-btn {
      background: var(--bg-card-hover);
      border: 1px solid var(--border-color);
      color: var(--text-secondary);
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 13px;
      cursor: pointer;
      font-weight: 500;
      transition: all 0.15s ease;
    }
    .filter-btn:hover {
      color: var(--text-primary);
      border-color: var(--border-accent);
    }
    .filter-btn.active {
      background: var(--accent-cyan);
      color: #0b0f19;
      border-color: var(--accent-cyan);
      font-weight: 600;
    }

    /* Two-column analysis layout */
    .two-col {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin: 16px 0;
    }
    @media (max-width: 850px) {
      .two-col {
        grid-template-columns: 1fr;
      }
    }

    .pro-con-box {
      border-radius: 10px;
      padding: 16px 20px;
      border: 1px solid var(--border-color);
    }
    .pro-box {
      background: rgba(16, 185, 129, 0.04);
      border-color: rgba(16, 185, 129, 0.2);
    }
    .pro-box h4 {
      color: var(--accent-emerald);
      font-size: 14px;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .con-box {
      background: rgba(244, 63, 94, 0.04);
      border-color: rgba(244, 63, 94, 0.2);
    }
    .con-box h4 {
      color: var(--accent-rose);
      font-size: 14px;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .audit-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 8px;
      font-size: 13px;
    }
    .audit-list li {
      position: relative;
      padding-left: 18px;
      color: var(--text-secondary);
      line-height: 1.5;
    }
    .audit-list li::before {
      content: '•';
      position: absolute;
      left: 4px;
      color: var(--text-muted);
    }
    .pro-box .audit-list li::before { color: var(--accent-emerald); }
    .con-box .audit-list li::before { color: var(--accent-rose); }

    /* Footer */
    footer.audit-footer {
      border-top: 1px solid var(--border-color);
      padding: 40px 0;
      background: #080c14;
      color: var(--text-muted);
      font-size: 13px;
      text-align: center;
    }

    /* Print optimization */
    @media print {
      body {
        background: #ffffff !important;
        color: #000000 !important;
        font-size: 11pt;
      }
      #progress-bar, .sticky-sidebar, .filter-bar, .print-hide {
        display: none !important;
      }
      .app-layout {
        grid-template-columns: 1fr !important;
        margin: 0 !important;
      }
      section.audit-section {
        background: #ffffff !important;
        border: 1px solid #cccccc !important;
        box-shadow: none !important;
        page-break-inside: avoid;
        margin-bottom: 20px !important;
        padding: 15px !important;
      }
      .table-container {
        border: 1px solid #dddddd !important;
        background: #ffffff !important;
      }
      table.data-table th {
        background: #eeeeee !important;
        color: #000000 !important;
      }
      table.data-table td {
        color: #000000 !important;
      }
      code {
        background: #f0f0f0 !important;
        color: #000000 !important;
        border: 1px solid #cccccc !important;
      }
      h1.hero-title {
        color: #000000 !important;
        -webkit-text-fill-color: initial !important;
      }
    }
  </style>
</head>
<body>
  <div id="progress-bar"></div>

  <!-- HERO HEADER -->
  <header class="hero-header">
    <div class="container">
      <div class="hero-top-meta">
        <span class="meta-tag highlight">UNDB 4.0 Escola de Tecnologia</span>
        <span class="meta-tag">Infraestrutura de Redes (80h)</span>
        <span class="meta-tag">Prof. Me. Arlley Costa</span>
        <span class="meta-tag">Semestre 2026.2</span>
        <span class="meta-tag danger">Auditoria Independente de Engenharia</span>
      </div>

      <h1 class="hero-title">Auditoria Técnica e Revisão Geral de Infraestrutura</h1>
      <p class="hero-subtitle">
        Revisão minuciosa, diagnóstico de conformidade normativa e plano de saneamento técnico para a expansão do 
        <strong>Complexo Portuário de São Luís / Porto do Itaqui (125.340 m²)</strong>, cobrindo Portaria TP, Prédio Administrativo, 
        Silo de Grãos, Pera Ferroviária e Prédio da Inspetoria / CCO Berço 098.
      </p>

      <div class="hero-quick-stats">
        <div class="stat-card">
          <div class="stat-label">Investimento Previsto</div>
          <div class="stat-value" style="color: var(--accent-emerald);">R$ 2,5 Bi</div>
          <div class="stat-desc">Complexo Novo Terminal Portuário</div>
        </div>
        <div class="stat-card">
          <div class="stat-label">Área do Complexo</div>
          <div class="stat-value" style="color: var(--accent-cyan);">125.340 m²</div>
          <div class="stat-desc">5 Setores Operacionais Integrados</div>
        </div>
        <div class="stat-card">
          <div class="stat-label">Score de Integração</div>
          <div class="stat-value" style="color: var(--accent-rose);">58 / 100</div>
          <div class="stat-desc">Reprovado por Colisão de IPs</div>
        </div>
        <div class="stat-card">
          <div class="stat-label">Discrepância Orçamentária</div>
          <div class="stat-value" style="color: var(--accent-amber);">R$ 897,8k</div>
          <div class="stat-desc">R$ 16k (Silo) a R$ 708k (ADM)</div>
        </div>
        <div class="stat-card">
          <div class="stat-label">Risco Crítico Imediato</div>
          <div class="stat-value" style="color: var(--accent-rose);">Nível 5</div>
          <div class="stat-desc">Overlapping Subnets (4 de 5 prédios)</div>
        </div>
      </div>
    </div>
  </header>

  <div class="container">
    <div class="app-layout">
      <!-- SIDEBAR DE NAVEGAÇÃO -->
      <aside class="sticky-sidebar">
        <div class="sidebar-title">Sumário de Auditoria</div>
        <ul class="nav-list">
          <li class="nav-item"><a href="#sec-executivo" class="active"><span>01. Resumo Executivo</span><span class="nav-badge">Score</span></a></li>
          <li class="nav-item"><a href="#sec-macro" class=""><span>02. O "Efeito Ilha"</span><span class="nav-badge">Crítico</span></a></li>
          <li class="nav-item"><a href="#sec-portaria" class=""><span>03. Portaria TP</span><span class="nav-badge">88/100</span></a></li>
          <li class="nav-item"><a href="#sec-adm" class=""><span>04. Prédio Administrativo</span><span class="nav-badge">85/100</span></a></li>
          <li class="nav-item"><a href="#sec-pera" class=""><span>05. Pera Ferroviária</span><span class="nav-badge">72/100</span></a></li>
          <li class="nav-item"><a href="#sec-inspetoria" class=""><span>06. Inspetoria & CCO</span><span class="nav-badge">52/100</span></a></li>
          <li class="nav-item"><a href="#sec-silo" class=""><span>07. Silo de Grãos</span><span class="nav-badge">50/100</span></a></li>
          <li class="nav-item"><a href="#sec-uas" class=""><span>08. Conformidade Aulas (UAs)</span><span class="nav-badge">Normas</span></a></li>
          <li class="nav-item"><a href="#sec-arquitetura" class=""><span>09. Arquitetura Corrigida</span><span class="nav-badge">Solução</span></a></li>
          <li class="nav-item"><a href="#sec-banca" class=""><span>10. Defesa & Banca Final</span><span class="nav-badge">Q&A</span></a></li>
        </ul>
      </aside>

      <!-- CONTEÚDO PRINCIPAL -->
      <main class="main-content">

        <!-- 01. RESUMO EXECUTIVO -->
        <section id="sec-executivo" class="audit-section">
          <div class="section-header">
            <div class="section-header-left">
              <span class="section-number">01</span>
              <h2 class="section-title">Resumo Executivo & Scorecard Geral</h2>
            </div>
            <span class="badge danger"><span class="badge-dot"></span>Inviável sem Saneamento Lógico</span>
          </div>

          <p class="section-intro">
            Esta auditoria analisa a totalidade dos projetos entregues para o <strong>Problema 1 (Conectividade Empresarial 2026.2)</strong>, 
            avaliando tanto o cumprimento estrito dos requisitos do enunciado quanto a aderência técnica às normas ensinadas nas aulas de 
            Infraestrutura de Redes da UNDB (ANSI/TIA-568-D, ABNT NBR 14565, TIA-569, TIA-606, TIA-942, Modelos OSI e TCP/IP, e Boas Práticas Cisco).
          </p>

          <div class="callout danger">
            <div class="callout-icon">⚠️</div>
            <div class="callout-content">
              <strong>Veredito da Auditoria de Integração: COLAPSO DE ROTEAMENTO NO ENLACE DE CAMPUS</strong>
              Se os cinco setores fossem interconectados fisicamente hoje ao Backbone do Terminal Portuário, 
              <strong>a rede inteira entraria em colapso operacional imediato</strong>. Quatro das cinco duplas adotaram, de forma totalmente 
              isolada e sem coordenação prévia, os mesmíssimos blocos IPv4 privados (<code>192.168.10.0/24</code>, <code>192.168.20.0/24</code>, 
              <code>192.168.30.0/24</code>, <code>192.168.40.0/24</code> e <code>192.168.99.0/24</code>), tornando o roteamento inter-edifícios 
              impossível devido a <em>Overlapping IP Subnets</em>. Além disso, a Inspetoria (que deveria abrigar o CCO e concentrar as 10 câmeras 
              da ferrovia e o tráfego do píer) dimensionou apenas um mini rack de 12U com um switch de 24 portas, incapaz de receber as fibras ópticas externas.
            </div>
          </div>

          <h3 style="font-size: 1.1rem; margin: 24px 0 12px; color: var(--text-primary);">Scorecard Consolidado por Setor e Critério do Problema 1</h3>
          <div class="table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Setor / Unidade</th>
                  <th>Autores Responsáveis</th>
                  <th>Metodologia</th>
                  <th>As-Built / Físico</th>
                  <th>Topologia Lógica</th>
                  <th>Orçamento (BOM)</th>
                  <th>Packet Tracer</th>
                  <th>Score Individual</th>
                  <th>Status Global</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Portaria TP</strong></td>
                  <td>Taino Samuel & Victor Cabral</td>
                  <td><span class="badge success">Excelente (PPDIOO)</span></td>
                  <td><span class="badge success">Completo + CSV</span></td>
                  <td><span class="badge warning">Colisão c/ Campus</span></td>
                  <td><span class="badge success">R$ 32.981,83</span></td>
                  <td><span class="badge success">15 devs / Aprovado</span></td>
                  <td><strong style="color: var(--accent-emerald);">88 / 100</strong></td>
                  <td><span class="badge warning">Requer Ajuste IP</span></td>
                </tr>
                <tr>
                  <td><strong>Prédio Administrativo</strong></td>
                  <td>Gabriel Ordonez & Higor Gabriel</td>
                  <td><span class="badge success">Muito Bom</span></td>
                  <td><span class="badge success">Dimensionado (40p)</span></td>
                  <td><span class="badge success">VLSM 10.20.0.0/16</span></td>
                  <td><span class="badge warning">R$ 708.624,00*</span></td>
                  <td><span class="badge success">36 devs / 172 regras</span></td>
                  <td><strong style="color: var(--accent-emerald);">85 / 100</strong></td>
                  <td><span class="badge warning">Equalizar Orçamento</span></td>
                </tr>
                <tr>
                  <td><strong>Pera Ferroviária</strong></td>
                  <td>João Lucas & Jaylon Coelho</td>
                  <td><span class="badge warning">Parcial</span></td>
                  <td><span class="badge success">Fibra SMF + IP67</span></td>
                  <td><span class="badge danger">Colisão 192.168.x.x</span></td>
                  <td><span class="badge info">R$ 125.114,00</span></td>
                  <td><span class="badge warning">Isolado</span></td>
                  <td><strong style="color: var(--accent-amber);">72 / 100</strong></td>
                  <td><span class="badge danger">Falta Agregação CCO</span></td>
                </tr>
                <tr>
                  <td><strong>Inspetoria | Berço 098</strong></td>
                  <td>Mateus Dantas & Renan Pires</td>
                  <td><span class="badge danger">Superficial</span></td>
                  <td><span class="badge danger">Subdimensionado</span></td>
                  <td><span class="badge danger">Colisão 192.168.x.x</span></td>
                  <td><span class="badge danger">R$ 18.891,32**</span></td>
                  <td><span class="badge warning">Básico (1 switch)</span></td>
                  <td><strong style="color: var(--accent-rose);">52 / 100</strong></td>
                  <td><span class="badge danger">CCO Inviável</span></td>
                </tr>
                <tr>
                  <td><strong>Silo de Grãos</strong></td>
                  <td>Asafe & Lucas</td>
                  <td><span class="badge danger">Omitida</span></td>
                  <td><span class="badge danger">Risco H=30m & ATEX</span></td>
                  <td><span class="badge danger">Colisão 192.168.x.x</span></td>
                  <td><span class="badge danger">R$ 16.720,90</span></td>
                  <td><span class="badge warning">Básico</span></td>
                  <td><strong style="color: var(--accent-rose);">50 / 100</strong></td>
                  <td><span class="badge danger">Risco Atmosfera Ex</span></td>
                </tr>
              </tbody>
            </table>
          </div>
          <p style="font-size: 12px; color: var(--text-muted);">
            * O Prédio Administrativo incluiu a aquisição integral de 32 notebooks, 8 desktops e periféricos (R$ 234.500,00) + 20% de contingência geral.<br>
            ** A Inspetoria considerou que computadores, impressoras, servidores de câmeras e NVR já pertenciam ao porto, deixando o CCO desprovido de estações de monitoramento.
          </p>
        </section>

        <!-- 02. O EFEITO ILHA -->
        <section id="sec-macro" class="audit-section">
          <div class="section-header">
            <div class="section-header-left">
              <span class="section-number">02</span>
              <h2 class="section-title">A Falha Macro de Integração: O "Efeito Ilha"</h2>
            </div>
            <span class="badge danger"><span class="badge-dot"></span>Falha Arquitetural Crítica</span>
          </div>

          <p class="section-intro">
            O enunciado do Problema 1 deixa claro: trata-se de um único <strong>Complexo Portuário Integrado de 125.340 m²</strong>. 
            Contudo, a divisão do trabalho por duplas resultou em cinco "ilhas digitais autônomas", criando incompatibilidades 
            insuperáveis de camada 2 (VLANs), camada 3 (Endereçamento IP) e camada física (Backbone de Campus).
          </p>

          <!-- SVG DIAGRAMA DO CONFLITO -->
          <div class="diagram-container">
            <svg width="100%" height="320" viewBox="0 0 950 320" xmlns="http://www.w3.org/2000/svg" style="max-width: 950px; font-family: 'Inter', sans-serif;">
              <defs>
                <linearGradient id="redGlow" x1="0" y1="0" x2="1" y2="1">
                  <stop offset="0%" stop-color="#f43f5e" stop-opacity="0.3"/>
                  <stop offset="100%" stop-color="#881337" stop-opacity="0.6"/>
                </linearGradient>
                <linearGradient id="boxGlow" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stop-color="#1e293b"/>
                  <stop offset="100%" stop-color="#0f172a"/>
                </linearGradient>
                <filter id="shadow">
                  <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.5"/>
                </filter>
              </defs>

              <!-- Central Collision Node -->
              <circle cx="475" cy="160" r="65" fill="url(#redGlow)" stroke="#f43f5e" stroke-width="2.5" filter="url(#shadow)"/>
              <text x="475" y="148" text-anchor="middle" fill="#fb7185" font-weight="700" font-size="13">COLISÃO FATAL</text>
              <text x="475" y="165" text-anchor="middle" fill="#ffffff" font-weight="800" font-size="12">CORE DE CAMPUS</text>
              <text x="475" y="180" text-anchor="middle" fill="#fda4af" font-size="10">Overlapping Subnets</text>

              <!-- Lines to collision -->
              <line x1="160" y1="80" x2="415" y2="140" stroke="#f43f5e" stroke-width="2" stroke-dasharray="6,4"/>
              <line x1="160" y1="240" x2="415" y2="180" stroke="#f43f5e" stroke-width="2" stroke-dasharray="6,4"/>
              <line x1="790" y1="80" x2="535" y2="140" stroke="#f43f5e" stroke-width="2" stroke-dasharray="6,4"/>
              <line x1="790" y1="240" x2="535" y2="180" stroke="#f43f5e" stroke-width="2" stroke-dasharray="6,4"/>
              <line x1="475" y1="35" x2="475" y2="95" stroke="#10b981" stroke-width="2" stroke-dasharray="4,4"/>

              <!-- Box 1: Portaria TP -->
              <rect x="30" y="45" width="220" height="85" rx="8" fill="url(#boxGlow)" stroke="#f59e0b" stroke-width="1.5"/>
              <text x="45" y="70" fill="#fcd34d" font-weight="700" font-size="13">Portaria TP</text>
              <text x="45" y="88" fill="#94a3b8" font-size="11" font-family="'JetBrains Mono', monospace">VLAN 10: 192.168.10.0/24</text>
              <text x="45" y="104" fill="#94a3b8" font-size="11" font-family="'JetBrains Mono', monospace">VLAN 20: 192.168.20.0/24</text>
              <text x="45" y="120" fill="#94a3b8" font-size="11" font-family="'JetBrains Mono', monospace">VLAN 30: 192.168.30.0/24</text>

              <!-- Box 2: Pera Ferroviária -->
              <rect x="30" y="195" width="220" height="85" rx="8" fill="url(#boxGlow)" stroke="#f43f5e" stroke-width="1.5"/>
              <text x="45" y="220" fill="#fda4af" font-weight="700" font-size="13">Pera Ferroviária</text>
              <text x="45" y="238" fill="#fb7185" font-size="11" font-family="'JetBrains Mono', monospace">VLAN 20: 192.168.20.0/24 (CFTV)</text>
              <text x="45" y="254" fill="#fb7185" font-size="11" font-family="'JetBrains Mono', monospace">VLAN 30: 192.168.30.0/24 (Auto)</text>
              <text x="45" y="270" fill="#fb7185" font-size="11" font-family="'JetBrains Mono', monospace">VLAN 99: 192.168.99.0/24 (Ger)</text>

              <!-- Box 3: Inspetoria Berço 098 -->
              <rect x="700" y="45" width="220" height="85" rx="8" fill="url(#boxGlow)" stroke="#f43f5e" stroke-width="1.5"/>
              <text x="715" y="70" fill="#fda4af" font-weight="700" font-size="13">Inspetoria / CCO</text>
              <text x="715" y="88" fill="#fb7185" font-size="11" font-family="'JetBrains Mono', monospace">VLAN 10: 192.168.10.0/24 (Dados)</text>
              <text x="715" y="104" fill="#fb7185" font-size="11" font-family="'JetBrains Mono', monospace">VLAN 20: 192.168.20.0/24 (Voz)</text>
              <text x="715" y="120" fill="#fb7185" font-size="11" font-family="'JetBrains Mono', monospace">VLAN 40: 192.168.40.0/24 (CFTV)</text>

              <!-- Box 4: Silo de Grãos -->
              <rect x="700" y="195" width="220" height="85" rx="8" fill="url(#boxGlow)" stroke="#f43f5e" stroke-width="1.5"/>
              <text x="715" y="220" fill="#fda4af" font-weight="700" font-size="13">Silo de Grãos</text>
              <text x="715" y="238" fill="#fb7185" font-size="11" font-family="'JetBrains Mono', monospace">VLAN 10: 192.168.10.0/24</text>
              <text x="715" y="254" fill="#fb7185" font-size="11" font-family="'JetBrains Mono', monospace">VLAN 50: 192.168.50.0/24</text>
              <text x="715" y="270" fill="#fb7185" font-size="11" font-family="'JetBrains Mono', monospace">VLAN 80: 192.168.80.0/24</text>

              <!-- Box 5: Prédio Administrativo (Isolado no 10.20.0.0/16) -->
              <rect x="365" y="5" width="220" height="55" rx="8" fill="url(#boxGlow)" stroke="#10b981" stroke-width="1.5"/>
              <text x="475" y="25" text-anchor="middle" fill="#34d399" font-weight="700" font-size="12">Prédio Administrativo</text>
              <text x="475" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5" font-family="'JetBrains Mono', monospace">Faixa 10.20.0.0/16 (Isolada)</text>
            </svg>
            <div class="diagram-caption">Figura 1: Evidência gráfica da colisão de rotas gerada pelo particionamento descoordenado de sub-redes IPv4.</div>
          </div>

          <h3 style="font-size: 1.1rem; margin: 24px 0 12px; color: var(--text-primary);">Matriz de Colisão Direta de Endereçamento IP</h3>
          <div class="table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Faixa IPv4 Adotada</th>
                  <th>Portaria TP</th>
                  <th>Pera Ferroviária</th>
                  <th>Inspetoria / CCO</th>
                  <th>Silo de Grãos</th>
                  <th>Impacto no Roteador / Core</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><code>192.168.10.0/24</code></td>
                  <td><span class="badge neutral">VLAN 10 (Dados)</span></td>
                  <td>-</td>
                  <td><span class="badge neutral">VLAN 10 (Dados)</span></td>
                  <td><span class="badge neutral">VLAN 10 (Dados)</span></td>
                  <td><span class="badge danger">Conflito Tríplo de Rota</span></td>
                </tr>
                <tr>
                  <td><code>192.168.20.0/24</code></td>
                  <td><span class="badge neutral">VLAN 20 (Voz)</span></td>
                  <td><span class="badge neutral">VLAN 20 (CFTV)</span></td>
                  <td><span class="badge neutral">VLAN 20 (Voz)</span></td>
                  <td>-</td>
                  <td><span class="badge danger">Conflito Tríplo de Rota</span></td>
                </tr>
                <tr>
                  <td><code>192.168.30.0/24</code></td>
                  <td><span class="badge neutral">VLAN 30 (CFTV)</span></td>
                  <td><span class="badge neutral">VLAN 30 (Balanças)</span></td>
                  <td><span class="badge neutral">VLAN 30 (Wi-Fi)</span></td>
                  <td>-</td>
                  <td><span class="badge danger">Conflito Tríplo de Rota</span></td>
                </tr>
                <tr>
                  <td><code>192.168.40.0/24</code></td>
                  <td><span class="badge neutral">VLAN 40 (Catraca)</span></td>
                  <td>-</td>
                  <td><span class="badge neutral">VLAN 40 (CFTV)</span></td>
                  <td>-</td>
                  <td><span class="badge danger">Conflito Duplo de Rota</span></td>
                </tr>
                <tr>
                  <td><code>192.168.50.0/24</code></td>
                  <td><span class="badge neutral">VLAN 50 (Wi-Fi)</span></td>
                  <td>-</td>
                  <td>-</td>
                  <td><span class="badge neutral">VLAN 50 (CFTV)</span></td>
                  <td><span class="badge danger">Conflito Duplo de Rota</span></td>
                </tr>
                <tr>
                  <td><code>192.168.99.0/24</code></td>
                  <td><span class="badge neutral">VLAN 99 (Gerência)</span></td>
                  <td><span class="badge neutral">VLAN 99 (Gerência)</span></td>
                  <td><span class="badge neutral">VLAN 99 (Gerência)</span></td>
                  <td>-</td>
                  <td><span class="badge danger">Conflito Tríplo de Gerência</span></td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="callout warning">
            <div class="callout-icon">💡</div>
            <div class="callout-content">
              <strong>O Paradoxo da Inspetoria vs. Pera Ferroviária:</strong>
              O projeto da Pera Ferroviária baseia toda a sua viabilidade no envio do tráfego das 10 câmeras e 2 balanças via fibra óptica até o 
              <em>"Switch Central do CCO localizado na Inspetoria (Berço 098)"</em>. No entanto, os autores da Inspetoria projetaram o seu prédio 
              com apenas 1 switch de 24 portas (TL-SG3428MP) com 4 slots SFP, onde todas as portas locais de cobre já estão consumidas pelas mesas 
              de operação e câmeras próprias, sem nenhuma porta SFP dedicada ou dimensionamento de agregação para receber as fibras da Pera!
            </div>
          </div>
        </section>

        <!-- 03. PORTARIA TP -->
        <section id="sec-portaria" class="audit-section">
          <div class="section-header">
            <div class="section-header-left">
              <span class="section-number">03</span>
              <h2 class="section-title">Auditoria Individual: Portaria TP</h2>
            </div>
            <span class="badge success"><span class="badge-dot"></span>Nota Técnica: 8.8 / 10</span>
          </div>

          <p class="section-intro">
            <strong>Autores:</strong> Taino Samuel Lima Ribeiro e Victor Eduard Rodrigues Cabral.<br>
            <strong>Escopo Auditado:</strong> Guarita de acesso principal, catracas de pedestres, recepção, videomonitoramento de fachadas e interface de uplink com o campus.
          </p>

          <div class="sector-grid-metrics">
            <div class="metric-box">
              <div class="metric-box-title">Orçamento Local</div>
              <div class="metric-box-val" style="color: var(--accent-emerald);">R$ 29.347,83</div>
            </div>
            <div class="metric-box">
              <div class="metric-box-title">Enlace Campus</div>
              <div class="metric-box-val" style="color: var(--accent-cyan);">R$ 3.634,00</div>
            </div>
            <div class="metric-box">
              <div class="metric-box-title">Dispositivos PKT</div>
              <div class="metric-box-val">15 nodes / 13 links</div>
            </div>
            <div class="metric-box">
              <div class="metric-box-title">Metodologia</div>
              <div class="metric-box-val" style="color: var(--accent-indigo);">PPDIOO / TIA-568</div>
            </div>
          </div>

          <div class="two-col">
            <div class="pro-con-box pro-box">
              <h4>✅ Pontos Fortes e Destaques Técnicos</h4>
              <ul class="audit-list">
                <li><strong>Excelente Rigor Metodológico:</strong> Estruturado segundo o ciclo de vida Cisco PPDIOO (Prepare, Plan, Design, Implement, Operate, Optimize).</li>
                <li><strong>As-Built e Memória de Cálculo Físico:</strong> Planta de encaminhamento detalhada com <code>Memoria-de-cabos.csv</code> especificando cada tomada, patch panel e eletroduto com cotas reais.</li>
                <li><strong>100% de Aderência aos Requisitos do Enunciado:</strong> Contemplou 1 PC recepção, 1 Telefone IP, 1 Impressora de rede, 1 Catraca RFID, 2 Câmeras internas, 2 Câmeras externas (Fachadas A e B) e 1 Access Point Wi-Fi.</li>
                <li><strong>Separação Orçamentária Clara:</strong> Isolou com precisão o que é investimento local da portaria do que é parcela de infraestrutura compartilhada (transceivers e fibra do enlace).</li>
                <li><strong>Simulação Packet Tracer Validada:</strong> Arquivo <code>Portaria-TP-Taino-Victor.pkt</code> abre sem falhas, com VLANs configuradas e portas mapeadas.</li>
              </ul>
            </div>
            <div class="pro-con-box con-box">
              <h4>❌ Pontos de Atenção e Falhas Identificadas</h4>
              <ul class="audit-list">
                <li><strong>Desperdício de Espaço IPv4:</strong> Utilizou máscaras <code>/24</code> (254 hosts disponíveis) para redes que possuem apenas 1 dispositivo (ex: Catraca na VLAN 40, PC e Impressora na VLAN 10).</li>
                <li><strong>Colisão de IP com o Complexo:</strong> Adotou as faixas <code>192.168.10.0</code> a <code>192.168.50.0</code> que entram em conflito com Silo, Inspetoria e Pera.</li>
                <li><strong>Premissa de Núcleo Provisória:</strong> Assumiu uma sub-rede de trânsito <code>192.168.200.0/24</code> sem validação prévia com o roteador de campus (que no Prédio ADM usou <code>10.255.20.0/30</code>).</li>
                <li><strong>Limitação do Switch Comercial:</strong> O switch previsto (24 portas PoE) é comercial de escritório; para o ambiente de portaria com poeira externa e umidade marinha, recomenda-se proteção adicional contra surtos na entrada dos cabos das câmeras externas.</li>
              </ul>
            </div>
          </div>
        </section>

        <!-- 04. PRÉDIO ADMINISTRATIVO -->
        <section id="sec-adm" class="audit-section">
          <div class="section-header">
            <div class="section-header-left">
              <span class="section-number">04</span>
              <h2 class="section-title">Auditoria Individual: Prédio Administrativo</h2>
            </div>
            <span class="badge success"><span class="badge-dot"></span>Nota Técnica: 8.5 / 10</span>
          </div>

          <p class="section-intro">
            <strong>Autores:</strong> Gabriel Ordonez e Higor Gabriel.<br>
            <strong>Escopo Auditado:</strong> Pavimento corporativo completo, sala técnica/CPD, 40 postos de trabalho, 4 salas de conferência, datacenter local (3 servidores + 1 storage), Wi-Fi corporativo/visitantes e telefonia VoIP.
          </p>

          <div class="sector-grid-metrics">
            <div class="metric-box">
              <div class="metric-box-title">Orçamento Global</div>
              <div class="metric-box-val" style="color: var(--accent-amber);">R$ 708.624,00</div>
            </div>
            <div class="metric-box">
              <div class="metric-box-title">Rede + Servidores</div>
              <div class="metric-box-val" style="color: var(--accent-cyan);">R$ 474.124,00</div>
            </div>
            <div class="metric-box">
              <div class="metric-box-title">Dispositivos PKT</div>
              <div class="metric-box-val">36 nodes / 33 links</div>
            </div>
            <div class="metric-box">
              <div class="metric-box-title">Testes Automatizados</div>
              <div class="metric-box-val" style="color: var(--accent-emerald);">172 regras OK</div>
            </div>
          </div>

          <div class="two-col">
            <div class="pro-con-box pro-box">
              <h4>✅ Pontos Fortes e Destaques Técnicos</h4>
              <ul class="audit-list">
                <li><strong>Arquitetura Lógica Enterprise Exemplar:</strong> Única equipe que utilizou corretamente a classe privada corporativa <code>10.20.0.0/16</code> com sub-redes VLSM customizadas (VLANs 110 a 200).</li>
                <li><strong>Isolamento Físico e Lógico do Storage (SAN/NAS):</strong> A VLAN 180 (Storage) foi mantida estritamente em Camada 2, sem gateway e sem subinterface no roteador, impedindo vazamento de tráfego de dados para a rede IP comum.</li>
                <li><strong>Validação Exaustiva no Packet Tracer:</strong> Criação de scripts automatizados de checagem com 172 regras verificadas, matriz de testes manuais e representação de servidores virtualizados (VM-DNS, VM-NVR, VM-RADIUS).</li>
                <li><strong>Topologia Hierárquica Estrela:</strong> Gateway 1941 + Core Layer 3 3560-24PS interligado a 3 switches de acesso de borda por enlaces gigabit dedicados.</li>
              </ul>
            </div>
            <div class="con-box pro-con-box">
              <h4>❌ Pontos de Atenção e Falhas Identificadas</h4>
              <ul class="audit-list">
                <li><strong>Hipertrofia Orçamentária por Inclusão de Terminais:</strong> O orçamento explodiu para R$ 708.624,00 porque os autores orçaram R$ 234.500,00 em notebooks, desktops e periféricos pessoais, itens que pertencem ao capex de TI corporativa e não à infraestrutura de redes.</li>
                <li><strong>Isolamento Fictício em Relação ao Campus:</strong> A simulação do Packet Tracer criou um <code>RTR-CAMPUS</code> conectado a uma Internet fictícia (<code>203.0.113.53</code>), mas não previu as rotas estáticas ou dinâmicas para alcançar a Pera, Silo, Portaria e Inspetoria.</li>
                <li><strong>Ociosidade de Portas Core L3:</strong> Adotou modelo 3560-24PS (24 portas PoE) para Core e também para todos os Switches de Acesso, quando o Core poderia ser um switch de agregação com mais portas SFP para receber o campus.</li>
              </ul>
            </div>
          </div>
        </section>

        <!-- 05. PERA FERROVIÁRIA -->
        <section id="sec-pera" class="audit-section">
          <div class="section-header">
            <div class="section-header-left">
              <span class="section-number">05</span>
              <h2 class="section-title">Auditoria Individual: Pera Ferroviária</h2>
            </div>
            <span class="badge warning"><span class="badge-dot"></span>Nota Técnica: 7.2 / 10</span>
          </div>

          <p class="section-intro">
            <strong>Autores:</strong> João Lucas Magalhães Gomes e Jaylon Coelho Saldanha.<br>
            <strong>Escopo Auditado:</strong> Pátio ferroviário de manobra e pesagem (600 m x 30 m), 2 balanças ferroviárias automatizadas e 10 câmeras IP PoE+ para videomonitoramento do CCO.
          </p>

          <div class="sector-grid-metrics">
            <div class="metric-box">
              <div class="metric-box-title">Orçamento Global</div>
              <div class="metric-box-val" style="color: var(--accent-emerald);">R$ 125.114,00</div>
            </div>
            <div class="metric-box">
              <div class="metric-box-title">Extensão da Via</div>
              <div class="metric-box-val" style="color: var(--accent-cyan);">600 metros</div>
            </div>
            <div class="metric-box">
              <div class="metric-box-title">Meio de Transmissão</div>
              <div class="metric-box-val">Fibra Monomodo OS2</div>
            </div>
            <div class="metric-box">
              <div class="metric-box-title">Proteção Física</div>
              <div class="metric-box-val" style="color: var(--accent-amber);">IP66 / IP67 Industrial</div>
            </div>
          </div>

          <div class="two-col">
            <div class="pro-con-box pro-box">
              <h4>✅ Pontos Fortes e Destaques Técnicos</h4>
              <ul class="audit-list">
                <li><strong>Excelente Consciência de Ambiente Industrial Severo:</strong> Reconheceu os 600m de distância como impeditivo para cabo metálico (limite de 90m da TIA-568) e adotou Fibra Óptica Monomodo OS2.</li>
                <li><strong>Imunidade Eletromagnética (EMI):</strong> Uso de fibra óptica protege o backbone contra ruído elétrico dos motores diesel-elétricos e sistemas de tração das locomotivas da Vale/EFC.</li>
                <li><strong>Equipamentos Rugerizados Outdoor:</strong> Especificação de caixas herméticas IP66 e switches industriais PoE+ com suporte a temperaturas elevadas e vibração mecânica contínua.</li>
              </ul>
            </div>
            <div class="con-box pro-con-box">
              <h4>❌ Pontos de Atenção e Falhas Identificadas</h4>
              <ul class="audit-list">
                <li><strong>Inconsistência Grave na Agregação com a Inspetoria:</strong> O relatório afirma categoricamente que as fibras chegam ao <em>"Switch Central do CCO na Inspetoria"</em>, mas o projeto da Inspetoria não previu esse switch nem as interfaces ópticas.</li>
                <li><strong>Colisão de Endereçamento IP:</strong> Uso de <code>192.168.20.0/24</code> (VLAN 20) e <code>192.168.30.0/24</code> (VLAN 30), colidindo diretamente com Portaria e Inspetoria.</li>
                <li><strong>Falta de Detalhamento no As-Built de Campo:</strong> Não há especificação de caixas de passagem subterrâneas, profundidade de valas conforme NBR/TIA-569 (mínimo 60-80cm sob leito ferroviário com fita sinalizadora) nem caixas de emenda óptica.</li>
              </ul>
            </div>
          </div>
        </section>

        <!-- 06. PRÉDIO INSPETORIA & CCO -->
        <section id="sec-inspetoria" class="audit-section">
          <div class="section-header">
            <div class="section-header-left">
              <span class="section-number">06</span>
              <h2 class="section-title">Auditoria Individual: Inspetoria | CCO Berço 098</h2>
            </div>
            <span class="badge danger"><span class="badge-dot"></span>Nota Técnica: 5.2 / 10</span>
          </div>

          <p class="section-intro">
            <strong>Autores:</strong> Mateus Dantas e Renan Pires.<br>
            <strong>Escopo Auditado:</strong> Prédio da Inspetoria Portuária no Berço 098, abrigando o Centro de Controle Operacional (CCO) marítimo, 8 consoles de operadores, sala de automação e 10 câmeras.
          </p>

          <div class="sector-grid-metrics">
            <div class="metric-box">
              <div class="metric-box-title">Orçamento Global</div>
              <div class="metric-box-val" style="color: var(--accent-rose);">R$ 18.891,32</div>
            </div>
            <div class="metric-box">
              <div class="metric-box-title">Tamanho do Relatório</div>
              <div class="metric-box-val" style="color: var(--accent-amber);">5 páginas (Raso)</div>
            </div>
            <div class="metric-box">
              <div class="metric-box-title">Switches Previstos</div>
              <div class="metric-box-val">1x 24p TP-Link</div>
            </div>
            <div class="metric-box">
              <div class="metric-box-title">Capacidade CCO</div>
              <div class="metric-box-val" style="color: var(--accent-rose);">Insuficiente</div>
            </div>
          </div>

          <div class="two-col">
            <div class="pro-con-box pro-box">
              <h4>✅ Pontos Fortes e Destaques Técnicos</h4>
              <ul class="audit-list">
                <li><strong>Atendimento Numérico dos Dispositivos:</strong> Alocou os 8 consoles de operação com telefonia IP, 1 posto na sala de equipamentos, 2 na automação, 2 câmeras internas e 8 externas.</li>
                <li><strong>Equipamentos Reais de Custo Acessível:</strong> Roteador TP-Link ER7206, Switch PoE+ TL-SG3428MP e Telefones TIP 125i com links de compra válidos.</li>
              </ul>
            </div>
            <div class="con-box pro-con-box">
              <h4>❌ Falhas Críticas e Omissões Graves</h4>
              <ul class="audit-list">
                <li><strong>Incompatibilidade Funcional com o CCO:</strong> Um Centro de Controle Operacional Portuário exige redundância de energia, switch de agregação com portas ópticas, servidores NVR e videowall. O projeto instalou um mini rack de parede 12U e um nobreak comum de 1200VA, incapaz de suportar a missão crítica do berço 098.</li>
                <li><strong>Premissa de Custo Irrealista:</strong> Declarou que computadores, servidores NVR e câmeras "já existiam" no porto para baratear o projeto, não apresentando o dimensionamento do sistema de CFTV.</li>
                <li><strong>Ausência de Cálculo de Cabeamento:</strong> Estimou genericamente "2 caixas de cabo Cat6 (610m)" sem memória de cálculo nem trajetos de eletrocalhas.</li>
                <li><strong>Colisão Total de Sub-redes IP:</strong> Mapeou VLAN 10 (192.168.10.0/24), VLAN 20 (192.168.20.0/24) e VLAN 40 (192.168.40.0/24), impossibilitando comunicação direta com o ADM e outros prédios.</li>
              </ul>
            </div>
          </div>
        </section>

        <!-- 07. SILO DE GRÃOS -->
        <section id="sec-silo" class="audit-section">
          <div class="section-header">
            <div class="section-header-left">
              <span class="section-number">07</span>
              <h2 class="section-title">Auditoria Individual: Silo de Grãos</h2>
            </div>
            <span class="badge danger"><span class="badge-dot"></span>Nota Técnica: 5.0 / 10</span>
          </div>

          <p class="section-intro">
            <strong>Autores:</strong> Asafe e Lucas.<br>
            <strong>Escopo Auditado:</strong> Estrutura circular de concreto e aço (Raio 25m, Altura 30m), monitoramento interno/externo, controle de acesso e sensoriamento IoT de grãos.
          </p>

          <div class="sector-grid-metrics">
            <div class="metric-box">
              <div class="metric-box-title">Orçamento Global</div>
              <div class="metric-box-val" style="color: var(--accent-rose);">R$ 16.720,90</div>
            </div>
            <div class="metric-box">
              <div class="metric-box-title">Dimensões da Estrutura</div>
              <div class="metric-box-val">R=25m | H=30m</div>
            </div>
            <div class="metric-box">
              <div class="metric-box-title">Risco Normativo</div>
              <div class="metric-box-val" style="color: var(--accent-rose);">ATEX / NFPA 652</div>
            </div>
            <div class="metric-box">
              <div class="metric-box-title">Comprimento Cabos</div>
              <div class="metric-box-val" style="color: var(--accent-amber);">Risco Limite 90m</div>
            </div>
          </div>

          <div class="two-col">
            <div class="pro-con-box pro-box">
              <h4>✅ Pontos Fortes e Destaques Técnicos</h4>
              <ul class="audit-list">
                <li><strong>Inclusão de Gateway IoT Industrial:</strong> Previsão de gateway Modbus/LoRaWAN para integração de telemetria de temperatura e umidade da massa de grãos com a rede TCP/IP.</li>
                <li><strong>Conexão Óptica ao Backbone:</strong> Módulos SFP monomodo previstos para isolamento galvânico contra surtos atmosféricos em estruturas metálicas altas.</li>
              </ul>
            </div>
            <div class="con-box pro-con-box">
              <h4>❌ Falhas Críticas e Omissões Graves</h4>
              <ul class="audit-list">
                <li><strong>Omissão Crítica de Atmosfera Explosiva (NR-20 / IECEx / ATEX):</strong> Silos de grãos têm alta concentração de poeira orgânica em suspensão (amido de soja/milho), gerando atmosfera com risco de explosão classe Ex. Todos os eletrodutos, conectores, câmeras e APs devem ser à prova de explosão (Ex-d / Ex-t). O projeto usou materiais de escritório plástico comum!</li>
                <li><strong>Risco de Violação do Limite de 90 Metros da TIA-568:</strong> Com raio de 25m (diâmetro 50m) e altura de 30m, um cabo saindo do rack na portaria até o topo superior do silo percorre: 25m horizontal + 30m vertical + curvas/curvaturas = 70 a 85m. Se não houver shaft central, o lance metálico ultrapassa facilmente os 90m permitidos!</li>
                <li><strong>Colisão Total de Endereçamento IP:</strong> Repetiu as redes <code>192.168.10.0/24</code>, <code>192.168.50.0/24</code>, <code>192.168.60.0/24</code> já utilizadas pelos outros setores.</li>
              </ul>
            </div>
          </div>
        </section>

        <!-- 08. CONFORMIDADE COM AS AULAS (UAs) -->
        <section id="sec-uas" class="audit-section">
          <div class="section-header">
            <div class="section-header-left">
              <span class="section-number">08</span>
              <h2 class="section-title">Auditoria Frente ao Conteúdo das Aulas (UAs)</h2>
            </div>
            <span class="badge info"><span class="badge-dot"></span>Cruzamento Pedagógico UNDB</span>
          </div>

          <p class="section-intro">
            Avaliação comparativa entre os conceitos formais ministrados pelo <strong>Prof. Me. Arlley Costa</strong> nas Unidades de Aprendizagem (UAs) 
            e o que foi efetivamente aplicado nos projetos pelos alunos.
          </p>

          <div class="table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Tópico / Aula Ministrada</th>
                  <th>Conceito / Norma Ensinada</th>
                  <th>Aplicação pelos Alunos</th>
                  <th>Diagnóstico da Auditoria</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>UA I - Subsistemas de Cabeamento</strong></td>
                  <td>6 Subsistemas (Área de Trabalho, Cabeamento Horizontal, TR, Backbone, ER, EF). Limite de 90m + 10m patch cords.</td>
                  <td>Portaria e ADM detalharam os 6 subsistemas. Silo e Inspetoria ignoraram a distinção entre TR e ER.</td>
                  <td><span class="badge warning">Parcial (2 de 5 cumpriram)</span></td>
                </tr>
                <tr>
                  <td><strong>UA I - Normas Técnicas</strong></td>
                  <td>ANSI/TIA-568-D, ISO/IEC 11801, ABNT NBR 14565, TIA-606 (identificação de cabos), TIA-569 (caminhos).</td>
                  <td>Portaria citou TIA-606 e NBR 14565. Demais grupos citaram genericamente ou omitiram normas.</td>
                  <td><span class="badge warning">Apenas Portaria cumpriu TIA-606</span></td>
                </tr>
                <tr>
                  <td><strong>UA I - Fibras Ópticas</strong></td>
                  <td>Monomodo SMF (núcleo 9µm, laser, campus) vs Multimodo MMF (50µm OM3/OM4, prédio até 550m).</td>
                  <td>Pera, Silo e Portaria acertaram ao adotar Monomodo OS2 para interligações externas de campus.</td>
                  <td><span class="badge success">Conforme (Boa escolha técnica)</span></td>
                </tr>
                <tr>
                  <td><strong>UA II - Sub-redes e VLSM</strong></td>
                  <td>Uso de VLSM para otimizar blocos IP, evitar desperdício de endereços e permitir sumarização de rotas.</td>
                  <td>Prédio ADM aplicou VLSM com rigor (/24, /27, /28). Os outros 4 grupos usaram apenas /24 fixo (FLSM rudimentar).</td>
                  <td><span class="badge danger">Grave desperdício de IPv4</span></td>
                </tr>
                <tr>
                  <td><strong>UA II - RFC 1918 (IPs Privados)</strong></td>
                  <td>Classes privadas 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16. Necessidade de plano corporativo unificado.</td>
                  <td>ADM usou 10.20.0.0/16; todos os outros usaram 192.168.x.x gerando sobreposição em massa.</td>
                  <td><span class="badge danger">Incompatibilidade Fatal</span></td>
                </tr>
                <tr>
                  <td><strong>UA III - Modelo OSI e PDUs</strong></td>
                  <td>Encapsulamento (Bits -> Quadros -> Pacotes -> Segmentos -> Dados). Equipamentos L1, L2 e L3.</td>
                  <td>ADM isolou VLAN 180 em Camada 2 para Storage (ótimo). Pera e Inspetoria misturaram funções de L2 e L3.</td>
                  <td><span class="badge success">ADM demonstrou domínio OSI</span></td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- 09. ARQUITETURA DE REFERÊNCIA CORRIGIDA -->
        <section id="sec-arquitetura" class="audit-section">
          <div class="section-header">
            <div class="section-header-left">
              <span class="section-number">09</span>
              <h2 class="section-title">Arquitetura de Referência Corrigida (Engenharia Sem Gambiarras)</h2>
            </div>
            <span class="badge success"><span class="badge-dot"></span>Solução Definitiva Unificada</span>
          </div>

          <p class="section-intro">
            Para sanar definitivamente todas as falhas encontradas e fornecer ao novo Terminal Portuário uma infraestrutura profissional, 
            robusta e escalável para os próximos 15 anos, apresentamos a <strong>Arquitetura Unificada de Campus</strong> com endereçamento 
            corporativo VLSM sem colisões e anel óptico redundante.
          </p>

          <!-- SVG TOPOLOGIA CORRIGIDA -->
          <div class="diagram-container">
            <svg width="100%" height="340" viewBox="0 0 950 340" xmlns="http://www.w3.org/2000/svg" style="max-width: 950px; font-family: 'Inter', sans-serif;">
              <defs>
                <linearGradient id="coreGrad" x1="0" y1="0" x2="1" y2="1">
                  <stop offset="0%" stop-color="#0284c7"/>
                  <stop offset="100%" stop-color="#0369a1"/>
                </linearGradient>
                <linearGradient id="nodeGrad" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stop-color="#1e293b"/>
                  <stop offset="100%" stop-color="#0f172a"/>
                </linearGradient>
              </defs>

              <!-- Backbone Ring (Anel Óptico Monomodo OS2) -->
              <ellipse cx="475" cy="170" rx="360" ry="110" fill="none" stroke="#06b6d4" stroke-width="3" stroke-dasharray="8,6"/>
              <text x="475" y="45" text-anchor="middle" fill="#22d3ee" font-weight="700" font-size="12">BACKBONE ÓPTICO REDUNDANTE EM ANEL (10 Gbps SMF OS2)</text>

              <!-- Core Central (Datacenter no Prédio ADM) -->
              <rect x="375" y="125" width="200" height="90" rx="10" fill="url(#coreGrad)" stroke="#38bdf8" stroke-width="2"/>
              <text x="475" y="150" text-anchor="middle" fill="#ffffff" font-weight="800" font-size="14">CORE DATACENTER</text>
              <text x="475" y="170" text-anchor="middle" fill="#e0f2fe" font-weight="600" font-size="11">Prédio Administrativo</text>
              <text x="475" y="190" text-anchor="middle" fill="#bae6fd" font-size="10" font-family="'JetBrains Mono', monospace">Sub-rede: 10.100.0.0/20</text>

              <!-- Node 1: Portaria TP -->
              <rect x="60" y="125" width="170" height="85" rx="8" fill="url(#nodeGrad)" stroke="#10b981" stroke-width="1.5"/>
              <text x="145" y="148" text-anchor="middle" fill="#34d399" font-weight="700" font-size="12">Portaria TP</text>
              <text x="145" y="166" text-anchor="middle" fill="#94a3b8" font-size="10.5">Switch PoE + Trânsito</text>
              <text x="145" y="185" text-anchor="middle" fill="#6ee7b7" font-size="10" font-family="'JetBrains Mono', monospace">10.100.28.0/23</text>

              <!-- Node 2: Pera Ferroviária -->
              <rect x="180" y="240" width="180" height="85" rx="8" fill="url(#nodeGrad)" stroke="#10b981" stroke-width="1.5"/>
              <text x="270" y="263" text-anchor="middle" fill="#34d399" font-weight="700" font-size="12">Pera Ferroviária</text>
              <text x="270" y="281" text-anchor="middle" fill="#94a3b8" font-size="10.5">Switches Ind. IP67</text>
              <text x="270" y="300" text-anchor="middle" fill="#6ee7b7" font-size="10" font-family="'JetBrains Mono', monospace">10.100.16.0/21</text>

              <!-- Node 3: Silo de Grãos -->
              <rect x="590" y="240" width="180" height="85" rx="8" fill="url(#nodeGrad)" stroke="#10b981" stroke-width="1.5"/>
              <text x="680" y="263" text-anchor="middle" fill="#34d399" font-weight="700" font-size="12">Silo de Grãos</text>
              <text x="680" y="281" text-anchor="middle" fill="#94a3b8" font-size="10.5">Rede Ex / ATEX + IoT</text>
              <text x="680" y="300" text-anchor="middle" fill="#6ee7b7" font-size="10" font-family="'JetBrains Mono', monospace">10.100.24.0/22</text>

              <!-- Node 4: Inspetoria e CCO Pier -->
              <rect x="720" y="125" width="180" height="85" rx="8" fill="url(#nodeGrad)" stroke="#10b981" stroke-width="1.5"/>
              <text x="810" y="148" text-anchor="middle" fill="#34d399" font-weight="700" font-size="12">Inspetoria / CCO</text>
              <text x="810" y="166" text-anchor="middle" fill="#94a3b8" font-size="10.5">Switch Agregação Berço 098</text>
              <text x="810" y="185" text-anchor="middle" fill="#6ee7b7" font-size="10" font-family="'JetBrains Mono', monospace">10.100.32.0/21</text>

              <!-- Physical Links -->
              <line x1="230" y1="167" x2="375" y2="167" stroke="#38bdf8" stroke-width="2"/>
              <line x1="575" y1="167" x2="720" y2="167" stroke="#38bdf8" stroke-width="2"/>
              <line x1="330" y1="240" x2="415" y2="215" stroke="#38bdf8" stroke-width="2"/>
              <line x1="620" y1="240" x2="535" y2="215" stroke="#38bdf8" stroke-width="2"/>
            </svg>
            <div class="diagram-caption">Figura 2: Arquitetura Corrigida em Estrela Hierárquica Estendida com Anel Óptico de 10 Gbps (Backbone Campus).</div>
          </div>

          <h3 style="font-size: 1.1rem; margin: 24px 0 12px; color: var(--text-primary);">Plano Mestre Unificado de Endereçamento IPv4 (Bloco 10.100.0.0/16)</h3>
          <p style="font-size: 13.5px; color: var(--text-secondary); margin-bottom: 14px;">
            Elimina 100% dos conflitos de IP, garante segmentação de segurança por setor e serviço, e permite sumarização de rotas perfeita no Core.
          </p>
          <div class="table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Setor / Unidade</th>
                  <th>VLAN ID</th>
                  <th>Nome do Serviço</th>
                  <th>Sub-rede IPv4</th>
                  <th>Máscara</th>
                  <th>Gateway Padrão</th>
                  <th>Capacidade Hosts</th>
                </tr>
              </thead>
              <tbody>
                <!-- ADM -->
                <tr>
                  <td rowspan="4"><strong>Prédio Administrativo</strong><br><span style="font-size: 11px; color: var(--text-muted);">Bloco: 10.100.0.0/20</span></td>
                  <td><code>VLAN 110</code></td>
                  <td>Staff & Diretoria</td>
                  <td><code>10.100.1.0/24</code></td>
                  <td><code>255.255.255.0</code></td>
                  <td><code>10.100.1.1</code></td>
                  <td>254 hosts</td>
                </tr>
                <tr>
                  <td><code>VLAN 130</code></td>
                  <td>Salas Reunião / VC</td>
                  <td><code>10.100.2.0/24</code></td>
                  <td><code>255.255.255.0</code></td>
                  <td><code>10.100.2.1</code></td>
                  <td>254 hosts</td>
                </tr>
                <tr>
                  <td><code>VLAN 160</code></td>
                  <td>CFTV & Acesso ADM</td>
                  <td><code>10.100.6.0/24</code></td>
                  <td><code>255.255.255.0</code></td>
                  <td><code>10.100.6.1</code></td>
                  <td>254 hosts</td>
                </tr>
                <tr>
                  <td><code>VLAN 180</code></td>
                  <td>Storage SAN/NAS (Sem GW)</td>
                  <td><code>10.100.8.0/28</code></td>
                  <td><code>255.255.255.240</code></td>
                  <td><em>Isolado L2</em></td>
                  <td>14 hosts</td>
                </tr>

                <!-- PERA -->
                <tr>
                  <td rowspan="3"><strong>Pera Ferroviária</strong><br><span style="font-size: 11px; color: var(--text-muted);">Bloco: 10.100.16.0/21</span></td>
                  <td><code>VLAN 210</code></td>
                  <td>CFTV Ferroviário (10 cams)</td>
                  <td><code>10.100.16.0/24</code></td>
                  <td><code>255.255.255.0</code></td>
                  <td><code>10.100.16.1</code></td>
                  <td>254 hosts</td>
                </tr>
                <tr>
                  <td><code>VLAN 220</code></td>
                  <td>Automação Balanças</td>
                  <td><code>10.100.17.0/28</code></td>
                  <td><code>255.255.255.240</code></td>
                  <td><code>10.100.17.1</code></td>
                  <td>14 hosts</td>
                </tr>
                <tr>
                  <td><code>VLAN 299</code></td>
                  <td>Gerência Sw. Industriais</td>
                  <td><code>10.100.23.0/28</code></td>
                  <td><code>255.255.255.240</code></td>
                  <td><code>10.100.23.1</code></td>
                  <td>14 hosts</td>
                </tr>

                <!-- SILO -->
                <tr>
                  <td rowspan="3"><strong>Silo de Grãos</strong><br><span style="font-size: 11px; color: var(--text-muted);">Bloco: 10.100.24.0/22</span></td>
                  <td><code>VLAN 310</code></td>
                  <td>CFTV Silo (5 cams)</td>
                  <td><code>10.100.24.0/24</code></td>
                  <td><code>255.255.255.0</code></td>
                  <td><code>10.100.24.1</code></td>
                  <td>254 hosts</td>
                </tr>
                <tr>
                  <td><code>VLAN 320</code></td>
                  <td>Sensores & Gateways IoT</td>
                  <td><code>10.100.25.0/24</code></td>
                  <td><code>255.255.255.0</code></td>
                  <td><code>10.100.25.1</code></td>
                  <td>254 hosts</td>
                </tr>
                <tr>
                  <td><code>VLAN 330</code></td>
                  <td>Controle Acesso & Portaria</td>
                  <td><code>10.100.26.0/28</code></td>
                  <td><code>255.255.255.240</code></td>
                  <td><code>10.100.26.1</code></td>
                  <td>14 hosts</td>
                </tr>

                <!-- PORTARIA -->
                <tr>
                  <td rowspan="3"><strong>Portaria TP</strong><br><span style="font-size: 11px; color: var(--text-muted);">Bloco: 10.100.28.0/23</span></td>
                  <td><code>VLAN 410</code></td>
                  <td>Recepção (PC / Impressora)</td>
                  <td><code>10.100.28.0/28</code></td>
                  <td><code>255.255.255.240</code></td>
                  <td><code>10.100.28.1</code></td>
                  <td>14 hosts</td>
                </tr>
                <tr>
                  <td><code>VLAN 420</code></td>
                  <td>CFTV Portaria (4 cams)</td>
                  <td><code>10.100.28.16/28</code></td>
                  <td><code>255.255.255.240</code></td>
                  <td><code>10.100.28.17</code></td>
                  <td>14 hosts</td>
                </tr>
                <tr>
                  <td><code>VLAN 430</code></td>
                  <td>Catracas de Pedestres</td>
                  <td><code>10.100.28.32/28</code></td>
                  <td><code>255.255.255.240</code></td>
                  <td><code>10.100.28.33</code></td>
                  <td>14 hosts</td>
                </tr>

                <!-- INSPETORIA / CCO -->
                <tr>
                  <td rowspan="3"><strong>Inspetoria & CCO</strong><br><span style="font-size: 11px; color: var(--text-muted);">Bloco: 10.100.32.0/21</span></td>
                  <td><code>VLAN 510</code></td>
                  <td>Consoles de Operação CCO</td>
                  <td><code>10.100.32.0/24</code></td>
                  <td><code>255.255.255.0</code></td>
                  <td><code>10.100.32.1</code></td>
                  <td>254 hosts</td>
                </tr>
                <tr>
                  <td><code>VLAN 520</code></td>
                  <td>CFTV Marítimo (10 cams)</td>
                  <td><code>10.100.33.0/24</code></td>
                  <td><code>255.255.255.0</code></td>
                  <td><code>10.100.33.1</code></td>
                  <td>254 hosts</td>
                </tr>
                <tr>
                  <td><code>VLAN 530</code></td>
                  <td>Telefonia VoIP Operacional</td>
                  <td><code>10.100.34.0/24</code></td>
                  <td><code>255.255.255.0</code></td>
                  <td><code>10.100.34.1</code></td>
                  <td>254 hosts</td>
                </tr>

                <!-- TRÂNSITO -->
                <tr>
                  <td><strong>Backbone Campus</strong></td>
                  <td><code>VLAN 900</code></td>
                  <td>Enlaces Roteados Ponto a Ponto</td>
                  <td><code>10.100.254.0/24</code></td>
                  <td><code>255.255.255.252</code> (/30)</td>
                  <td><em>Sub-redes /30</em></td>
                  <td>64 enlaces /30</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h3 style="font-size: 1.1rem; margin: 28px 0 12px; color: var(--text-primary);">Consolidação Orçamentária Equalizada (Visão Realista sem Distorções)</h3>
          <p style="font-size: 13.5px; color: var(--text-secondary); margin-bottom: 14px;">
            Abaixo, todos os orçamentos foram equalizados: separamos a <strong>Infraestrutura Real de Redes</strong> (ativos, passivos, fibra, racks, nobreaks e servidores) 
            dos <strong>Terminais Pessoais de Usuários</strong> (notebooks e computadores que a equipe do ADM orçou, mas as outras duplas não).
          </p>

          <div class="table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Setor</th>
                  <th>Passivos & Cabeamento</th>
                  <th>Ativos de Rede (Switches/APs/Routers)</th>
                  <th>Energia & Infra (Racks/Nobreaks)</th>
                  <th>Servidores & Storage</th>
                  <th>Subtotal Infraestrutura</th>
                  <th>Terminais de Usuários</th>
                  <th>Total Geral Real</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Portaria TP</strong></td>
                  <td>R$ 10.450,00</td>
                  <td>R$ 9.897,83</td>
                  <td>R$ 9.000,00</td>
                  <td>-</td>
                  <td><strong>R$ 29.347,83</strong></td>
                  <td>R$ 3.634,00 (PC/Imp)</td>
                  <td>R$ 32.981,83</td>
                </tr>
                <tr>
                  <td><strong>Prédio Administrativo</strong></td>
                  <td>R$ 48.120,00</td>
                  <td>R$ 48.100,00</td>
                  <td>R$ 52.100,00</td>
                  <td>R$ 154.000,00</td>
                  <td><strong>R$ 302.320,00</strong></td>
                  <td>R$ 234.500,00</td>
                  <td>R$ 536.820,00*</td>
                </tr>
                <tr>
                  <td><strong>Pera Ferroviária</strong></td>
                  <td>R$ 42.500,00</td>
                  <td>R$ 52.440,00</td>
                  <td>R$ 18.800,00</td>
                  <td>-</td>
                  <td><strong>R$ 113.740,00</strong></td>
                  <td>-</td>
                  <td>R$ 125.114,00**</td>
                </tr>
                <tr>
                  <td><strong>Inspetoria | CCO (Ajustado)</strong></td>
                  <td>R$ 14.800,00</td>
                  <td>R$ 38.500,00***</td>
                  <td>R$ 24.000,00</td>
                  <td>R$ 45.000,00 (NVR/Srv)</td>
                  <td><strong>R$ 122.300,00</strong></td>
                  <td>R$ 48.000,00 (8 Consoles)</td>
                  <td>R$ 170.300,00</td>
                </tr>
                <tr>
                  <td><strong>Silo de Grãos (Ajustado Ex)</strong></td>
                  <td>R$ 22.400,00****</td>
                  <td>R$ 14.500,00</td>
                  <td>R$ 12.000,00</td>
                  <td>R$ 8.000,00 (GW IoT)</td>
                  <td><strong>R$ 56.900,00</strong></td>
                  <td>-</td>
                  <td>R$ 56.900,00</td>
                </tr>
                <tr style="background: rgba(6, 182, 212, 0.08); font-weight: 700;">
                  <td>TOTAL COMPLEXO PORTUÁRIO</td>
                  <td>R$ 138.270,00</td>
                  <td>R$ 163.437,83</td>
                  <td>R$ 115.900,00</td>
                  <td>R$ 207.000,00</td>
                  <td style="color: var(--accent-emerald);">R$ 624.607,83</td>
                  <td>R$ 286.134,00</td>
                  <td style="color: var(--accent-cyan);">R$ 922.115,83</td>
                </tr>
              </tbody>
            </table>
          </div>
          <p style="font-size: 12px; color: var(--text-muted);">
            * Sem os 20% de contingência abstrata aplicada sobre todo o contrato.<br>
            ** Inclui 10% de margem de segurança física para obra ferroviária.<br>
            *** Ajustado para incluir Switch Core de Agregação SFP no CCO, Servidor NVR industrial e consoles multi-telas de operação portuária.<br>
            **** Ajustado para incluir tubulações metálicas industriais galvanizadas e invólucros com vedação à prova de poeira combustível (Ex-d).
          </p>
        </section>

        <!-- 10. GUIA PARA APRESENTAÇÃO E BANCA FINAL -->
        <section id="sec-banca" class="audit-section">
          <div class="section-header">
            <div class="section-header-left">
              <span class="section-number">10</span>
              <h2 class="section-title">Guia Prático para Apresentação Perante a Banca</h2>
            </div>
            <span class="badge success"><span class="badge-dot"></span>Defesa Nota 10 com o Prof. Arlley</span>
          </div>

          <p class="section-intro">
            Durante a apresentação do PBL no dia 17/09, o <strong>Prof. Me. Arlley Costa</strong> fará perguntas técnicas profundas para testar se a equipe 
            apenas "conectou cabos no Packet Tracer" ou se realmente compreendeu o projeto de engenharia, as normas e as restrições físicas do Porto do Itaqui. 
            Abaixo estão as 5 perguntas capitais e como a equipe deve responder tecnicamente:
          </p>

          <div style="display: flex; flex-direction: column; gap: 16px;">
            <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 18px;">
              <h4 style="color: var(--accent-amber); font-size: 14.5px; margin-bottom: 8px;">
                1. "Se vocês juntarem os 5 arquivos Packet Tracer em um único Core Switch de Campus, a rede funciona?"
              </h4>
              <p style="font-size: 13.5px; color: var(--text-secondary); line-height: 1.6;">
                <strong style="color: var(--text-primary);">Resposta Técnica Correta:</strong> "Não, professor. Na nossa auditoria preliminar, 
                identificamos que quatro grupos utilizaram a mesma faixa de IPs <code>192.168.10.0/24</code> a <code>192.168.40.0/24</code> de forma independente, 
                gerando sobreposição de sub-redes (Overlapping Subnets). Por isso, criamos na revisão geral o Plano Mestre de Endereçamento VLSM corporativo 
                no bloco <code>10.100.0.0/16</code>, onde cada prédio possui seu bloco sumarizado (/20 a /23) e suas próprias VLANs hierárquicas, garantindo 
                roteamento limpo via OSPF ou rotas estáticas sem qualquer conflito."
              </p>
            </div>

            <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 18px;">
              <h4 style="color: var(--accent-amber); font-size: 14.5px; margin-bottom: 8px;">
                2. "Por que usar fibra óptica monomodo (OS2) entre a Pera Ferroviária e a Inspetoria, e não cabo Cat6 blindado (STP)?"
              </h4>
              <p style="font-size: 13.5px; color: var(--text-secondary); line-height: 1.6;">
                <strong style="color: var(--text-primary);">Resposta Técnica Correta:</strong> "Por duas razões normativas e físicas, professor (vistas na UA I): 
                1) A distância é de 600 metros, o que excede em mais de 6 vezes o limite máximo de canal permanente de par trançado da ANSI/TIA-568-D e ABNT NBR 14565 (que é de 90m + 10m de patch cords = 100m); 
                2) A ferrovia gera forte interferência eletromagnética (EMI) pelos motores de tração dos trens de minério e soja. A fibra óptica transmite fótons (luz) em vez de pulsos elétricos, conferindo 
                imunidade dielétrica total a ruídos eletromagnéticos e surtos elétricos induzidos por descargas atmosféricas."
              </p>
            </div>

            <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 18px;">
              <h4 style="color: var(--accent-amber); font-size: 14.5px; margin-bottom: 8px;">
                3. "Qual cuidado especial de segurança física e ambiental deve ser tomado no Silo de Grãos?"
              </h4>
              <p style="font-size: 13.5px; color: var(--text-secondary); line-height: 1.6;">
                <strong style="color: var(--text-primary);">Resposta Técnica Correta:</strong> "Silos de grãos possuem poeira vegetal combustível em suspensão, 
                sendo classificados como Atmosfera Explosiva (Zona 20/21/22 segundo IECEx e NR-20/NR-33). Todo equipamento ativo (Access Points, Câmeras e Gateways IoT) 
                deve possuir invólucro certificado à prova de explosão (Ex-d / Ex-t), e os eletrodutos devem ser de aço carbono galvanizado a fogo com rosca NPT 
                e unidades seladoras para impedir que qualquer centelha elétrica interna propague para o ambiente inflamável de grãos."
              </p>
            </div>

            <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 18px;">
              <h4 style="color: var(--accent-amber); font-size: 14.5px; margin-bottom: 8px;">
                4. "Por que a VLAN 180 (Storage SAN/NAS) no Prédio Administrativo não possui gateway configurado?"
              </h4>
              <p style="font-size: 13.5px; color: var(--text-secondary); line-height: 1.6;">
                <strong style="color: var(--text-primary);">Resposta Técnica Correta:</strong> "Porque tráfego de armazenamento em bloco/iSCSI ou NFS dedicado 
                deve ser restrito estritamente à Camada 2 (Data Link) do Modelo OSI, entre as placas dedicadas dos servidores de virtualização e o Storage NAS. 
                Ao não atribuir gateway nem subinterface roteável no roteador, impedimos que qualquer usuário comum, máquina infectada ou visitante Wi-Fi 
                consiga sequer tentar rotear pacotes TCP/IP em direção aos discos de dados corporativos da empresa, garantindo segurança 'by-design'."
              </p>
            </div>

            <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 18px;">
              <h4 style="color: var(--accent-amber); font-size: 14.5px; margin-bottom: 8px;">
                5. "Como foi tratada a alta salinidade e índice pluviométrico da Baía de São Marcos (Porto do Itaqui)?"
              </h4>
              <p style="font-size: 13.5px; color: var(--text-secondary); line-height: 1.6;">
                <strong style="color: var(--text-primary);">Resposta Técnica Correta:</strong> "A região de São Luís possui umidade relativa > 85% e altíssima 
                agressividade por cloretos marinhos. Por isso, adotamos armários externos em aço inoxidável ou poliéster reforçado com fibra de vidro (IP66), 
                conectores ópticos LC com vedação selada, cabos com capa resistente a raios UV/intempéries e dispositivos de proteção contra surtos (DPS Classe I e II) 
                com malha de aterramento equipotencializada conforme a ABNT NBR 5410 e ANSI/TIA-607."
              </p>
            </div>
          </div>
        </section>

      </main>
    </div>
  </div>

  <!-- FOOTER -->
  <footer class="audit-footer">
    <div class="container">
      <p style="font-weight: 600; color: var(--text-primary); margin-bottom: 6px;">
        Auditoria Técnica de Infraestrutura de Redes • UNDB 4.0 Escola de Tecnologia
      </p>
      <p>
        Componente Curricular: Infraestrutura de Redes (80h) • Professor: Me. Arlley Costa • Semestre 2026.2
      </p>
      <p style="margin-top: 8px; font-size: 12px;">
        Documento técnico elaborado para revisão geral, correção de inconformidades e consolidação executiva do Terminal Portuário do Maranhão.
      </p>
    </div>
  </footer>

  <script>
    // Reading progress bar
    window.addEventListener('scroll', () => {
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      document.getElementById('progress-bar').style.width = scrolled + '%';

      // Update active nav item
      const sections = document.querySelectorAll('section.audit-section');
      const navLinks = document.querySelectorAll('.nav-item a');
      
      let currentSectionId = '';
      sections.forEach(sec => {
        const top = sec.offsetTop - 120;
        if (winScroll >= top) {
          currentSectionId = sec.getAttribute('id');
        }
      });

      navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === '#' + currentSectionId) {
          link.classList.add('active');
        }
      });
    });
  </script>
</body>
</html>
"""

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Arquivo {output_file} gerado com sucesso!")
print(f"Tamanho total: {len(html_content)} caracteres.")
