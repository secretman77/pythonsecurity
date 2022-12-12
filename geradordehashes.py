import hashlib
# Biblioteca Hashlib - implementa uma interface comum para muitos algoritmos de hash seguro
# como SHAI , SHA256, MD5 entre outros

string = input("Digite o texto a ser gerado a hash: ")

menu = int(input (''' ### MENU - ESCOLHA O TIPO DE HASH: ### 
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Digite o tipo do hash a ser gerado: '''))
# variável "menu" recebe tipo de hash do "input" convertido para inteiro por "int" dentre opções do menu

if menu == 1: # Salto condicional "if"(se) para saltar entre opções do menu
    resultado = hashlib.md5(string.encode('utf-8'))
    print('A hash MD5 da string:', string, 'é: ', resultado.hexdigest())
# Variável resultado recebe string do input na variável "string" e codificado antes do hashe por ".encode 'utf-8'"
# e depois transformado em hashe md5 por "hashlib.md5".

elif menu == 2: # salto condicional "ELIF" (se condição anterior não for satisfeita então faça)
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('A hash SHA1 da string:', string, 'é: ', resultado.hexdigest())

elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('A hash SHA256 da string:', string, 'é: ', resultado.hexdigest())

elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('A hash SHA512 da string:', string, 'é: ', resultado.hexdigest())

else: # saldo condicional "else"(senão) -> (se nenhuma condição for satisfeita então faça:)
    print('Algo está incorreto. Por favor tente novamente!')

# resultado = hashlib.md5(b'Python Security') # ( abaixo fase opcional sem input)
# Variável resultado recebe string "Python Security" convertido para binário por "b" e depois transformado
#em hashe md5 por "hashlib.md5".

#print ("O hash da string é ", resultado.hexdigest())
# variável "resultado" é impressa após convertida de binário para hexadecimal por ".hexdigest"