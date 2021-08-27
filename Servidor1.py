from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

IP = ''
PORTA = 0
name = 'estoque'
desc = 'Servidor responde quais itens estão em estoque'

#adicionando servidor ao servidor Nome
server = xmlrpc.client.ServerProxy("http://{0}:{1}/".format('127.0.0.1', 8080))

try:
    IP, PORTA = server.add(name, desc)
except:
    None


#função que busca pelos itens no servidor
def buscar(item):
    lista = ['Arroz', 'Sal', 'Milho', 'Ovos', 'Peixes', 'Carnes', 'leite']

    if item in lista:
        return '1'
    return '0'

def list_fun():
    return 'lista de funções: buscar'

print(f'\tSERVIDOR {IP} {PORTA}')

print('\nAVISO: O Não escrever no servidor.')

print('\nEsperando por clientes: ')

#cria uma nova instancia de servidor com uma porta e IP predefinidos
servidor = SimpleXMLRPCServer((IP, PORTA))
#registra função buscar para uso dos usuarios
servidor.register_function(buscar, "buscar")
servidor.register_function(list_fun, "list")
#esse metodo mantem o servidor funcionando mesmo com a desconexão do usuario
servidor.serve_forever()