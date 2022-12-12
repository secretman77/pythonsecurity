# "Programa para enviar mensagem ao servidor UDP e aguardar uma resposta
# sincronização, reconhecimento, finalização
# Three-way Handshake (Handshake de três vias)

#Estabelecimento de conexões

#1. O cliente envia um pacote com a flag SYN ativa;
#2. O servidor responde com um pacote com as flags SYN + ACK;
#3. O cliente reponde com um pacote ACK.

import socket # Importar biblioteca "socket" que faz relacionamento da placa de rede e sistema operacional

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)# criar objeto de conexão "s"
        # socket.socket = pegar da biblioteca socket o método socket
        # socket.AF_INET = família de protocolo = IP
        # socket.SOCK_DGRAM = tipo de protocolo = protocolo de datagrama do usuário = UDP


print ("Socket criado com sucesso!!!") # Aviso de criação do socketpu bem sucedida

host = 'localhost' # Rede interna do computador
porta = 5433 # Porta do computador
texto = 'Olá servidor, firmeza?'# mensagem para o servidor

try:
    print ('Cliente:' + texto)
    s.sendto(texto.encode(), (host, 5432))
    # sendto = método para enviar datagrama para socket UDP
    # encode = codifica conteúdo de "mensagem" em datagrama UDP
    # "host" está chamando  "localhost"
    # "5432" =  porta nna qual o servidor estará ouvindo

    dados, servidor = s.recvfrom(4096) # s.recvfrom = objeto de conexão "s" espera do servidor pacote de 4096 bytes
    dados = dados.decode() # Desempacotar mensagem
    print ('Cliente' + dados) # apresenta mensagem do servidor

finally:# Finalizar conexão
    print ('Cliente: Fechando a conexão')
    s.close() # fechar conexão com objeto "s"










