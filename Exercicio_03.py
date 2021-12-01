# Iniciar o programa com a explicação 
# do objetivo do jogo.

while True:
    
    print('  \n HOTEL DOS ANIMAIS \n  ')

    print('  !!! ATENÇÃO !!!\n ')

    print('''O nosso Hotel possui algumas restrições \nquanto a loca-lização do quarto do hóspede.
Fique atento ao que segue:''')

    print('''
• O RATO não pode ficar ao lado do GATO.
• O CÃO não pode ficar ao lado do OSSO.
• O GATO não pode ficar ao lado do CÃO.
• O QUEIJO não pode ficar ao lado do RATO.
''')

    # Criar um modelo representando a disposição 
    # dos quartos para situar o usuário
    quarto_modelo = ('''[ '1º' ,  '2º' ,  '3º' ,  '4º' ]\n[ '5º' ,  '6º' ,  '7º' ,  '8º' ]''')

    print('Abaixo temos a posição de cada quar-to:\n{}'.format(quarto_modelo))

    print('''
Os quartos com '*' representam os quartos indisponíveis, 
e os quartos com '-' representam os que podem ser ocupados. 
As letras nas células correspondem aos hóspedes:
    G – GATO
    C – CÃO
    R – RATO
    O – OSSO
    Q – QUEIJO''')

    print('''
Vamos para a 1ª FASE?

Nesta FASE, o jogador deve alocar o RATO e o GATO 
na seguinte matriz que representa os quartos: ''')

    # Lógica da Fase 1
    quarto_fase_1_modelo = ('''[ '*' ,  '*' ,  '-' ,  'G' ]\n[ 'R' ,  '-' ,  '*' ,  '*' ]''')
    print(quarto_fase_1_modelo)
    
    # Quarto da 1ª Fase com as opções corretas:
    quarto_1_certo = [6, 3]
    
    # Solicitar que o jogador escolhas os quartos para o RATO e o GA-TO:
    opcao_1_fase_1 = int(input('Em qual quarto você quer colocar o RATO? '))
    opcao_2_fase_1 = int(input('Em qual quarto você quer colocar o GATO? '))
    
    # Armazenar a resposta dada pelo usuário
    fase_1 = [opcao_1_fase_1, opcao_2_fase_1]
    
    # Nesta etapa iremos comparar a resposta dada pelo usuário 
    # com a resposta correta (quarto_1_certo = [6, 3])
    if fase_1 != quarto_1_certo: 
        print(10*'x~')
        print('|   Você Perdeu!   |')
        print(10*'x~')
        break
    
    else:  
        print(9*'=-')
        print('|  Você Ganhou!  |')
        print(9*'=-')
        
        # Lógica da Fase 2
        print('''
Vamos para a 2ª FASE!
Nesta FASE, o jogador deve alocar o 1º CÃO, o 2º CÃO e o GATO 
na seguinte matriz que representa os quartos:''')
        # Apresentar um modelo da disposição dos quartos
        quarto_fase_2_modelo = ('''[ '-' ,  '*' ,  '*' ,  '*' ]\n[ '*' ,  'C' ,  '-' ,  '-' ]''')
        print(quarto_fase_2_modelo)
        
        # Solicitar que o jogador escolhas os quartos para o CÃO, CÃO e o OSSO:
        opcao_1_fase_2 = int(input('Em qual quarto você quer colocar o 1º CÃO? '))
        opcao_2_fase_2 = int(input('Em qual quarto você quer colocar o 2º CÃO? '))
        opcao_3_fase_2 = int(input('Em qual quarto você quer colocar o OSSO? '))
        
        # Nesta etapa iremos novamente comparar a resposta dada pelo usuário 
        # com a resposta correta.
        if opcao_1_fase_2 == 1: # CÃO
            print(10*'x~')
            print('|   Você Perdeu!   |')
            print(10*'x~')
            break
            
        if opcao_2_fase_2 == 1:  # CÃO
            print(10*'x~')
            print('|   Você Perdeu!   |')
            print(10*'x~')
            break
        
        if opcao_3_fase_2 == 1:  #  OSSO
            print(9*'=-')
            print('|  Você Ganhou!  |')
            print(9*'=-')
            
            # Lógica da Fase 3
            print('''
Vamos para a 3ª FASE!
Nesta FASE, o jogador deve alocar o GATO, o RATO e o OSSO 
na seguinte matriz que representa os quartos:''')    
            # Apresentar um modelo da disposição dos quartos
            quarto_fase_3_modelo = ('''[ '-' ,  '*' ,  '*' ,  '*' ]\n[ '-' ,  'G' ,  '-' ,  '*' ]''')
            print(quarto_fase_3_modelo)
            
            # Solicitar que o jogador escolhas os quartos para o GA-TO, RATO e o OSSO:
            opcao_1_fase_3 = int(input('Em qual quarto você quer co-locar o 1º GATO? '))
            opcao_2_fase_3 = int(input('Em qual quarto você quer co-locar o RATO? '))
            opcao_3_fase_3 = int(input('Em qual quarto você quer co-locar o OSSO? '))
            
            if opcao_1_fase_3 == 1: # GATO
                print(10*'x~')
                print('|   Você Perdeu!   |')
                print(10*'x~')
                break
                
            if opcao_2_fase_3 == 5 or opcao_2_fase_3 == 7: # RATO
                print(10*'x~')
                print('|   Você Perdeu!   |')
                print(10*'x~')
                break
                
            if opcao_3_fase_3 == 5 or opcao_2_fase_3 == 7: # OSSO
                print(9*'=-')
                print('|  Você Ganhou!  |')
                print(9*'=-')

            
            # Lógica da Fase 4
                print('''
Vamos para a 4ª e última FASE!
Nesta FASE, o jogador deve alocar o 1º QUEIJO, o 2º QUEIJO e o OSSO 
na seguinte matriz que representa os quartos:''')
                # Apresentar um modelo da disposição dos quartos
                quarto_fase_4_modelo = ('''[ '-' ,  '-' ,  '-' ,  '*' ]\n[ '*' ,  'R' ,  '*' ,  '*' ]''')
                print(quarto_fase_4_modelo)
            
            # Solicitar que o jogador escolhas os quartos para o 1º QUEIJO, 2º QUEIJO e o OSSO:
                opcao_1_fase_4 = int(input('Em qual quarto você quer colocar o QUEIJO? '))
                opcao_2_fase_4 = int(input('Em qual quarto você quer colocar o 2º QUEIJO? '))
                opcao_3_fase_4 = int(input('Em qual quarto você quer colocar o OSSO? '))
            
                if opcao_1_fase_4 == 2: # QUEIJO
                    print(10*'x~')
                    print('|   Você Perdeu!   |')
                    print(10*'x~')
                    break
                
                if opcao_2_fase_4 == 2: # QUEIJO
                    print(10*'x~')
                    print('|   Você Perdeu!   |')
                    print(10*'x~')
                    break
                
                if opcao_3_fase_4 == 2: # OSSO
                    print(9*'=-')
                    print('|  Você Ganhou!  |')
                    print(9*'=-')
    # Perguntar se desejar encerrar o programa, 
    # se resposta for 0 (zero) fazer um Break
    resp = int(input('Deseja jogar Novamente?  [0] - NÃO     [1] - SIM  '))
    
    if resp == 1:
        continue
    else:
        print('Até a Próxima \o/')
        break
