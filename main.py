import random
import copy
gameConfigs = {'Tabuleiros': 0, 'Dificuldade': 0, 'Encerrar': []} #Dif = (F,M OU D)
gameStats = { 'Jogador 1': [['Nome', 0],['Jogada X']], 'Jogador 2': [['Nome', 0],['Jogada X']]}
#Encerrar recebe uma lista contendo [X,Y] se a opção selecionadar for por rodadas, sendo X a opção e Y o número de rodadas
def receberConfiguracoes(quantTabuleiros,dificuldade, encerramento, rodadas) :
    if quantTabuleiros == 1:
        gameConfigs['Tabuleiros'] = 1
    elif quantTabuleiros == 2:
        gameConfigs['Tabuleiros'] = 2
    else:
        return 'O jogo só pode ser jogado com 1 ou 2 tabuleiros! Digite uma quantidade válida.'

    if dificuldade == 'F':
        gameConfigs['Dificuldade'] = 3
    elif dificuldade == 'M':
        gameConfigs['Dificuldade'] = 4
    elif dificuldade == 'D':
        gameConfigs['Dificuldade'] = 5
    
    if encerramento == 1:
        gameConfigs['Encerrar'].append(encerramento)
        gameConfigs['Encerrar'].append(rodadas)
    elif encerramento == 2:
        gameConfigs['Encerrar'] = encerramento
    return quantTabuleiros, dificuldade, encerramento, rodadas

#Iniciando o game
menu = int(input('''
=== Selecione uma opção ========    

    [1] - Iniciar 
    [2] - Instruções
    [3] - Sair

================================    
'''))

while menu != 3:
    if menu == 2:
        print('Aqui jás instruções')
        menu = int(input('''
=== Selecione uma opção ========    

    [1] - Iniciar 
    [2] - Instruções
    [3] - Sair

================================    
'''))
    #Configurando o game
    elif menu == 1:
        quantTab = int(input('Digite a quantidade de tabuleiros a serem jogados: '))
        dificuldade = input('''Selecione a dificuldade:
        
=== Selecione a dificuldade ===

    [F] - Fácil (3x3)
    [M] - Médil (4x4)
    [D] - Difícil (5x5) 
    
================================    
''').upper()[0]
        
        finalizar = int(input('''Selecione o modo de encerramento da partida:
    [1] - Por número de rodadas
    [2] - Ao revelar completamente um dos tabuleiros
'''))
        if finalizar == 1:
            numRodadas = int(input('''Digite o número de rodadas:
'''))
        elif finalizar == 2:
            numRodadas = ''
    #Retornando as configurações para o dicionário
    receberConfiguracoes(quantTab, dificuldade,finalizar, numRodadas)
    jogador1Nick = input('''
================================  
Digite o nickname do jogador 1
================================  
''')
    gameStats['Jogador 1'][0][1] = jogador1Nick
    jogador2Nick = input('''
================================  
Digite o nickname do jogador 2
================================  
''')
    gameStats['Jogador 2'][0][1] = jogador2Nick
    menu = 3

print(gameConfigs)
print(gameStats)


