import random # "random": Biblioteca que implementa geradores de números letras e símbolos aleatórios.
import string # "string": Biblioteca que implementa operações comuns para strings.

tamanho = int(input('Digite o número de caracteres desejado para a senha: '))
# tamanho = 16 #variável que recebe  número de caracteres da senha -> padrão em segurança da informação = 16

chars = string.ascii_letters + string.digits + '@#$%¨&*()-+§<>:[]{}?,.;/^~Ç'
# variável que irá definir estrutura de formação das senhas
# string.ascii_letters = módulo que gera letras maiúsculas e minúsculas
# string.digits = módulo que gera dígitos de 0-9
# '@#$%¨&*()-+§<>:[]{}?,.;/^~' = incluir caracteres especiais
5
# .ascii_lowercase = se utilizado gera apenas letras minúsculas
# .ascii_uppercase = se utilizado gera apenas letras maiúsculas

rnd = random.SystemRandom()
# variável rnd que receberá a senha gerada
# random.SystemRandom() = função ".SystemRandom" da biblioteca "random" fará uso de "os.urandom"
# ".urandom" =  função da biblioteca "os" que recebe do sistema operacional senhas aleatórias

print (' '.join(rnd.choice(chars) for i in range(tamanho)))
# join = faz a junção dos itens aleatórios recebidos
# choice =  escolhe um item de uma lista de itens gerados randomicamente, no caso da variável "chars"
# rnd = recebe os itens aleatórios
# "for i in range" = salto condicional que provoca várias iterações("i") na geração dos itens aleatórios até atingir
# um limite inserido na função "range" que no caso o limite é a variável "tamanho".