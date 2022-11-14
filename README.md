# ThreadedFinder

Este software tem por objetivo emular uma ferramenta que busca palavras ou expressões em um arquivo PDF.

## Instalação e dependências

A aplicação utiliza a versão 3.9 do python e apenas uma dependência externa, esta é a lib [pypdf2](https://pypi.org/project/PyPDF2/) que pode ser instalada manualmente da seguinte forma:

```sh
$ pip install PyPDF2
```

### Configurando automaticamente com o conda

Caso você já utilize o gerenciador de ambientes [conda](https://www.anaconda.com/products/distribution) pode instalar tudo de uma vez só utilizando o arquivo _requirements.yml_. Basta executar:

```sh
$ conda env create -f requirements.yml 
```

OBS.: verifique se o local de instalação da plataforma no seu dispositivo coincide com o local especificado em ```prefix``` do arquivo de configuração.
Visite [Managing Environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) para quaisquer dúvidas.

## Modo de uso

Com o repositório do projeto hospedado localmente, entre na pasta do projeto e execute o seguinte:

```sh
$ python src/main.py
```

Em seguida o software é iniciado e é solicitado o __nome do arquivo__ PDF de onde serão lidos os dados (Não é necessário acrescentar .pdf ao final do nome). Caso você ainda não tenha adicionado nenhum arquivo siga as intruções no tópico _Adicionando arquivos para leitura_.

O próximo passo é digitar a palavra ou expressão a ser buscada. Este software não diferencia letras maiúsculas de minúsculas.

Pronto! Você deverá receber o número total de vezes que a palavra ou expressão foi encontrada seguidos pelos locais dessas ocorrências.

### Adicionando arquivos para leitura

Todos os arquivos para leitura __devem estar no formato PDF__ e devem ser previamente inseridos na pasta __data__ na raíz do projeto.

_Para fins de testes a pasta data já conta com o arquivo do conto O Espelho de Machado de Assis._
