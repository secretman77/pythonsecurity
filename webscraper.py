from bs4 import BeautifulSoup
# Beautiful Soup é uma biblioteca Python para extrair dados de arquivos HTML e XML. Ele funciona com seu analisador
# favorito para fornecer maneiras idiomáticas de navegar, pesquisar e modificar a árvore de análise.

import requests # A "requests" biblioteca é o padrão para fazer solicitações HTTP em Python

site = requests.get("https://www.climatempo.com.br/").content
# Objeto "site" recebe a requisição através da biblioteca "requests" trazida através da função ".get" o conteúdo
# do site "https://www.climatempo.com.br/" solicitado pela função ".content"

soup = BeautifulSoup(site, 'html.parser')
# Objeto "soup" baixando do site seu código HTML através da biblioteca "BeautifulSoup"

#print(soup.prettify()) # *** Opcional -> visualizar HTML ***
# Função ".prettyfi" transforma objeto "soup" em string e função "print" imprime código HTML na tela

temperatura = soup.find("span",class_="-bold -gray-dark-2 -uppercase -font-12 _padding-5")
# Objeto "temperatura" recebe dados conforme "tag e class" entre parênteses utilizando função ".find"(encontrar) do
# HTML do objeto "soup". *** Foram adicionadas aspas duplas à tag "span" e underline após "class".***

print(soup.title.string)
# Imprimir somente o título do site com função "string"(Transformar em texto claro) aplicada à função "title"
# (extrair título)

print(soup.a.string) # Trazer primeira tag âncora HTML através da função ".a"

print(soup.p.string) # Trazer primeiro tag parágrafo HTML através da função ".p"

print(soup.find('Clima')) # Encontrar item dentro do HTML com função ".find"

print(temperatura.string) # Imprimir objeto "temperatura" com função ".string"(Transformar em texto claro)