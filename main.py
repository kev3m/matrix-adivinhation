import random
gameConfigs = {'Tabuleiros': 0, 'Dificuldade': 0, 'Encerrar': 0} #Dif = (F,M OU D)
gameStats = { 'Jogador 1': [['Nome', 0],[[], []]], 'Jogador 2': [['Nome', 0],[[], []]]}
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
        gameConfigs['Encerrar'] = rodadas
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

    lines = matrice.copy()

    if boardNumbers == 2:
        for i in range(difficulty):
            numbers = random.sample(copyofNumList, difficulty)
            for j in numbers:
                copyofNumList.pop(copyofNumList.index(j))
            secondMatrice.append(numbers)      
    return matrice, secondMatrice, lines
def createFakeMatrice(difficulty):
    fakeMatriz = []

    for i in range(difficulty):
        invVar = []
        for j in range(difficulty):
            invVar.append(0)
        fakeMatriz.append(invVar)
    return fakeMatriz       
def createColumns(mat1, mat2):
    colunas = []
    colunas2 = []
    for i in range(len(mat1)):
        col = []
        for j in mat1:
            col.append(j[i])
        colunas.append(col)

    for i in range(len(mat2)):
        col = []
        for j in mat2:
            col.append(j[i])
        colunas2.append(col)
    return colunas, colunas2


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
    elif difficulty == 5:
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

def atribuirValoresTabela(p1P, p2P,sumtab):
    if p1P == 'c1':
        p1P = sumtab['Colunas'][0]
    elif p1P == 'c2':
        p1P = sumtab['Colunas'][1]
    elif p1P == 'c3':
        p1P = sumtab['Colunas'][2]
    elif p1P == 'c4':
        p1P = sumtab['Colunas'][3]
    elif p1P == 'c5':
        p1P = sumtab['Colunas'][4]
    elif p1P == 'l1':
        p1P = sumtab['Linhas'][0]
    elif p1P == 'l2':
        p1P = sumtab['Linhas'][1]
    elif p1P == 'l3':
        p1P = sumtab['Linhas'][2]
    elif p1P == 'l4':
        p1P = sumtab['Linhas'][3]
    elif p1P == 'l5':
        p1P = sumtab['Linhas'][4]

    if p2P == 'c1':
        p2P = sumtab['Colunas'][0]
    elif p2P =='c2':
        p2P = sumtab['Colunas'][1]
    elif p2P =='c3':
        p2P = sumtab['Colunas'][2]
    elif p2P =='c4':
        p2P = sumtab['Colunas'][3]
    elif p2P =='c5':
        p2P = sumtab['Colunas'][4]
    elif p2P == 'l1':
        p2P = sumtab['Linhas'][0]
    elif p2P == 'l2':
        p2P = sumtab['Linhas'][1]
    elif p2P == 'l3':
        p2P = sumtab['Linhas'][2]
    elif p2P == 'l4':
        p2P = sumtab['Linhas'][3]
    elif p2P == 'l5':
        p2P = sumtab['Linhas'][4]
    return p1P,p2P    

def intervalVerifier(p1P,p1Sum, p2P, p2Sum):
    if p1P > p1Sum:#Num Original | Num escolhido pelo user
        p1P = (p1P - p1Sum)
        maiorOumenor = False
    elif p1P < p1Sum:
        p1P = (p1Sum - p1P)
        maiorOumenor = True
    elif p1P == p1Sum:
        p1P = 0
        maiorOumenor = True
    if p2P > p2Sum: #p2p = num da casa chutada | p2sum = soma chutada
        p2P = (p2P - p2Sum)
        maiorOumenor2 = False
    elif p2P < p2Sum:
        p2P = (p2Sum - p2P)
        maiorOumenor2 = True
    elif p2P == p2Sum:
        p2P = 0
        maiorOumenor2 = True
    #Retorna  o intervalo
    return p1P, p2P, maiorOumenor, maiorOumenor2

def roundWinner(p1P, p2P,maiMen1, maiMen2):
    if p1P < p2P and p1P != 0:
        return 1, maiMen1
    elif p1P > p2P:
        return 2, maiMen2
     #mesma aproximação   
    elif p1P == p2P and p1P != 0 and p2P != 0:
        maiMen1 = maiMen2 = 'Mesma aproximação'
        return 3, maiMen1, maiMen2
    elif p1P == 0:
        maiMen1 = 'P1 Acertou a soma'
        return 4, maiMen1
    elif p2P == 0:
        maiMen2 = 'P2 Acertou a soma'
        return 5, maiMen2
    elif p1P == 0 and p1P == 0:
        maiMen1 = maiMen2 = 'Ambos acertaram a soma'
        return 6, maiMen1, maiMen2

def returnWinnePlay(p1P, p2P, roundWinner, maiMen1, maiMen2):
        if roundWinner == 1 or roundWinner == 4:
            return p1P, maiMen1
        elif roundWinner == 2 or roundWinner == 5:
            return p2P, maiMen2
        elif roundWinner == 3 or roundWinner == 6:
            return p1P, p2P, maiMen1, maiMen2 

#Remove os nums da linha/coluna
def returnNumToSwap(winnerPlay, winnerPlayCase,maiorOumenor, maiorOumenor2,coluna,playsTab, linha):
    if winnerPlay == 1 or winnerPlay == 4:
        if winnerPlayCase[0] == 'c':
            indexcolumn = playsTab[0].index(winnerPlayCase)
            if winnerPlay == 1:
                if maiorOumenor == True:
                    swapNum = max(coluna[indexcolumn])
                    coluna[indexcolumn].remove(swapNum)
                elif maiorOumenor == False:
                    swapNum = min(coluna[indexcolumn])
                    coluna[indexcolumn].remove(swapNum)
            elif winnerPlay == 4:
                #Não da pra usar pop pois remove a matriz               
                swapNum = coluna[indexcolumn].copy()  
                coluna[indexcolumn].clear()        
        elif winnerPlayCase[0] == 'l':
            indexcolumn = playsTab[1].index(winnerPlayCase)
            if winnerPlay == 1:
                if maiorOumenor == True:
                    swapNum = max(linha[indexcolumn])
                    linha[indexcolumn].remove(swapNum)
                elif maiorOumenor == False:
                    swapNum = min(linha[indexcolumn])
                    linha[indexcolumn].remove(swapNum)
            elif winnerPlay == 4:
                swapNum = linha[indexcolumn].copy()  
                linha[indexcolumn].clear()    
        return swapNum, linha

    elif winnerPlay == 2 or winnerPlay == 5:
        if winnerPlayCase[0] == 'c':
            indexcolumn = playsTab[0].index(winnerPlayCase)
            if winnerPlay == 2:
                if maiorOumenor2 == True:
                    swapNum = max(coluna[indexcolumn])
                    coluna[indexcolumn].remove(swapNum)
                elif maiorOumenor2 == False:
                    swapNum = min(coluna[indexcolumn]) 
                    coluna[indexcolumn].remove(swapNum)
            elif winnerPlay == 5:
                swapNum = linha[indexcolumn].copy()  
                coluna[indexcolumn].clear() 

        elif winnerPlayCase[0] == 'l':
            indexcolumn = playsTab[1].index(winnerPlayCase)
            if winnerPlay == 2:
                if maiorOumenor2 == True:
                    swapNum = max(linha[indexcolumn])
                    linha[indexcolumn].remove(swapNum)
                elif maiorOumenor2 == False:
                    swapNum = min(linha[indexcolumn])
                    linha[indexcolumn].remove(swapNum)
            elif winnerPlay == 5:
                swapNum = linha[indexcolumn].copy()  
                linha[indexcolumn].clear() 
        return swapNum, linha

def searchindex(defaultboard,num):
    #Verificar se num é uma lista ou não
    if isinstance(num,list) == False:
        for i in defaultboard:
            if num in i:
                return defaultboard.index(i), i.index(num)
    elif isinstance(num,list) == True:
        whichList = []
        whichListPos = []
        for j in num:
            for i in defaultboard:
                if j in i:
                    whichList.append(defaultboard.index(i))
                    whichListPos.append(i.index(j))
        return whichList, whichListPos



def tableSwap(numero,fakemat,matrizInd, numInd):
    if isinstance(numero,list) == False:
        fakemat[matrizInd][numInd] = numero
        return fakemat
    elif isinstance(numero,list) == True:
        #Indica que é uma linha
        if isinstance(matrizInd,list) == False:
            for i in range(len(numero)):
                matrizIndice = matrizInd
                numIndice = numInd[i]
                fakemat[matrizIndice][numIndice] = numero[i]
        #Indica que é uma coluna        
        else:
            for i in range(len(numero)):
                matrizIndice = matrizInd[i]
                numIndice = numInd[i]
                fakemat[matrizIndice][numIndice] = numero[i]
        return fakemat



def statusReceiver(p1P,p1Sum, p2P, p2Sum,statsTab):
    statsTab['Jogador 1'][1][0].append(p1P)
    statsTab['Jogador 1'][1][1].append(p1Sum)
    statsTab['Jogador 2'][1][0].append(p2P)
    statsTab['Jogador 2'][1][1].append(p2Sum)

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
        quantTab = int(input('''
=== Selecione a quantidade de tabuleiros ===

    [1] - Tabuleiro único
    [2] - 1 Tabuleiro para cada jogador
    
============================================ 
'''))
        if quantTab == 2:
            print('''
=====================================
 ________________
|                |
|    Falha na    | 
|     Matrix     |
|________________| 
 ∧＿∧  ||   Pedimos perdão!
( ´ω`) ||   Apenas um tabuleiro está   
/     づ    disponível no momento   
=====================================
            ''')
            quantTab == 1
        dificuldade = int(input('''Selecione a dificuldade:
        
=== Selecione a dificuldade ===

    [3] - Fácil (3x3)
    [4] - Médil (4x4)
    [5] - Difícil (5x5) 
    
================================    
'''))

        while dificuldade != 3 and dificuldade != 4 and dificuldade != 5:
            print('Falha na matrix! Dificuldade inválida')
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
        
        while finalizar != 1 and finalizar != 2:
            print('Falha na matrix! Encerramento inválido')
            finalizar = int(input('''Selecione o modo de encerramento da partida:
    [1] - Por número de rodadas
    [2] - Ao revelar completamente um dos tabuleiros
'''))

        if finalizar == 1:
            numRodadas = int(input('''Digite o número de rodadas: 
'''))       
            while numRodadas % 2 == 0:
                print('Falha na matrix! O número de rodadas deve ser impar para evitar impates.')
                numRodadas = int(input('''Digite o número de rodadas:        
'''))     
        elif finalizar == 2:
            numRodadas = ''
    #Retornando as configurações para o dicionário
    plays = [['c1', 'c2', 'c3', 'c4', 'c5'], ['l1', 'l2', 'l3', 'l4', 'l5']]
    contadorRodadas = 0
    receberConfiguracoes(quantTab, dificuldade,finalizar, numRodadas)

    board, board2, lines = createMatrice(quantTab,dificuldade)
    print(board)
  
    #PR evitar o bug das linhas
   
    column, column2 = createColumns(board, board2)
    #Matriz
    
    sumtab = somarMatriz(quantTab, dificuldade)
    fakeMatrice = createFakeMatrice(dificuldade)
    jogador1Nick = input('''
================================  
Digite o nickname do jogador 1
================================  
''')
    gameStats['Jogador 1'][0][0] = jogador1Nick
    jogador2Nick = input('''
================================  
Digite o nickname do jogador 2
================================  
''')
    gameStats['Jogador 2'][0][0] = jogador2Nick
    menu = 3
    #Iniciando o jogo com um tabuleiro
    if gameConfigs['Tabuleiros'] == 1:
        print(f'''O jogo foi iniciado com um tabuleiro para dois jogadores
        Boa sorte {gameStats['Jogador 1'][0][0]} e {gameStats['Jogador 2'][0][0]}''')
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
        if finalizar == 1:
            while contadorRodadas < gameConfigs['Encerrar']:
                p1Play = input(f'''{gameStats['Jogador 1'][0][0]} | Digite a linha ou coluna que deseja chutar o valor: ''')
                if dificuldade == '3':
                    while p1Play != 'c1' and p1Play != 'c2' and p1Play != 'c3' and p1Play != 'l1' and p1Play != 'l2' and p1Play != 'l3':
                        p1Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a dificuldade escolhida |Até c3 ou l3|: ''')
                elif dificuldade == '4':
                    while p1Play != 'c1' and p1Play != 'c2' and p1Play != 'c3' and p1Play != 'c4' and p1Play != 'l1' and p1Play != 'l2' and p1Play != 'l3' and p1Play != 'l4': 
                        p1Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a dificuldade escolhida |Até c4 ou l4|: ''')
                elif dificuldade == '5':
                    while p1Play != 'c1' and p1Play != 'c2' and p1Play != 'c3' and p1Play != 'c4' and p1Play != 'c5' and p1Play != 'l1' and p1Play != 'l2' and p1Play != 'l3' and p1Play != 'l4' and p1Play != 'l5': 
                        p1Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a dificuldade escolhida |Até c5 ou l5|: ''')
                
                p1PlaySum = int(input(f'''{gameStats['Jogador 1'][0][0]} | Digite o valor que deseja chutar: '''))
                
                p2Play = input(f'''{gameStats['Jogador 2'][0][0]} | Digite a linha ou coluna que deseja chutar o valor: ''')
                if dificuldade == '3':
                    while p2Play != 'c1' and p2Play != 'c2' and p2Play != 'c3' and p2Play != 'l1' and p2Play != 'l2' and p2Play != 'l3':
                        p2Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a dificuldade escolhida |Até c3 ou l3|: ''')
                elif dificuldade == '4':
                    while p2Play != 'c1' and p2Play != 'c2' and p2Play != 'c3' and p2Play != 'c4' and p2Play != 'l1' and p2Play != 'l2' and p2Play != 'l3' and p2Play != 'l4': 
                        p2Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a dificuldade escolhida |Até c4 ou l4|: ''')
                elif dificuldade == '5':
                    while p2Play != 'c1' and p2Play != 'c2' and p2Play != 'c3' and p2Play != 'c4' and p2Play != 'c5' and p2Play != 'l1' and p2Play != 'l2' and p2Play != 'l3' and p2Play != 'l4' and p2Play != 'l5': 
                        p2Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a dificuldade escolhida |Até c5 ou l5|: ''')
               
                p2PlaySum = int(input(f'''{gameStats['Jogador 2'][0][0]} | Digite o valor que deseja chutar: '''))

                p1pTabel, p2pTabel = atribuirValoresTabela(p1Play,p2Play,sumtab)
                interval1, interval2,maiMen1, maiMen2= intervalVerifier(p1pTabel, p1PlaySum, p2pTabel, p2PlaySum)
                roundWin, maiorOumenor = roundWinner(interval1,interval2,maiMen1,maiMen2)
                statusReceiver(p1Play, p1PlaySum, p2Play, p2PlaySum, gameStats)
                winnerplay, maiorOuMen = returnWinnePlay(p1Play, p2Play, roundWin, maiMen1, maiMen2)
                numToSwap, matrizLimpa = returnNumToSwap(roundWin,winnerplay,maiMen1, maiMen2,column, plays, lines)
                matind, numind = searchindex(board,numToSwap)
                print(board)
                fakematr = tableSwap(numToSwap,fakeMatrice,matind,numind)
                fakeMatrice = fakematr
                
                
                print(f'''
 ===========Status da rodada===========    
                ''')
                if roundWin == 1:
                    print('O jogador 1 foi o vencedor da rodada')
                    gameStats['Jogador 1'][0][1] += 1
                    if maiorOuMen == True:
                        print('O valor chutado é maior que a soma')    
                    else:
                        print('O valor chutado é menor que a soma') 

                elif roundWin == 2:
                    print('O jogador 2 foi o vencedor da rodada')
                    gameStats['Jogador 2'][0][1] += 1
                    if maiorOuMen == True:
                        print('O valor chutado é maior que a soma')    
                    else:
                        print('O valor chutado é menor que a soma') 

                elif roundWin == 3:
                    print('Os dois jogadores possuem a mesma aproximação, ambos ganharam!')
                    gameStats['Jogador 1'][0][1] += 1
                    gameStats['Jogador 2'][0][1] += 1

                elif roundWin == 4:
                    print('O jogador 1 acertou a soma em cheio! Todas as casas da respectiva linha/coluna serão reveladas')

                #########FAZER PONTUAÇÃO #########FAZER PONTUAÇÃO #########FAZER PONTUAÇÃO
                elif roundWin == 5:
                    print('O jogador 2 acertou a soma em cheio! Todas as casas da respectiva linha/coluna serão reveladas')
                elif roundWin == 6:
                    print('Os dois jogadores acertaram a soma! Verdadeiros mestres da matriz.')
                #########FAZER PONTUAÇÃO #########FAZER PONTUAÇÃO #########FAZER PONTUAÇÃO
                
                for i in fakematr:
                    print(i)

                print(f'''
{gameStats['Jogador 1'][0][0]} | Possui {gameStats['Jogador 1'][0][1]} Casas Reveladas       
{gameStats['Jogador 2'][0][0]} | Possui {gameStats['Jogador 2'][0][1]} Casas Reveladas       
                ''')

                for i in range(len(gameStats['Jogador 1'][1][0])):
                    quadPlay = gameStats['Jogador 1'][1][0][i]
                    numSumPlay = gameStats['Jogador 1'][1][1][i]
                    print(f'''
{i + 1}º Rodada | {gameStats['Jogador 1'][0][0]}
Escolheu a jogada {quadPlay} de soma {numSumPlay}''')
                for i in range(len(gameStats['Jogador 2'][1][0])):
                    quadPlay = gameStats['Jogador 2'][1][0][i]
                    numSumPlay = gameStats['Jogador 2'][1][1][i]
                    print(f'''
{i + 1}º Rodada | {gameStats['Jogador 2'][0][0]}
Escolheu a jogada {quadPlay} de soma {numSumPlay} 

    ''')
                contadorRodadas += 1
        elif finalizar == 2:   
            while fakeMatrice != board:
                p1Play = input(f'''{gameStats['Jogador 1'][0][0]} | Digite a linha ou coluna que deseja chutar o valor: ''')
                p1PlaySum = int(input(f'''{gameStats['Jogador 1'][0][0]} | Digite o valor que deseja chutar: '''))
                p2Play = input(f'''{gameStats['Jogador 2'][0][0]} | Digite a linha ou coluna que deseja chutar o valor: ''')
                p2PlaySum = int(input(f'''{gameStats['Jogador 2'][0][0]} | Digite o valor que deseja chutar: '''))

                p1pTabel, p2pTabel = atribuirValoresTabela(p1Play,p2Play,sumtab)
                interval1, interval2,maiMen1, maiMen2= intervalVerifier(p1pTabel, p1PlaySum, p2pTabel, p2PlaySum)
                roundWin, maiorOumenor = roundWinner(interval1,interval2,maiMen1,maiMen2)

                statusReceiver(p1Play, p1PlaySum, p2Play, p2PlaySum, gameStats)
                
                winnerplay, maiorOuMen = returnWinnePlay(p1Play, p2Play, roundWin, maiMen1, maiMen2)
                numToSwap = returnNumToSwap(roundWin,winnerplay,maiMen1, maiMen2,column, plays, lines)
                matind, numind = searchindex(board,numToSwap)
                fakematr = tableSwap(numToSwap,fakeMatrice,matind,numind)
                fakeMatrice = fakematr
                
                
                print(f'''
        ===========Status da rodada===========    
                ''')
                if roundWin == 1:
                    print('O jogador 1 foi o vencedor da rodada')
                    gameStats['Jogador 1'][0][1] += 1
                    if maiorOuMen == True:
                        print('O valor chutado é maior que a soma')    
                    else:
                        print('O valor chutado é menor que a soma') 

                elif roundWin == 2:
                    print('O jogador 2 foi o vencedor da rodada')
                    gameStats['Jogador 2'][0][1] += 1
                    if maiorOuMen == True:
                        print('O valor chutado é maior que a soma')    
                    else:
                        print('O valor chutado é menor que a soma') 

                elif roundWin == 3:
                    print('Os dois jogadores possuem a mesma aproximação, ambos ganharam!')
                    gameStats['Jogador 1'][0][1] += 1
                    gameStats['Jogador 2'][0][1] += 1

                elif roundWin == 4:
                    print('O jogador 1 acertou a soma em cheio! Todas as casas serão reveladas')

                #########FAZER PONTUAÇÃO #########FAZER PONTUAÇÃO #########FAZER PONTUAÇÃO
                elif roundWin == 5:
                    print('O jogador 2 acertou a soma em cheio! Todas as casas serão reveladas')
                elif roundWin == 6:
                    print('Os dois jogadores acertaram a soma! Verdadeiros mestres da matriz.')
                #########FAZER PONTUAÇÃO #########FAZER PONTUAÇÃO #########FAZER PONTUAÇÃO
                
                for i in fakematr:
                    print(i)

                print(f'''
    {gameStats['Jogador 1'][0][0]} | Possui {gameStats['Jogador 1'][0][1]} Casas Reveladas       
    {gameStats['Jogador 2'][0][0]} | Possui {gameStats['Jogador 2'][0][1]} Casas Reveladas       
                ''')

                for i in range(len(gameStats['Jogador 1'][1][0])):
                    quadPlay = gameStats['Jogador 1'][1][0][i]
                    numSumPlay = gameStats['Jogador 1'][1][1][i]
                    print(f'''
    {i + 1}º Rodada | {gameStats['Jogador 1'][0][0]}
    Escolheu a jogada {quadPlay} de soma {numSumPlay}''')
                for i in range(len(gameStats['Jogador 2'][1][0])):
                    quadPlay = gameStats['Jogador 2'][1][0][i]
                    numSumPlay = gameStats['Jogador 2'][1][1][i]
                    print(f'''
    {i + 1}º Rodada | {gameStats['Jogador 2'][0][0]}
    Escolheu a jogada {quadPlay} de soma {numSumPlay} 
    ''')

        if gameStats['Jogador 1'][0][1] > gameStats['Jogador 2'][0][1]:
            print(f'''
===========Fim do jogo=========== 

{gameStats['Jogador 1'][0][0]} saiu vitorioso!

===========Fim do jogo=========== 
''')
        elif gameStats['Jogador 1'][0][1] < gameStats['Jogador 2'][0][1]:
            print(f'''
===========Fim do jogo=========== 

{gameStats['Jogador 2'][0][0]} saiu vitorioso!

===========Fim do jogo=========== 
''')
        else:
            print(f'''
===========Fim do jogo=========== 

Houve um empate,

===========Fim do jogo=========== 
''')
print('fim')
print(gameConfigs)
print(gameStats)
print(board)
print(board2)


