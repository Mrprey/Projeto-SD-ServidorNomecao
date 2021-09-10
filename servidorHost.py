from xmlrpc.server import SimpleXMLRPCServer

print('\tSERVIDOR')

IP = 'localhost'
PORTA = 8080

server_list = {} #lista de servidores
#função que busca pelos servidores diponiveis
def buscar_name(name):
    try:
        return server_list[name]
    except:
        return None

def buscar_attr(attr):
    try:
        for name in server_list.keys():
            for uni_attr in attr:
                if uni_attr in server_list[name][2]:
                    return server_list[name], name
        return None, None
    except:
        return None, None

#add de no servidor para pesquisa e setando o ip e porta
def add(nome, descr, attr):
    tam_list = server_list.__len__()
    try:
        server_list[nome] = [geradorConnect(tam_list), descr, attr]
        print(server_list)
        return server_list[nome][0][0], server_list[nome][0][1]
    except:
        None

#gera a porta e ip do novo servidor
def geradorConnect(num):
    return geradorIP(), geradorPorta(num+1)

def geradorIP():
    return IP

def geradorPorta(num):
    return PORTA+num

print('\nAVISO: O Não escrever no servidor.')

print('\nEsperando por clientes: ')

#cria uma nova instancia de servidor com uma porta e IP predefinidos
servidor = SimpleXMLRPCServer((IP, PORTA), allow_none=True)
#registra função buscar para uso dos usuarios
servidor.register_function(buscar_name, "buscar_name")

servidor.register_function(buscar_attr, 'buscar_attr')

#registra função inserir servidor
servidor.register_function(add, "add")
#esse metodo mantem o servidor funcionando mesmo com a desconexão do usuario
servidor.serve_forever()