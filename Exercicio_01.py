# Criar uma estrutura de repetição While em True,
# quando o usuário selecionar que não deseja fazer 
# uma nova consulta, o programa fará um Breack
while True:
    
    # Iniciar dando as boas vindas e ambientando o usuário 
    # com a Funcionalidade do Programa
    welcome = print('Olá, Seja Bem-Vindo!\nAqui você poderá consultar em qual ano o seu filho está matriculado. ')

    # Definir Duas variáveis (Nome e Idade) a serem usadas 
    # nas estruturas de seleção ou decisão do programa
    nome_filho = input('Nos forneça o nome do seu Filho(a): ')

    idade_filho = int(input('Quantos anos ele(a) tem? '))

    # Verificar através das estruturas de seleção ou decisão 
    # utilizando a idade do filho(a), qual o nível de Ensino na qual ela se enquadra
    if (idade_filho >= 1 and idade_filho <= 5):
        print('{} por ter {} ano(s), está matriculado(a) na Educação Infantil.\n'.format(nome_filho.title(), idade_filho))

    elif (idade_filho >= 6 and idade_filho <= 10):
        print('{} por ter {} anos, está matriculado(a) no \nEnsino Fundamental Anos Iniciais (Antigo Ensino Fundamental I).\n'.format(nome_filho.title(), idade_filho))

    elif (idade_filho >= 11 and idade_filho <= 14):
        print('{} por ter {} anos, está matriculado(a) no \nEnsino Fundamental Anos Finais (Antigo Ensino Fundamental II).\n'.format(nome_filho.title(), idade_filho))

    elif (idade_filho >= 15 and idade_filho <= 18):
        print('{} por ter {} anos, está matriculado(a) no Ensino Mé-dio.\n'.format(nome_filho.title(), idade_filho))

    else:
        print('{} por ter {} anos, provavelmente já concluiu o Ensino Médio \o/\n'.format(nome_filho.title(), idade_filho))

     # Perguntar ao usuário se ele deseja fazer uma nova consulta
    print('Deseja fazer uma nova Consulta? ')

    # Criar uma variável para armazenar a resposta da pergunta ante-rior
    resp = int(input('0 - NÃO    1 - SIM: '))
    
    # Com o uso de uma condição após a resposta do usuário
    # podemos fazer a quebra do loop.
    if resp == 0:
        break
    
print('\nPrograma encerrado!\n')