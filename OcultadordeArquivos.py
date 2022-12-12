import ctypes
#Biblioteca "ctypes" — fornece tipos de dados compatíveis com C e permite funções de chamada
# em DLLs ou bibliotecas compartilhadas

pasta = input("Digite o caminho da pasta a ser ocultada no formato C:/pasta: ")

atributo_ocultar = 0x02
# "0x02" Atributo hexadecimal que será passado para arquivo através de "SetFileAttributtesW"

retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)

#retorno = ctypes.windll.kernel32.SetFileAttributesW('Ocultar.txt', atributo_ocultar)
# opção para ocultar apenas um arquivo

# "windll" = classe que carrega bibliotecas compartilhadas do "Windows"
# "kernel32" =  ctypes usa o tratamento de exceção estruturada "kernel32" para evitar travamentos de falhas de proteção
# geral quando as funções são chamadas com valores de argumento inválidos.
# "SetFileAttributtesW" = configurar atributos e reescrever arquivo

if retorno:
    print('Arquivo ocultado com sucesso!')

else:
    print('Falha! Arquivo NÃO ocultado!')