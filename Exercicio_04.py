# INSCRIÇÕES PARA O CURSO DE PYTHON

# importando módulo gerador de 
# identificador único universal 
# (do inglês universally unique identifier - UUID)
import uuid

# Criação de uma lista vazia de inscritos
# que será populada com append dos novos inscritos
lista_inscritos = []
inscritos = {}

# Criar um Loop que só será finalizado
# caso o usuário digite 0 (zero)
while True:
    
    print('\n********| MENU |********')
    
    # Apresentação do MENU do Programa ao usuário
    menu = print('''
1 - Nova Inscrição (Curso de Python)
2 - Visualizar Inscrição
0 - Encerrar Programa
''')
    
    # Captação da Escolha apresentada pelo MENU
    escolha = int(input('Opção escolhida: '))
    
    # Verificação se a escolha se encaixa com os itens apresentados 
    # no MENU, caso não, apresentar mensagem de ERRO!
    if escolha > 2:
        print('Erro: digite uma opção válida! ')
     
    
    # Criação de uma nova inscrição
    if escolha == 1:
        
        # Declaração das variáveis
        nome = input('Nome: ')
        email = input('E-mail: ')
        telefone = input('Telefone: ')
        curso = 'Python'
        
        # Criação de um dicionário para armazenar os dados do inscrito
        inscritos = {
            'voucher' : uuid.uuid1(),
            'nome' : nome.title(),
            'email' : email,
            'telefone' : telefone,
            'curso' : curso
        }
        
        # Adicionando a inscrição na Lista dos Inscritos
        lista_inscritos.append(inscritos)
    
    # Verificar se o usuário desejar fazer uma consulta
    # no banco de dados dos inscritos, caso a banco esteja
    # vazio, apresentar mensagem de (Nenhuma inscrição cadastrada)
    if escolha == 2:
        if len(lista_inscritos) == 0:
            print('Nenhuma inscrição cadastrada.')
            continue
        
        # Caso já exista cadastrados, fazer a apresentação dos mesmos
        print('\n -------- LISTA DE INSCRITO(S) -------- \n')
        
        # Utilizar dois FOR para percorrer a Lista de Inscritos
        # e os dados destes. Fazer apresentação dos dados por 
        # intermédio de um Print formatado.
        for inscrito in lista_inscritos:
            for chave, valor in inscrito.items():
                print(f'{chave.upper()}: {valor}')
            print()
                
    # Se a escolha no MENU for 0 (zero), encerrar programa.
    if escolha == 0:
        print('\nPrograma Encerrado\n')
        break