import xmlrpc.client

print('\tCLIENTE')

#IP e Porta do servidor nomes
IP = 'localHost'
PORTA = 8080
#cria uma conexão com o servidor e porta predefinidos
servidor = xmlrpc.client.ServerProxy("http://{0}:{1}/".format(IP, PORTA))


name = input('\n- Digite o nome do produto ou fim para buscar itens: ').lower()

resposta = servidor.buscar(name) #pede ao servidor para pesquisar se o item esta disponivel

if resposta != None:
	print(f'O servidor {name} com Porta: {resposta[0][1]} e IP: {resposta[0][0]}\n')
	print('Foi encontrado com sucesso')

	servidor = xmlrpc.client.ServerProxy("http://{0}:{1}/".format(resposta[0][0], resposta[0][1]))

	print(servidor.list())

else:
	print('Servidor não encontrado ou não cadastrado')