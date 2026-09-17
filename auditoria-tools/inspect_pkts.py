import os
import glob
import zipfile

pkt_files = glob.glob('**/*.pkt', recursive=True)
print("Arquivos PKT encontrados:")
for p in pkt_files:
    sz = os.path.getsize(p)
    print(f" - {p} ({sz} bytes)")
    # Test if it is a zip
    is_zip = zipfile.is_zipfile(p)
    print(f"   É zip? {is_zip}")
    if is_zip:
        try:
            with zipfile.ZipFile(p, 'r') as z:
                print(f"   Arquivos internos: {z.namelist()[:5]}")
        except Exception as e:
            print(f"   Erro ao abrir zip: {e}")
    else:
        # Check header bytes
        with open(p, 'rb') as f:
            header = f.read(32)
            print(f"   Header bytes: {header[:16]}")
