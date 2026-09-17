import json
import os

def check_jsons():
    targets = [
        "Portaria-TP(Taino Samuel e Victor Cabral)/03-Packet-Tracer/inventario-validacao.json",
        "Portaria-TP(Taino Samuel e Victor Cabral)/03-Packet-Tracer/plano-dispositivos.json",
        "Portaria-TP(Taino Samuel e Victor Cabral)/04-Orcamento/dados-orcamento.json",
        "Portaria-TP(Taino Samuel e Victor Cabral)/05-Validacao/Relatorio-de-validacao.md",
        "Predio-Administrativo(Gabriel Ordonez e Higor Gabriel)/03-Packet-Tracer/inventario-validacao.json",
        "Predio-Administrativo(Gabriel Ordonez e Higor Gabriel)/05-Validacao/Relatorio-de-validacao.md",
        "Predio-Administrativo(Gabriel Ordonez e Higor Gabriel)/05-Validacao/resultado-verificacao.json",
        "Predio-Administrativo(Gabriel Ordonez e Higor Gabriel)/05-Validacao/Roteiro-de-testes-manuais.md",
    ]
    
    for t in targets:
        if os.path.exists(t):
            print(f"\n==========================================")
            print(f"ARQUIVO: {t}")
            print(f"==========================================")
            with open(t, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                print(content[:1500])
                if len(content) > 1500:
                    print(f"\n... [Total de {len(content)} caracteres]")

if __name__ == '__main__':
    check_jsons()
