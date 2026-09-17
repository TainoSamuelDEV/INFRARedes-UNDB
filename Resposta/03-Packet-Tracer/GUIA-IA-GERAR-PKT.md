# Guia simples para uma IA gerar o arquivo `.pkt`

Use este guia quando todo o trabalho de redes já estiver documentado e faltar apenas montar e salvar a topologia no Cisco Packet Tracer.

## 1. O que entregar à IA

Forneça, na mesma pasta ou conversa:

- enunciado original do trabalho;
- relatório final;
- topologias física e lógica;
- tabela de dispositivos, portas, VLANs e endereços IP;
- configurações de roteadores e switches, se existirem;
- regras de DHCP, DNS, Wi-Fi, telefonia e ACL;
- versão do Cisco Packet Tracer usada pela equipe;
- nome e caminho desejados para o arquivo final.

Se alguma informação estiver em conflito, a IA deve apontar o conflito antes de montar o laboratório. Ela não deve inventar decisões que alterem o projeto aprovado.

## 2. Método correto

A forma mais segura é a IA controlar o Cisco Packet Tracer e montar o laboratório pela interface do próprio programa:

1. ler todos os documentos do trabalho;
2. criar um inventário único dos dispositivos e enlaces;
3. abrir o Packet Tracer na versão definida;
4. inserir dispositivos nativos equivalentes aos especificados;
5. nomear e conectar os equipamentos conforme a topologia;
6. configurar portas, VLANs, trunks, endereços, gateways e serviços;
7. salvar diretamente pelo Packet Tracer em formato `.pkt`;
8. fechar e abrir novamente o arquivo;
9. executar os testes previstos no trabalho;
10. registrar o resultado e as limitações reais da simulação.

Python pode preparar configurações, inventários e verificações auxiliares. Ele não deve ser usado para criar um arquivo binário improvisado, renomear outro formato para `.pkt` ou declarar compatibilidade sem abrir o resultado no Packet Tracer.

Se a IA não tiver acesso ao aplicativo, ela deve informar essa limitação e produzir apenas um pacote de montagem: lista de dispositivos, mapa de portas, configurações CLI e roteiro de testes. Nesse caso, o `.pkt` ainda deverá ser criado e validado no Packet Tracer.

## 3. Prompt pronto para copiar

```text
Analise todos os arquivos deste trabalho antes de executar qualquer alteração. O projeto já está concluído; falta apenas criar o arquivo nativo do Cisco Packet Tracer.

Objetivo:
- montar no Cisco Packet Tracer a topologia descrita nos documentos;
- usar exatamente os dispositivos, nomes, enlaces, portas, VLANs, endereços e serviços documentados;
- salvar o resultado como [NOME-DO-ARQUIVO.pkt] em [CAMINHO-DE-DESTINO].

Regras:
1. Crie primeiro um inventário consolidado e confira conflitos entre os arquivos.
2. Não altere a arquitetura para facilitar a montagem.
3. Use dispositivos nativos do Packet Tracer. Quando não houver modelo idêntico, escolha o equivalente funcional e documente a equivalência.
4. Configure switches, roteadores, servidores e terminais conforme o relatório.
5. Use cabos e interfaces coerentes com a topologia física.
6. Não invente resultados de ping, DHCP, DNS, HTTP, telefonia ou ACL.
7. Não gere um arquivo falso, vazio ou apenas renomeado para .pkt.
8. O arquivo só pode ser considerado pronto depois de ser salvo pelo Packet Tracer, fechado, reaberto sem erro e testado.
9. Preserve os demais arquivos do trabalho.

Validação obrigatória:
- conferir a quantidade e os nomes dos dispositivos;
- conferir cada enlace e cada porta;
- verificar VLANs e trunks;
- verificar endereçamento IP, máscaras e gateways;
- testar DHCP e serviços configurados;
- testar conectividade permitida e bloqueios de ACL;
- verificar Wi-Fi e telefonia quando fizerem parte do projeto;
- executar os testes também no modo Simulation quando solicitado;
- registrar a versão do Packet Tracer, a data da validação e o SHA-256 do arquivo final.

Ao terminar, informe:
- caminho do arquivo .pkt;
- versão do Packet Tracer usada;
- resumo do inventário;
- testes realmente executados e seus resultados;
- equivalências ou limitações da simulação;
- pendências que ainda exigem demonstração manual.

Se você não puder controlar ou abrir o Cisco Packet Tracer, pare antes de afirmar que o .pkt foi criado. Entregue as configurações e o roteiro necessário para uma montagem manual fiel.
```

Substitua os campos entre colchetes antes de enviar o prompt.

## 4. Checklist de aceitação

O arquivo final é aceitável somente quando:

- [ ] foi salvo pelo Cisco Packet Tracer;
- [ ] abre novamente sem erro ou alerta de incompatibilidade;
- [ ] contém todos os equipamentos do inventário;
- [ ] nomes, portas e cabos correspondem à documentação;
- [ ] VLANs, trunks, IPs, máscaras e gateways estão corretos;
- [ ] os serviços previstos estão configurados;
- [ ] os testes de conectividade foram realmente executados;
- [ ] os bloqueios de segurança também foram testados;
- [ ] o relatório distingue testes executados de testes ainda pendentes;
- [ ] o arquivo possui nome final, versão registrada e hash SHA-256.

## 5. Aplicação neste trabalho

Para a Portaria TP, a IA deve usar como fontes principais:

- `../01-Relatorio/Relatorio-Portaria-TP.pdf`;
- `../02-Plantas/02-Topologia-fisica.pdf`;
- `../02-Plantas/03-Topologia-logica.pdf`;
- `plano-dispositivos.json`;
- `LEIA-ME-Portaria-TP.md`;
- `../05-Validacao/Relatorio-de-validacao.md`.

O nome previsto para o laboratório é `Portaria-TP-Taino-Victor.pkt`. A IA deve preservar as decisões registradas nesses documentos e indicar qualquer divergência antes de modificar o laboratório.
