# Coleta os codigos de cada arquivo
# import re
# from pdfminer.high_level import extract_text

# def extract_code_from_pdf(pdf_file):
#     text = extract_text(pdf_file)
#     regex = r'(?<=Registro Fadesp)\s*\d+'
#     match = re.search(regex, text)

#     if match:
#         code = match.group()
#         return code

#     return None

# pdf_file = 'arquivos/pagina_1.pdf'
# code = extract_code_from_pdf(pdf_file)

# if code:
#     print(code)
# else:
#     print('Código não encontrado.')

import os
import re
from pdfminer.high_level import extract_text

def extract_code_from_pdf(pdf_file):
    text = extract_text(pdf_file)
    regex = r'(?<=Registro Fadesp)\s*\d+'
    match = re.search(regex, text)

    if match:
        code = match.group()
        return code

    return None

def main():
    pdf_folder = 'arquivos'
    result_folder = 'resultados'
    os.makedirs(result_folder, exist_ok=True)

    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            pdf_file = os.path.join(pdf_folder, filename)
            code = extract_code_from_pdf(pdf_file)

            if code:
                result_filename = filename.replace(filename, f'{code}.pdf')
                result_file = os.path.join(result_folder, result_filename)
                os.rename(pdf_file, result_file)
                print(f'Arquivo renomeado para {result_filename}')
            else:
                print(f'Código não encontrado em {filename}.')

if __name__ == '__main__':
    main()