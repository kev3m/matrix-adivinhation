import random


# def receberConfiguracoes(quantTabuleiros,dificuldade, encerramento, rodadas) :
#     if quantTabuleiros == 1:
#         gameConfigs['Tabuleiros'] = 1
#     elif quantTabuleiros == 2:
#         gameConfigs['Tabuleiros'] = 2
#     else:
#         return 'O jogo só pode ser jogado com 1 ou 2 tabuleiros! Digite uma quantidade válida.'

#     if dificuldade == 'F':
#         gameConfigs['Dificuldade'] = 3
#     elif dificuldade == 'M':
#         gameConfigs['Dificuldade'] = 4
#     elif dificuldade == 'D':
#         gameConfigs['Dificuldade'] = 5
    
#     if encerramento == 1:
#         gameConfigs['Encerrar'].append(encerramento)
#         gameConfigs['Encerrar'].append(rodadas)
#     elif encerramento == 2:
#         gameConfigs['Encerrar'] = encerramento
#     return quantTabuleiros, dificuldade, encerramento, rodadas


def createMatrice(boardNumbers, difficulty):
    numList = []

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
    
def fakeMatrice(difficulty):
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
        maiorOumenor = 'Acertou a soma'

    if p2P > p2Sum: #p2p = num da casa chutada | p2sum = soma chutada
        p2P = (p2P - p2Sum)
        maiorOumenor2 = False
    elif p2P < p2Sum:
        p2P = (p2Sum - p2P)
        maiorOumenor2 = True
    elif p2P == p2Sum:
        p2P = 0
        maiorOumenor2 = 'Acertou a soma'
    #Retorna  o intervalo
    return p1P, p2P, maiorOumenor, maiorOumenor2

def roundWinner(p1P, p2P,maiMen1, maiMen2):
    if p1P < p2P:
        return 1, maiMen1
    elif p1P > p2P:
        return 2, maiMen2
     #mesma aproximação   
    elif p1P == p2P:
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
            
def returnNum(winnerPlay, winnerPlayCase,maiorOumenor, maiorOumenor2,coluna,playsTab, matriz):
    if winnerPlay == 1 or winnerPlay == 4:
        if winnerPlayCase[0] == 'c':
            indexcolumn = playsTab[0].index(winnerPlayCase)
            if maiorOumenor == True:
                swapNum = max(coluna[indexcolumn])
            elif maiorOumenor == False:
                swapNum = min(coluna[indexcolumn])

        if winnerPlayCase[0] == 'l':
            indexcolumn = playsTab[1].index(winnerPlayCase)
            if maiorOumenor == True:
                swapNum = max(matriz[indexcolumn])
            elif maiorOumenor == False:
                swapNum = min(matriz[indexcolumn])
        return swapNum
    elif winnerPlay == 2 or winnerPlay == 5:
        if winnerPlayCase[0] == 'c':
            indexcolumn = playsTab[0].index(winnerPlayCase)
            if maiorOumenor2 == True:
                swapNum = max(coluna[indexcolumn])
            elif maiorOumenor2 == False:
                swapNum = min(coluna[indexcolumn])

        if winnerPlayCase[0] == 'l':
            indexcolumn = playsTab[1].index(winnerPlayCase)
            if maiorOumenor2 == True:
                swapNum = max(matriz[indexcolumn])
            elif maiorOumenor2 == False:
                swapNum = min(matriz[indexcolumn])
        return swapNum

def searchindex(matriz,num):
    for i in matriz:
        if num in i:
            return matriz.index(i), i.index(num)

def tableSwap(numero,fakemat,matrizInd, numInd):
    fakemat[matrizInd][numInd] = numero
    return fakemat

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

tab = int(input('a> '))
dif = int(input('b> '))

plays = [['c1', 'c2', 'c3', 'c4', 'c5'], ['l1', 'l2', 'l3', 'l4', 'l5']]

p1Play = input('''p1| Digite a linha ou coluna que deseja chutar o valor: ''')
p1PlaySum = int(input('''p1| Digite o valor que deseja chutar: '''))
p2Play = input(f'''p2| Digite a linha ou coluna que deseja chutar o valor: ''')
p2PlaySum = int(input(f'''p2| Digite o valor que deseja chutar: '''))
fakeMatriz = fakeMatrice(dif)
board, board2 = createMatrice(tab,dif)
column, column2 = createColumns(board, board2)
sumtab = somarMatriz(tab,dif)
#mudar parametros
p1pTabel, p2pTabel = atribuirValoresTabela(p1Play,p2Play,sumtab)
interval1, interval2,maiMen1, maiMen2= intervalVerifier(p1pTabel, p1PlaySum, p2pTabel, p2PlaySum)
roundWinner, maiorOumenor = roundWinner(interval1,interval2,maiMen1,maiMen2)
winnerplay, maiorOuMen = returnWinnePlay(p1Play, p2Play, roundWinner, maiMen1, maiMen2)
nume = returnNum(roundWinner,winnerplay,maiMen1, maiMen2,column, plays, board)
matind, numind = searchindex(board,nume)
fakematr = tableSwap(nume,fakeMatriz,matind,numind)

print(board)
print(board2)
print(column)
print(column2)
print(interval1)
print(interval2)

if roundWinner == 1:
    print('O jogador 1 foi o vencedor da rodada')
    
    if maiorOumenor == True:
        print('O valor chutado é maior que a soma')    
    else:
        print('O valor chutado é menor que a soma') 

elif maiorOumenor == 2:
    print('O jogador 2 foi o vencedor da rodada')
    
    if maiorOumenor == True:
        print('O valor chutado é maior que a soma')    
    else:
        print('O valor chutado é menor que a soma') 

elif maiorOumenor == 3:
    print('Os dois jogadores possuem a mesma aproximação, ambos ganharam!')
    

elif maiorOumenor == 4:
    print('O jogador 1 acertou a soma em cheio! Todas as casas serão reveladas')

        #########FAZER PONTUAÇÃO #########FAZER PONTUAÇÃO #########FAZER PONTUAÇÃO
elif maiorOumenor == 5:
    print('O jogador 2 acertou a soma em cheio! Todas as casas serão reveladas')
elif maiorOumenor == 6:
    print('Os dois jogadores acertaram a soma! Verdadeiros mestres da matriz.')
        #########FAZER PONTUAÇÃO #########FAZER PONTUAÇÃO #########FAZER PONTUAÇÃO
        
#Se o numero vencedor for maior = True, se for menor recebe False
print(roundWinner)
for i in fakematr:
    print(i)
