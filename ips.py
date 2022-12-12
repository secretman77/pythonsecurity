import ipaddress # Biblioteca ipaddress fornece os recursos para criar, manipular e operar em redes e endereços IPv4 e IPv6.

#ip = '192.168.0.1' # Variável que recebe determinado número IP

ip = '192.168.0.0/32' # Variável que recebe determinado número de rede

# endereco = ipaddress.ip_address(ip) # Objeto "endereço" recebe da biblioteca "ipaddres" o método ".ip_address()"

rede = ipaddress.ip_network(ip,strict=False) # Objeto "endereço" recebe da biblioteca "ipaddres" o método ".ip_network()"

print(rede) # Imprimir na tela valor do objeto "endereco"

for ip in rede:
    print(ip)


