from collections import namedtuple
import PyPDF2 as pydf
from typing import List, Tuple


def ler_PDF(nome_arquivo:str) -> Tuple[List[List], int]:
  '''
    funcao que lê o texto do pdf e define o número de threads a serem usadas
    :param nome_arquivo: nome do arquivo em pdf a ser lido
    :return: tupla com todas_linhas (matriz de linhas do arquivo) e um inteiro que representa o número total de threads (2 threads por página)
  '''
  todas_linhas = []
  leitor = pydf.PdfFileReader('data/' + nome_arquivo)
  for num_pagina in range(leitor.numPages):
      pagina = leitor.getPage(num_pagina)
      conteudo_pagina = pagina.extract_text()
      linhas_pag = conteudo_pagina.split('\n')
      todas_linhas.append(linhas_pag)
  return todas_linhas, leitor.numPages*2

def alimenta_dados(alvo_busca:str, linhas:List[List]) -> List[namedtuple]:
  '''
    funcao que alimenta uma lista de namedtuples(subclasses de tuplas com nomes de campo) que serão utilizadas como iteradores da função alvo das threads que serão criados
    :param alvo_busca: palavra alvo da busca
    :param linhas: matriz de linhas lidas do arquivo 
    :return: lista preenchida com namedtuples(subclasses de tuplas com nomes de campo)
  '''
  infos = []
  Info = namedtuple('Info', ['num_pag','alvo','linhas_para_ler'])
  for num_pagina, linhas_pagina in enumerate(linhas, start=1):
      num_linhas_thread = int(len(linhas_pagina)/2)
      info_thread1 = Info(num_pagina, alvo_busca, linhas_pagina[:num_linhas_thread])
      info_thread2 = Info(num_pagina, alvo_busca, linhas_pagina[num_linhas_thread:])
      infos.append(info_thread1)
      infos.append(info_thread2)
  return infos

  #roda 