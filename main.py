import random
gameConfigs = {'Tabuleiros': 0, 'Dificuldade': 0, 'Encerrar': []} #Dif = (F,M OU D)
gameStats = { 'Jogador 1': [['Nome', 0],['Jogada X']], 'Jogador 2': [['Nome', 0],['Jogada X']]}
#Encerrar recebe uma lista contendo [X,Y] se a opção selecionadar for por rodadas, sendo X a opção e Y o número de rodadas

#Recebendo as configurações do jogo
def receberConfiguracoes(quantTabuleiros,dificuldade, encerramento, rodadas) :
    if quantTabuleiros == 1:
        gameConfigs['Tabuleiros'] = 1
    elif quantTabuleiros == 2:
        gameConfigs['Tabuleiros'] = 2
    else:
        return 'O jogo só pode ser jogado com 1 ou 2 tabuleiros! Digite uma quantidade válida.'

    if dificuldade == 'F':
        gameConfigs['Dificuldade'] = 30
    elif dificuldade == 'M':
        gameConfigs['Dificuldade'] = 60
    elif dificuldade == 'D':
        gameConfigs['Dificuldade'] = 100
    
    if encerramento == 1:
        gameConfigs['Encerrar'].append(encerramento)
        gameConfigs['Encerrar'].append(rodadas)
    elif encerramento == 2:
        gameConfigs['Encerrar'] = encerramento
    return quantTabuleiros, dificuldade, encerramento, rodadas


#Criando a matriz do jogo 
def criarMatriz(boardNumbers, dificulty):
    matriz = []
    #Shuffle problem
    oldMatriz = []
    for i in range(1,dificulty+1):
        matriz.append(i)
        random.shuffle(matriz)
    oldMatriz = matriz
    if boardNumbers == 1:
        board = [[matriz[0],matriz[1],matriz[2]],[matriz[3],matriz[4],matriz[5]],[matriz[6],matriz[7],matriz[8]]]
        if dificulty == 60:
            board[0].append(matriz[9]),board[1].append(matriz[10]), board[2].append(matriz[11]) 
            board.append([matriz[12], matriz[13], matriz[14], matriz[15]])   
        elif dificulty == 100:
            board[0].append(matriz[9]),board[0].append(matriz[10]), board[1].append(matriz[11]), board[1].append(matriz[12]), board[2].append(matriz[13]),board[2].append(matriz[14])
            board.append([matriz[15], matriz[16], matriz[17], matriz[18], matriz[19]]),board.append([matriz[20], matriz[21], matriz[22], matriz[23], matriz[24]]) 
        return board
    elif boardNumbers == 2:
        board = [[matriz[0],matriz[1],matriz[2]],[matriz[3],matriz[4],matriz[5]],[matriz[6],matriz[7],matriz[8]]]
        random.shuffle(matriz)
        secondBoard = [[matriz[0],matriz[1],matriz[2]],[matriz[3],matriz[4],matriz[5]],[matriz[6],matriz[7],matriz[8]]]
        #MÉTODO COPY
        if dificulty == 60:
            board[0].append(oldMatriz[9]),board[1].append(oldMatriz[10]), board[2].append(oldMatriz[11]) 
            board.append([oldMatriz[12], oldMatriz[13], oldMatriz[14], oldMatriz[15]])  
            secondBoard[0].append(matriz[9]),secondBoard[1].append(matriz[10]), secondBoard[2].append(matriz[11])
            secondBoard.append([matriz[12], matriz[13], matriz[14], matriz[15]])   
        elif dificulty == 100:
            board[0].append(oldMatriz[9]),board[0].append(oldMatriz[10]), board[1].append(oldMatriz[11]), board[1].append(oldMatriz[12]), board[2].append(oldMatriz[13]),board[2].append(oldMatriz[14])    
            board.append([oldMatriz[15], oldMatriz[16], oldMatriz[17], oldMatriz[18], oldMatriz[19]]), board.append([oldMatriz[20], oldMatriz[21], oldMatriz[22], oldMatriz[23], oldMatriz[24]])
            secondBoard[0].append(matriz[9]), secondBoard[0].append(matriz[10]), secondBoard[1].append(matriz[11]), secondBoard[1].append(matriz[12]), secondBoard[2].append(matriz[13]), secondBoard[2].append(matriz[14])
            secondBoard.append([matriz[15], matriz[16], matriz[17], matriz[18], matriz[19]]), secondBoard.append([matriz[20], matriz[21], matriz[22], matriz[23], matriz[24]])    
        return board, secondBoard

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
print(criarMatriz(gameConfigs['Tabuleiros'], gameConfigs['Dificuldade']))
