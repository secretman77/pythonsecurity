import re
# Biblioteca "re" — Permite Operações com expressões regulares

import json
# Biblioteca json — Fornece operação de codificação e decodificação JSON

from urllib.request import urlopen
#  urllib.request import urlopen - Funções e classes que ajudam a abrir URLs

url = 'https://ipinfo.io/json'
# Site escolhido para consultar IP externo

resposta = urlopen(url)
# Variável recebe dados da url

dados = json.load(resposta)
# Decodificar código da url em Java Script(JSON)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']
# Variáveis que recebem os dados

print('Detalhes do IP externo\n')
print('IP: {4}\nRegião: {1}\nPaís: {2}\nCidade: {3}\nOrganização: {0}'.format(org,regiao,pais,cid,ip))
# Formatar dados com "\n"(quebra de linha) e ordenar dados com ".format" conforme índice inserido em "{}"
print(dados)
