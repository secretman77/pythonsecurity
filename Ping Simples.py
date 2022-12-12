import os # Importar módulo ou biblioteca "OS" que integra programas e recursos do sistema operacional - O.S.

print ("&" * 70) # Imprimir "&" setents vezes para melhor visualização e apresentação.

ip_ou_host = input("Digite o IP ou Host a ser verificado: ") # Criar variável para receber número "IP" ou nome do "Host"

os.system('ping -n 7 {}'.format(ip_ou_host)) # Chamar comando "ping" da biblioteca "OS" com número de pacotes em "-n".
# format recebe variável "ip_ou_host" e formata dentro de "{}".

print ("&" * 70) # Imprimir "&" setenta vezes para melhor visualização e apresentação.