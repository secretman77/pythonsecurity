import hashlib
# Biblioteca Hashlib - implementa uma interface comum para muitos algoritmos de hash seguro
# como SHAI , SHA256, MD5 entre outros

arquivo1 = 'a.txt' # atribuir a.txt à variável arquivo1
arquivo2 = 'b.txt' # atribuir b.txt à variável arquivo2

hash1 = hashlib.new('ripemd160')
# variável hash1 define algorítimo de hash
# Biblioteca "hashlib" chama construtor "new", o qual recebe nome do hash a ser utilizado como string

hash2 = hashlib.new('ripemd160')
# variável hash1 define algorítimo de hash
# Biblioteca "hashlib" chama construtor "new", o qual recebe nome do hash a ser utilizado como string

hash1.update(open(arquivo1, 'rb').read())
# hash1 com função "update" informa frase ou arquivos para comparar o hash
# Função "open" para abrir "arquivo1"
# "rb" método de leitura binária (observe aspas em "rb")
# ".read" = método usado para solicitar leitura do arquivo1

hash2.update(open(arquivo2, 'rb').read())
# hash2 com função "update" informa frase ou arquivos para comparar o hash
# Função "open" para abrir "arquivo2"
# "rb" método de leitura binária (observe aspas em "rb")
# ".read" = método usado para solicitar leitura do arquivo2

if hash1.digest() != hash2.digest():# "if" = se (comparador), função "digest" resume informação da função "update"
    print (f' O Arquivo: {arquivo1} é diferente do arquivo: {arquivo2}') #Se forem iguais
    print ('O hash do arquivo a.txt é: ', hash1.hexdigest())
    print ('O hash do arquivo b.txt é: ', hash2.hexdigest())
    # função ".hexdigest" resume informação do hash em hexadecimal
else: # Se não:
    print(f' O Arquivo: {arquivo1} é igual ao arquivo: {arquivo2}')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())