import itertools # Importar Itertools — Biblioteca que fornece condições para iterações como permutação e combinação.

string = input("String a ser permutada: ") # Entrada de string pelo usuário mediante função "input"
contador = 0 # Contador para número de palavras na WordList
resultado = itertools.permutations(string, len(string))
# Variável "resultado" recebe da biblioteca "itertools" função ".permutations" para permutar valores da variável
# "string" criando palavras com mesmo tamanho da string através da função "len"(tamanho)
for i in resultado:# para cada item da variável "resultado" faça:
    print (' '.join(i)) # imprimir conjunto dos itens(caracteres) de "i" com função ".join"(juntar).
    contador = contador + 1 # somar um a cada iteração

print ('Esta WordList contém ', contador, 'palavras!') # printar tamanho da WordList