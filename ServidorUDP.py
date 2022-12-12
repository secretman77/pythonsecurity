import socket # Importar biblioteca "socket" que faz relacionamento da placa de rede e sistema operacional

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)# criar objeto de conexão "s"

print ("Socket criado com sucesso!!!") # Aviso de criação do socket bem sucedida

host = 'localhost' # Rede interna do computador
porta = 5432 # Porta do servidor

s.bind((host, porta)) # Método "bind" faz ligação entre cliente e servidor através do host e da porta

frase = '\nServidor:Olá cliente, e aí beleza?' # mensagem para o cliente

while 1 : # enquanto resposta do "bind" for "1" (verdadeiro) faça:
    dados, end = s.recvfrom(4096) # "dados" e "end" receberão o pacote de 4096 bytes

    if dados:
        print('Servidor enviando mensagem...')# mensagem para o cliente
        s.sendto(dados + (frase.encode()), end)
        # sendto = método para enviar datagrama para socket UDP
        # encode = codifica conteúdo de "mensagem" em datagrama UDP
        s.close()



