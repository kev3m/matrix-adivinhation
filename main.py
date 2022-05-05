import random
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

def createMatrice(boardNumbers, difficulty):
    numList = []
    interval = 0
    if difficulty == 3:
        interval = 30
    elif difficulty == 4:
        interval = 60
    elif difficulty == 5:
        interval = 100

    for i in range(1, interval + 1):
        numList.append(i)
    random.shuffle(numList)
    copyofNumList = numList.copy()
    
    matrice = []
    secondMatrice = []

    for i in range(difficulty):
            numbers = random.sample(numList, difficulty)
            for j in numbers:
                numList.pop(numList.index(j))
            matrice.append(numbers)

    if boardNumbers == 2:
        for i in range(difficulty):
            numbers = random.sample(copyofNumList, difficulty)
            for j in numbers:
                copyofNumList.pop(copyofNumList.index(j))
            secondMatrice.append(numbers)
    return matrice, secondMatrice
def createFakeMatrice(difficulty):
    fakeMatriz = []

    for i in range(difficulty):
        invVar = []
        for j in range(difficulty):
            invVar.append(0)
        fakeMatriz.append(invVar)
    return fakeMatriz       

def somarMatriz(boardNumbers, difficulty):
    c1,c2,c3 = (board[0][0] + board[1][0] + board[2][0]), (board[0][1] + board[1][1] + board[2][1]), (board[0][2] + board[1][2] + board[2][2])
    l1, l2, l3 = (sum(board[0])), (sum(board[1])), (sum(board[2]))
    somasTab = {'Colunas': [c1,c2,c3], 'Linhas': [l1,l2,l3] }
    if boardNumbers == 2:
        c_1,c_2,c_3 = (board2[0][0] + board2[1][0] + board2[2][0]), (board2[0][1] + board2[1][1] + board2[2][1]), (board2[0][2] + board2[1][2] + board2[2][2])
        l_1, l_2, l_3 = (sum(board2[0])), (sum(board2[1])), (sum(board2[2]))
        somasTab = {'Colunas': [c1,c2,c3], 'Linhas': [l1,l2,l3] 
            ,'ColunasT2': [c_1,c_2,c_3], 'LinhasT2': [l_1,l_2,l_3]} 

    if difficulty == 4:
        c1 += board[3][0]
        c2 += board[3][1]
        c3 += board[3][2]
        c4 = board[0][3] + board[1][3] + board[2][3] + board[3][3]
        l4 = sum(board[3])
        somasTab['Colunas'].append(c4), somasTab['Linhas'].append(l4)
        if boardNumbers == 2:  
            c_1 += board2[3][0]
            c_2 += board2[3][1]
            c_3 += board2[3][2]
            c_4 = board2[0][3] + board2[1][3] + board2[2][3] + board2[3][3]
            l_4 = sum(board2[3]) 
            somasTab['ColunasT2'].append(c_4), somasTab['LinhasT2'].append(l_4)     
    elif dif == 5:
        c1 += board[3][0] + board[4][0]
        c2 += board[3][1] + board[4][1]
        c3 += board[3][2] + board[4][2]
        c4 = board[0][3] + board[1][3] + board[2][3] + board[3][3] + board[4][3]
        c5 = board[0][4] + board[1][4] + board[2][4] + board[3][4] + board[4][4] 
        l4 = sum(board[3])
        l5 = sum(board[4])
        somasTab = {'Colunas': [c1,c2,c3,c4,c5], 'Linhas': [l1,l2,l3,l4,l5] }
        if boardNumbers == 2:  
            c_1 += board2[3][0]
            c_2 += board2[3][1]
            c_3 += board2[3][2]
            c_4 = board2[0][3] + board2[1][3] + board2[2][3] + board2[3][3] + board2[4][3]
            c_5 = board2[0][4] + board2[1][4] + board2[2][4] + board2[3][4] + board2[4][4]
            l_4 = sum(board2[3]) 
            l_5 = sum(board2[4])
            somasTab = {'Colunas': [c1,c2,c3,c4,c5], 'Linhas': [l1,l2,l3,l4,l5] 
            ,'ColunasT2': [c_1,c_2,c_3,c_4,c_5], 'LinhasT2': [l_1,l_2,l_3,l_4,l_5]}           
    return somasTab


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
        dificuldade = int(input('''Selecione a dificuldade:
        
=== Selecione a dificuldade ===

    [3] - Fácil (3x3)
    [4] - Médil (4x4)
    [5] - Difícil (5x5) 
    
================================    
'''))
        
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
    board, board2 = createMatrice(quantTab,dificuldade)
    fakeMatrice = createFakeMatrice(dificuldade)
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
    #Iniciando o jogo com um tabuleiro
    if gameConfigs['Tabuleiros'] == 1:
        print(f'''O jogo foi iniciado com um tabuleiro para dois jogadores
        Boa sorte {gameStats['Jogador 1'][0][1]} e {gameStats['Jogador 2'][0][1]}''')
        #if gameConfigs['Encerrar'] == 2:
        print(f'''
======Tabela guia para escolha das opções======
-------------
| x | x | x | > l1
| x | x | x | > l2
| x | x | x | > l3 
-------------
^   ^   ^
c1  c2  c3
''')    
        p1Play = input(f'''{gameStats['Jogador 1'][0][1]} | Digite a linha ou coluna que deseja chutar o valor: ''')
        p1PlaySum = int(input(f'''{gameStats['Jogador 1'][0][1]} | Digite o valor que deseja chutar: '''))
        p2Play = input(f'''{gameStats['Jogador 2'][0][1]} | Digite a linha ou coluna que deseja chutar o valor: ''')
        p2PlaySum = int(input(f'''{gameStats['Jogador 2'][0][1]} | Digite o valor que deseja chutar: '''))

        



        



print(gameConfigs)
print(gameStats)
print(board)
print(board2)


