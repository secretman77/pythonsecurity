import os
import time

with open('Hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print ('Verificando o IP: ', ip)
        print ('*' * 70)
        os.system('ping -n 5 {}'.format(ip))
        print('*' * 70)
        time.sleep(5)