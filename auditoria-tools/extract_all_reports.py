import os
import zipfile
import xml.etree.ElementTree as ET
import pdfplumber
import json

def extract_docx(file_path):
    try:
        with zipfile.ZipFile(file_path) as docx:
            xml_content = docx.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            paragraphs = []
            for node in tree.iter():
                if node.tag.endswith('}p'):
                    p_text = ''.join(node.itertext()).strip()
                    if p_text:
                        paragraphs.append(p_text)
            return '\n'.join(paragraphs)
    except Exception as e:
        return f"Erro ao ler docx {file_path}: {e}"

def extract_pdf(file_path):
    try:
        text = []
        with pdfplumber.open(file_path) as pdf:
            for i, page in enumerate(pdf.pages):
                p_text = page.extract_text()
                if p_text:
                    text.append(f"--- PÁGINA {i+1} ---\n" + p_text)
        return '\n\n'.join(text)
    except Exception as e:
        return f"Erro ao ler pdf {file_path}: {e}"

def main():
    os.makedirs('extracted_reports', exist_ok=True)
    
    # 1. Pera Ferroviaria
    pera_pdf = os.path.join("Pera-Ferroviaria(João Lucas e Jaylon Coelho)", "Relatório Geral - Pera Ferroviária.pdf")
    if os.path.exists(pera_pdf):
        with open('extracted_reports/pera_ferroviaria.txt', 'w', encoding='utf-8') as f:
            f.write(extract_pdf(pera_pdf))
        print("Pera Ferroviária extraído com sucesso.")
        
    # 2. Portaria TP
    portaria_md = os.path.join("Portaria-TP(Taino Samuel e Victor Cabral)", "01-Relatorio", "Relatorio-Portaria-TP.md")
    if os.path.exists(portaria_md):
        with open(portaria_md, 'r', encoding='utf-8') as src, open('extracted_reports/portaria_tp.txt', 'w', encoding='utf-8') as f:
            f.write(src.read())
        print("Portaria TP extraído com sucesso.")
        
    # 3. Predio Administrativo
    adm_docx = os.path.join("Predio-Administrativo(Gabriel Ordonez e Higor Gabriel)", "01-Relatorio", "Projeto_de_Redes_Predio_Administrativo_TP.docx")
    if os.path.exists(adm_docx):
        with open('extracted_reports/predio_adm.txt', 'w', encoding='utf-8') as f:
            f.write(extract_docx(adm_docx))
        print("Prédio Administrativo extraído com sucesso.")
        
    # 4. Predio Inspetoria
    insp_pdf = os.path.join("Predio-Inspetoria(Mateus Dantas e Renan Pires)", "relatorioinspetoriaberco098.pdf")
    if os.path.exists(insp_pdf):
        with open('extracted_reports/predio_inspetoria.txt', 'w', encoding='utf-8') as f:
            f.write(extract_pdf(insp_pdf))
        print("Prédio Inspetoria extraído com sucesso.")
        
    # 5. Silo de Grãos
    silo_pdf = os.path.join("Silo-Grãos(Asafe e Lucas)", "Projeto de Rede do Silo de Grãos.pdf")
    if os.path.exists(silo_pdf):
        with open('extracted_reports/silo_graos.txt', 'w', encoding='utf-8') as f:
            f.write(extract_pdf(silo_pdf))
        print("Silo de Grãos extraído com sucesso.")

if __name__ == '__main__':
    main()
