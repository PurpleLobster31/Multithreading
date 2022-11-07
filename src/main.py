import threading
import PyPDF2 as pydf

def ler_PDF(nome_arquivo):
    leitor = pydf.PdfFileReader('data/' + nome_arquivo)
    for num_pagina in range(0, leitor.numPages):
        pagina = leitor.getPage(num_pagina)
        conteudo_pagina = pagina.extract_text()
        paragrafos = conteudo_pagina.split('\n')

if __name__ == "__main__":
    print('Informe a palavra que deseja procurar: ')
    palavra = input()
    
    