from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import random

IP = ''
PORTA = 0
name = 'gerador'
desc = 'Cria um número aleatorio'

#adicionando servidor ao servidor Nome
server = xmlrpc.client.ServerProxy("http://{0}:{1}/".format('127.0.0.1', 8080))

try:
    IP, PORTA = server.add(name, desc)
except:
    None


#função que busca pelos itens no servidor
def gerador():
    return random.random()

def list_fun():
    return 'lista de funções: gerador'

print(f'\tSERVIDOR {IP} {PORTA}')

print('\nAVISO: O Não escrever no servidor.')

print('\nEsperando por clientes: ')

#cria uma nova instancia de servidor com uma porta e IP predefinidos
servidor = SimpleXMLRPCServer((IP, PORTA))
#registra função gerar numero para uso dos usuarios
servidor.register_function(gerador, "ger")
#registra função listar funções para uso dos usuarios
servidor.register_function(list_fun, "list")
#esse metodo mantem o servidor funcionando mesmo com a desconexão do usuario
servidor.serve_forever()