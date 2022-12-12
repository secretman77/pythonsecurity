import requests # A "requests" biblioteca é o padrão para fazer solicitações HTTP em Python
from bs4 import BeautifulSoup
# Beautiful Soup é uma biblioteca Python para extrair dados de arquivos HTML e XML. Ele funciona com seu analisador
# favorito para fornecer maneiras idiomáticas de navegar, pesquisar e modificar a árvore de análise.

import operator
# Biblioteca "operator" exporta um conjunto de funções eficientes correspondentes
# aos operadores intrínsecos do Python como: + - * / not and

from collections import Counter
# Biblioteca "collections" nos ajuda a preencher e manipular eficientemente as estruturas de dados como tuplas,
# dicionários e listas.
# Counter é uma classe onde os elementos são armazenados como chaves de dicionário e suas contagens são armazenadas como
# valores de dicionário. As contagens podem ser qualquer valor inteiro, incluindo zero ou contagens negativas.


def start(url): # Startar URL
    wordlist = [] # Lista vazia para receber o conteúdo do site
    source_code = requests.get(url).text


    soup = BeautifulSoup(source_code, 'html.parser') # Faz requisição do conteúdo do site e converte em HTML
    # O texto em determinada página da web é armazenado em tags da classe <entry-content>

    for each_text in soup.find_all('div',{'class':'entry-content'}):
    # "each_text" procurar dentro do texto da HTML baixado com "soup.find_all" tudo que contiver "div","class",
    # "entry-content"
        content = each_text.text
        # Transforma conteúdo da URL em "string"

        words = content.lower().split()
        # Transforma conteúdo em letras minúsculas e separa em linhas

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)

def clean_wordlist(wordlist): # Remover qualquer conteúdo indesejado conforme "symbols"
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*_-+={[}]|\;:"<>?/., '

        for i in range(0,len(symbols)):
            word = word.replace(symbols[i], '') # Trocar cada item de "symbols" por nada(vazio) com "replace"

        if len(word) > 0: # se word for maior que zero ele vai limpando a lista
            clean_list.append(word)
        create_dictionary(clean_list)

def create_dictionary(clean_list): # Cria um dicionário acrescentando cada palavra e realiza e exibe contagem
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        # mostrar palavras chaves com mais ocorrência neste site
        print ("% s : % s" % (key, value))

    c = Counter(word_count)

    top = c.most_common(10)
    #"most_common" retorna uma lista dos n elementos mais comuns e suas contagens, do mais comum ao menos.

    print(top)


if __name__ == '__main__':  # Chama função principal que no caso é a função "start"
    #start("https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar")
    start("https://www.mediawiki.org/wiki/Special:MyLanguage/Help:Categories/?ref=lefbar")



