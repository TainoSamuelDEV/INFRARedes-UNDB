import re

html_path = 'Auditoria-Geral-InfraRedes-UNDB.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'101\s+(?:nodes|dispositivos)', '104 dispositivos', content)
content = re.sub(r'101 nodes', '104 nodes', content)
content = re.sub(r'36 nodes', '39 nodes', content)

old_master_row = re.search(r'<td><strong>Terminal-Portuario-Geral\.pkt</strong></td>.*?</tr>', content, re.DOTALL)
if old_master_row:
    new_master_row = """<td><strong>Terminal-Portuario-Geral.pkt</strong></td>
                  <td><strong>Complexo Completo (Master Unificado)</strong></td>
                  <td><code>10.100.0.0/16</code> (Campus)</td>
                  <td>104 nodes / 84 links</td>
                  <td>487.681 B</td>
                  <td><code style="font-size: 11px;">2f91cd430ea1...</code></td>
                  <td><span class="badge success">Master Homologado</span></td>
                </tr>"""
    content = content.replace(old_master_row.group(0), new_master_row)

old_adm_row = re.search(r'<td>Predio-Administrativo-TP\.pkt</td>.*?</tr>', content, re.DOTALL)
if old_adm_row:
    new_adm_row = """<td>Predio-Administrativo-TP.pkt</td>
                  <td>Prédio ADM & Datacenter (Atualizado com ALTERADO)</td>
                  <td><code>10.20.0.0/16</code> + Rotas Campus</td>
                  <td>39 nodes / 33 links</td>
                  <td>373.954 B</td>
                  <td><code style="font-size: 11px;">8aa4a8db9408...</code></td>
                  <td><span class="badge success">Atualizado</span></td>
                </tr>"""
    content = content.replace(old_adm_row.group(0), new_adm_row)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML atualizado com sucesso.")
