#Funções responsáveis por gerar as matrizes que serão utilizadas na partida.
from functions.matricesGenerator import createMatrice, createFakeMatrice, createColumnsMatrice
#Funções responsáveis por manipular os valores contidos nas matrizes utilizadas.
from functions.valuesManipulationInMatrices import sumMatrice, assignTableValues
#Funções responsáveis por retornar o(s) vencedor(es) do round, seus "chutes" e os números que serão exibidos na matriz
from functions.roundWinner import intervalVerifier, roundWinner, returnWinnerPlay, returnNumToSwap
#Funções responsáveis por exibir a matriz falsa utillizando os valores substituídos
from functions.matrixView import searchNumIndexInMainBoard, tableSwap

gameConfigs = {'Tabuleiros': 0, 'difficulty': 0, 'Encerrar': 0} #Dif = (F,M OU D)
gameStats = { 'Jogador 1': [['Nome', 0],[[], []]], 'Jogador 2': [['Nome', 0],[[], []]]}
#gameStats = { 'Jogador X/Y': [['Nome do jogador', Pontuação do jogador],[[Linha/Coluna selecionada], [Chute da soma]]]}

def receiveConfigs(boardNumbers,difficulty, closure, roundsNum) :
    if boardNumbers == 1:
        gameConfigs['Tabuleiros'] = 1
    elif boardNumbers == 2:
        gameConfigs['Tabuleiros'] = 2
    else:
        return 'O jogo só pode ser jogado com 1 ou 2 tabuleiros! Digite uma quantidade válida.'

    if difficulty == 'F':
        gameConfigs['difficulty'] = 3
    elif difficulty == 'M':
        gameConfigs['difficulty'] = 4
    elif difficulty == 'D':
        gameConfigs['difficulty'] = 5
    
    if closure == 1:
        gameConfigs['Encerrar'] = roundsNum
    elif closure == 2:
        gameConfigs['Encerrar'] = closure
    return boardNumbers, difficulty, closure, roundsNum


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
        difficulty = int(input('''Selecione a difficulty:
        
=== Selecione a difficulty ===

    [3] - Fácil (3x3)
    [4] - Médil (4x4)
    [5] - Difícil (5x5) 
    
================================    
'''))

        while difficulty != 3 and difficulty != 4 and difficulty != 5:
            print('Falha na matrix! difficulty inválida')
            difficulty = int(input('''Selecione a difficulty:
        
=== Selecione a difficulty ===

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
    plays = [['c1', 'c2', 'c3', 'c4', 'c5'], ['l1', 'l2', 'l3', 'l4', 'l5']] #Utlizada para servir de referência para a função que retorna o(s) número(s) a ser(em) exibido(s)
    
    contadorRodadas = 0
    receiveConfigs(quantTab, difficulty,finalizar, numRodadas)
    board, board2, lines = createMatrice(quantTab,difficulty)
    print(board)
  
    #PR evitar o bug das linhas
   
    column, column2 = createColumnsMatrice(board, board2)
    #Matriz
    
    sumtab = sumMatrice(quantTab, difficulty, board, board2)
    fakeMatrice = createFakeMatrice(difficulty)
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
                if difficulty == '3':
                    while p1Play != 'c1' and p1Play != 'c2' and p1Play != 'c3' and p1Play != 'l1' and p1Play != 'l2' and p1Play != 'l3':
                        p1Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a difficulty escolhida |Até c3 ou l3|: ''')
                elif difficulty == '4':
                    while p1Play != 'c1' and p1Play != 'c2' and p1Play != 'c3' and p1Play != 'c4' and p1Play != 'l1' and p1Play != 'l2' and p1Play != 'l3' and p1Play != 'l4': 
                        p1Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a difficulty escolhida |Até c4 ou l4|: ''')
                elif difficulty == '5':
                    while p1Play != 'c1' and p1Play != 'c2' and p1Play != 'c3' and p1Play != 'c4' and p1Play != 'c5' and p1Play != 'l1' and p1Play != 'l2' and p1Play != 'l3' and p1Play != 'l4' and p1Play != 'l5': 
                        p1Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a difficulty escolhida |Até c5 ou l5|: ''')
                
                p1PlaySum = int(input(f'''{gameStats['Jogador 1'][0][0]} | Digite o valor que deseja chutar: '''))
                
                p2Play = input(f'''{gameStats['Jogador 2'][0][0]} | Digite a linha ou coluna que deseja chutar o valor: ''')
                if difficulty == '3':
                    while p2Play != 'c1' and p2Play != 'c2' and p2Play != 'c3' and p2Play != 'l1' and p2Play != 'l2' and p2Play != 'l3':
                        p2Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a difficulty escolhida |Até c3 ou l3|: ''')
                elif difficulty == '4':
                    while p2Play != 'c1' and p2Play != 'c2' and p2Play != 'c3' and p2Play != 'c4' and p2Play != 'l1' and p2Play != 'l2' and p2Play != 'l3' and p2Play != 'l4': 
                        p2Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a difficulty escolhida |Até c4 ou l4|: ''')
                elif difficulty == '5':
                    while p2Play != 'c1' and p2Play != 'c2' and p2Play != 'c3' and p2Play != 'c4' and p2Play != 'c5' and p2Play != 'l1' and p2Play != 'l2' and p2Play != 'l3' and p2Play != 'l4' and p2Play != 'l5': 
                        p2Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a difficulty escolhida |Até c5 ou l5|: ''')
               
                p2PlaySum = int(input(f'''{gameStats['Jogador 2'][0][0]} | Digite o valor que deseja chutar: '''))

                p1pTabel, p2pTabel = assignTableValues(p1Play,p2Play,sumtab)
                interval1, interval2,biggerORsmaller, biggerORsmaller2= intervalVerifier(p1pTabel, p1PlaySum, p2pTabel, p2PlaySum)
                roundWin, bigger_or_smaller = roundWinner(interval1,interval2,biggerORsmaller,biggerORsmaller2)
                statusReceiver(p1Play, p1PlaySum, p2Play, p2PlaySum, gameStats)
                winnerplay, moreOrLess = returnWinnerPlay(p1Play, p2Play, roundWin, biggerORsmaller, biggerORsmaller2)
                numToSwap, matrizLimpa = returnNumToSwap(roundWin,winnerplay,biggerORsmaller, biggerORsmaller2,column, plays, lines)
                matind, numind = searchNumIndexInMainBoard(board,numToSwap)
                print(board)
                fakematr = tableSwap(numToSwap,fakeMatrice,matind,numind)
                fakeMatrice = fakematr
                
                print(f'''
 ===========Status da rodada===========    
                ''')
                if roundWin == 1:
                    print('O jogador 1 foi o vencedor da rodada')
                    gameStats['Jogador 1'][0][1] += 1
                    if moreOrLess == True:
                        print('O valor chutado é maior que a soma')    
                    else:
                        print('O valor chutado é menor que a soma') 

                elif roundWin == 2:
                    print('O jogador 2 foi o vencedor da rodada')
                    gameStats['Jogador 2'][0][1] += 1
                    if moreOrLess == True:
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

                p1pTabel, p2pTabel = assignTableValues(p1Play,p2Play,sumtab)
                interval1, interval2,biggerORsmaller, biggerORsmaller2= intervalVerifier(p1pTabel, p1PlaySum, p2pTabel, p2PlaySum)
                roundWin, bigger_or_smaller = roundWinner(interval1,interval2,biggerORsmaller,biggerORsmaller2)

                statusReceiver(p1Play, p1PlaySum, p2Play, p2PlaySum, gameStats)
                
                winnerplay, moreOrLess = returnWinnerPlay(p1Play, p2Play, roundWin, biggerORsmaller, biggerORsmaller2)
                numToSwap = returnNumToSwap(roundWin,winnerplay,biggerORsmaller, biggerORsmaller2,column, plays, lines)
                matind, numind = searchNumIndexInMainBoard(board,numToSwap)
                fakematr = tableSwap(numToSwap,fakeMatrice,matind,numind)
                fakeMatrice = fakematr
                
                
                print(f'''
        ===========Status da rodada===========    
                ''')
                if roundWin == 1:
                    print('O jogador 1 foi o vencedor da rodada')
                    gameStats['Jogador 1'][0][1] += 1
                    if moreOrLess == True:
                        print('O valor chutado é maior que a soma')    
                    else:
                        print('O valor chutado é menor que a soma') 

                elif roundWin == 2:
                    print('O jogador 2 foi o vencedor da rodada')
                    gameStats['Jogador 2'][0][1] += 1
                    if moreOrLess == True:
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


