import PyPDF2
import os

# Abre o arquivo PDF para leitura
with open('certificados_para_assinatura_original.pdf', 'rb') as arquivo:
    # Lê o arquivo PDF e obtem o número de páginas
    leitor = PyPDF2.PdfReader(arquivo)
    num_paginas = len(leitor.pages)

    # Percorre cada página do arquivo PDF e a salva em um novo arquivo
    for pagina in range(num_paginas):
        leitor_pagina = PyPDF2.PdfReader(arquivo)
        writer = PyPDF2.PdfWriter()
        writer.add_page(leitor_pagina.pages[pagina])

        with open(os.path.join('arquivos', f'pagina_{pagina+1}.pdf'), 'wb') as nova_pagina:
            writer.write(nova_pagina)

print("PDF dividido com sucesso!")