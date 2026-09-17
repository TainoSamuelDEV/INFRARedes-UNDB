import pdfplumber
import glob

def find_keywords_in_uas():
    uas = sorted(glob.glob('UA *.pdf'))
    keywords = ['ppdioo', 'nbr 14565', 'tia-568', '568-c', '568-d', 'cat6', 'cat6a', 'fibra', 'distancia', '90 m', '100 m', 'sub-rede', 'vlsm', 'cidr', 'osi', 'transporte', 'apresenta']
    
    for u in uas:
        print(f"\n==========================================")
        print(f"UA: {u}")
        print(f"==========================================")
        with pdfplumber.open(u) as pdf:
            for i, page in enumerate(pdf.pages):
                txt = page.extract_text() or ""
                for kw in keywords:
                    if kw in txt.lower():
                        # print the line
                        for line in txt.splitlines():
                            if kw in line.lower():
                                print(f"  P{i+1} [{kw}]: {line.strip()[:100]}")

if __name__ == '__main__':
    find_keywords_in_uas()
