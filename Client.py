import xmlrpc.client
from xmlrpc.server import SimpleXMLRPCRequestHandler

#função para fazer conexão com servidor
def connect(ip, porta):
	servidor = xmlrpc.client.ServerProxy("http://{0}:{1}/".format(ip, porta), allow_none=True)

	return servidor

#função para buscar por servidores apartir dos atributos
def busca_atrr(servidor, attr):
	resposta, name = servidor.buscar_attr(attr)

	return name, resposta

#pede ao servidor para pesquisar se o servidor esta disponivel
def busca_nome(servidor, name):
	resposta = servidor.buscar_name(name)  #

	return resposta

#verifica se digito do usuario esta correto
def dig_num():
	try:
		n = int(input('\n- Digite a quantidades de atributos: '))
		return n
	except:
		print('digite numero valido')
		dig_num()

print('\tCLIENTE')

#IP e Porta do servidor nomes
IP = 'localHost'
PORTA = 8080
#cria uma conexão com o servidor e porta predefinidos
servidor = connect(IP, PORTA)


entrada = ''
resposta = None
name = ''


while entrada != 'fim':
	entrada = input('\n- Digite qual tipo de pesquisa[nome, atributo, fim]: ').lower()

	if entrada == 'nome':
		entrada = 'fim'
		name = input('\n- Digite o nome do serviço ou fim para buscar: ').lower()
		resposta = busca_nome(servidor, name)

	elif entrada == 'atributo':
		entrada = 'fim'
		n = dig_num()
		attrs = []

		for i in range(n):
			attrs.append(input('\n- Digite o atributo para buscar: ').lower())
		name, resposta = busca_atrr(servidor, attrs)


if resposta != None:
	print(f'O servidor {name.upper()} com Porta: {resposta[0][1]} e IP: {resposta[0][0]}\n')
	print(f'Atributos: {resposta[2]}')
	print('Foi encontrado com sucesso')
	#conecta ao servidor buscado
	servidor = connect(resposta[0][0], resposta[0][1])
	#acessa a função que lista as funções
	print(servidor.list())

else:
	print('Servidor não encontrado ou não cadastrado')