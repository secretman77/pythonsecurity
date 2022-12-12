import socket # Importar biblioteca "socket" que faz relacionamento da placa de rede e sistema operacional

import sys # Importar biblioteca "sys" que fornece acesso à variáveis e funções que têm forte interação com
# interpretador "Python"

def main (): # Definir função chamada "main" para realizar conexão TCP/IP

    try: # try = função para testar pontos críticos do programa e inserir tratamento de exceções

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM, 0)
        # socket.socket = pegar da biblioteca socket o método socket
        # socket.AF_INET = família de protocolo = IP
        # socket.SOCK_STREAM = tipo de protocolo = TCP
        # 0 = número do protocolo (TCP)

    except socket.error as e:# chamar função "except" com método "socket.error" para inserir o erro na variável "e"

        print ("A conexão falhou!!!") # se der erro vai imprimir esta frase
        print ("Erro: {}".format(e)) # método ".format" vai inserir erro dentro de "{}" e exibir conteúdo

        sys.exit() # Método ".exit" na função "sys" para fechar aplicação em caso de erro

    print ("Socket criado com sucesso!!!") # Aviso de criação do socketpu bem sucedida

    HostAlvo = input("Digite o Host ou IP a ser conectado: ") # Criar espaço para usuário inserir "HOST"
    PortaAlvo = input("Digite a porta a ser conectada: ") # Criar espaço para usuário inserir "Porta de Conexão"

    try: # Tentar a conexão

        s.connect((HostAlvo, int(PortaAlvo))) # "s" é o objeto de conexão e o ".connect" o método que realiza a conexão
 # ".connect" solicita "address" = "HostAlvo" e porta = "PortaAlvo", *** é preciso "int" para converter em inteiro***

        print ("Cliente TCP conectado com sucesso no host: " + HostAlvo + " e na porta: " + PortaAlvo)
        # Aviso de execução bem sucedida no host e porta solicitados.

        s.shutdown(2) # Chamar método ."shutdown" para objeto"s" para encerrar conexão após 2 segundos para não gerar looping.

    except socket.error as e: # chamar função "except" com método "socket.error" para inserir o erro na variável "e"

        print (" Não foi possível conectar no Host: " + HostAlvo + " -> porta: " + PortaAlvo)
        # Aviso de conexão mau sucedida.

        print("Erro: {}".format(e))
        # método ".format" vai inserir erro dentro de "{}" e exibir conteúdo

        sys.exit() # Método ".exit" na função "sys" para fechar aplicação em caso de erro

if __name__ == "__main__": # Se o nome da função for "main" executar função "main"
    main() # Chamada da função