from threading import Thread # Da biblioteca "threading" importar classe "Thread"

import time # Biblioteca/módulo que fornece várias funções relacionadas ao tempo

def carro(velocidade,piloto):# definir função "carro1" com argumento "velocidade"
    trajeto = 0 # Onde o carrinho vai iniciar a corrida
    while trajeto <= 100:# Enquanto variável trajeto for menor ou igual à 100 faça:
        trajeto+=velocidade # somar ao valor atual da variável "trajeto" o valor da variável "velocidade"
        time.sleep(0.5) # aguardar 0.5 segundos para imprimir novamente através da função ".sleep"(dormir)
        print('Piloto: {} KM: {} \n'.format(piloto, trajeto))  # Imprimir na tela "Carro1" mais valor da variável "trajeto"
        # Função ".format" insere valores já formatados das variáveis "piloto" e "trajeto" dentro dos colchetes "{}"
        # "\n" para separar dados do carro1 dos dados do carro2
        # time.sleep( segundos ) = Suspenda a execução do thread de chamada por um determinado número de segundos.
        # format( valor [ , formato _spec ] ) = Converte um valor em uma representação “ formatada ”, conforme controlado pelo formato _spec .

# Threads =  Linhas de execução concorrentes em um mesmo processo
t_carro1 = Thread(target=carro,args=[1,'Marcelo']) # Criar thread para carro1 com componente "target"=alvo e "args"=argumento
t_carro2 = Thread(target=carro,args=[2,'Python']) # Criar thread para carro2 com componente "target"=alvo e "args"=argumento

t_carro1.start() # Iniciar processo carro1
t_carro2.start() #Iniciar processo carro2


