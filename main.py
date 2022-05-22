'''Autor: Keven Coutinho Crisostomo
Componente Curricular: Algoritmos I
Concluido em: 22/05/2022
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
'''
import os
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
    

def clearTerminal():
    if os.name == 'nt':
        return os.system('cls')
    elif os.name == 'posix':
        return os.system('clear')
        
#Recebe o histórico da rodada
def statusReceiver(p1P,p1Sum, p2P, p2Sum,statsTab):
    statsTab['Jogador 1'][1][0].append(p1P)
    statsTab['Jogador 1'][1][1].append(p1Sum)
    statsTab['Jogador 2'][1][0].append(p2P)
    statsTab['Jogador 2'][1][1].append(p2Sum)

#Iniciando o game
menu = 0
while menu != 3:
    menu = int(input('''
============ Selecione uma opção ===============    
+                                            +   
+    [1] - Iniciar                           +
+    [2] - Instruções                        +
+    [3] - Sair                              +    
+                                            +        
================================================      
➪ '''))
    while menu == 2:
        print('Aqui jás instruções')
        menu = int(input('''
============ Selecione uma opção ===============    
+                                            +   
+    [1] - Iniciar                           +
+    [2] - Instruções                        +
+    [3] - Sair                              +    
+                                            +        
================================================         
➪ '''))
    clearTerminal()
        
    #Configurando o game
    if menu == 1:
        quantTab = int(input('''
==================== Configurando o jogo =======================         
+        === Selecione a quantidade de tabuleiros ===          +  
+                                                              +  
+    [1] - Tabuleiro único                                     +   
+    [2] - 2 Tabuleiros (1 Tabuleiro para cada jogador)        +    
+                                                              +  
================================================================  
➪ '''))
        clearTerminal()
        while quantTab != 1 and quantTab != 2:
            print('''
================================================
+                                              +  
+    ________________                          + 
+   |                |                         +
+   |    Falha na    |                         +  
+   |     Matrix     |                         + 
+   |________________|                         + 
+    ∧＿∧  ||   Entrada inválida!              +
+   (⌐■_■) ||   Não tente quebrar o código.    + 
+   /     づ                                   +
================================================  
            ''')
            quantTab = int(input('''
==================== Configurando o jogo =======================         
+        === Selecione a quantidade de tabuleiros ===          + 
+                                                              +  
+    [1] - Tabuleiro único                                     +    
+    [2] - 2 Tabuleiros (1 Tabuleiro para cada jogador)        +  
+                                                              +  
================================================================    
➪ '''))
        clearTerminal()
        if quantTab == 2:
            quantTab -= 1
            print('''
================================================
+                                              +  
+    ________________                          + 
+   |                |                         +
+   |    Falha na    |                         +  
+   |     Matrix     |                         + 
+   |________________|                         + 
+    ∧＿∧  ||   Pedimos perdão!                +
+   (⌐■_■) ||   Apenas um tabuleiro está       + 
+   /     づ    disponível no momento          +
================================================  
            ''')
            

        difficulty = int(input('''
========= Selecione a dificuldade ===========
+                                           + 
+    [3] - Fácil (3x3)                      + 
+    [4] - Médil (4x4)                      +    
+    [5] - Difícil (5x5)                    + 
+                                           + 
=============================================     
➪ '''))
        clearTerminal()
        while difficulty != 3 and difficulty != 4 and difficulty != 5:
            print('''
================================================
+                                              +  
+    ________________                          + 
+   |                |                         +
+   |    Falha na    |                         +  
+   |     Matrix     |                         + 
+   |________________|                         + 
+    ∧＿∧  ||   Dificuldade inválida!          +
+   (⌐■_■) ||   Digite de acordo com as opções + 
+   /     づ    fornecidas                     +
================================================  
            ''')
            difficulty = int(input('''
========= Selecione a dificuldade ===========
+                                           + 
+    [3] - Fácil (3x3)                      + 
+    [4] - Médil (4x4)                      +    
+    [5] - Difícil (5x5)                    + 
+                                           + 
=============================================  
➪ '''))

        finalizar = int(input('''
============= Selecione o modo de encerramento ===========     
+                    da partida                          +
+                                                        +
+    [1] - Por número de rodadas                         + 
+    [2] - Ao revelar completamente um dos tabuleiros    +
+                                                        +
==========================================================
➪ '''))
        clearTerminal()
        while finalizar != 1 and finalizar != 2:
            print('''
================================================
+                                              +  
+    ________________                          + 
+   |                |                         +
+   |    Falha na    |                         +  
+   |     Matrix     |                         + 
+   |________________|                         + 
+    ∧＿∧  ||   Encerramento inválido!         +
+   (⌐■_■) ||   Digite de acordo com as opções + 
+   /     づ    fornecidas                     +
================================================  
            ''')
            finalizar = int(input('''
============= Selecione o modo de encerramento ===========     
+                    da partida                          +
+                                                        +
+    [1] - Por número de rodadas                         + 
+    [2] - Ao revelar completamente um dos tabuleiros    +
+                                                        +
==========================================================
➪ '''))

        if finalizar == 1:
            numRodadas = int(input('''
=============================================
+         Digite o número de rodadas        +
=============================================         
➪ '''))       
            while numRodadas % 2 == 0 or numRodadas < 0:
                print('''
================================================
+                                              +  
+    ________________                          + 
+   |                |                         +
+   |    Falha na    |                         +  
+   |     Matrix     |                         + 
+   |________________|                         + 
+    ∧＿∧  ||   O número de rodadas deve ser   +
+   (⌐■_■) ||   impar e maior que zero.        + 
+   /     づ    Pare de quebrar o código!      +
================================================  
            ''')
                numRodadas = int(input('''
=============================================
+         Digite o número de rodadas        +
=============================================   
➪ '''))    
        elif finalizar == 2:
            numRodadas = ''
    #Retornando as configurações para o dicionário
    clearTerminal()
    #Utlizada para servir de referência para a função que retorna o(s) número(s) a ser(em) exibido(s)
    plays = [['c1', 'c2', 'c3', 'c4', 'c5'], ['l1', 'l2', 'l3', 'l4', 'l5']] 
    contadorRodadas = 0
    receiveConfigs(quantTab, difficulty,finalizar, numRodadas)
    
    board, board2 = createMatrice(quantTab,difficulty)
    #Cópia da matriz para remover os números
    lines = list(map(list, board))
    #Cópia da matriz invertida(colunas viram linhas) para remover os números
    column, column2 = createColumnsMatrice(board, board2)
    sumtab = sumMatrice(quantTab, difficulty, board, board2)
    fakeMatrice = createFakeMatrice(difficulty)
    jogador1Nick = input('''
=============================================
+      Digite o nickname do jogador 1       +
=============================================    
➪ ''')
    gameStats['Jogador 1'][0][0] = jogador1Nick
    jogador2Nick = input('''
=============================================
+      Digite o nickname do jogador 2       +
=============================================  
➪ ''')
    gameStats['Jogador 2'][0][0] = jogador2Nick
    menu = 3
    clearTerminal()
    #Iniciando o jogo com um tabuleiro
    if gameConfigs['Tabuleiros'] == 1:
        print(f'''
================= O jogo foi iniciado com um tabuleiro para dois jogadores =============
+                                                                                      +  
                                Boa sorte {gameStats['Jogador 1'][0][0]} e {gameStats['Jogador 2'][0][0]}                
+                                                                                      +   
========================================================================================    
    ''')
        
        print(f'''
======================= Tabela guia para escolha das opções ==========================
+                                                                                    +
+        Fácil                   Médio                       Díficil                 +
+    -------------         -----------------         ---------------------           +    
+    | x | x | x | > l1    | x | x | x | x | > l1    | x | x | x | x | x | > l1      +    
+    | x | x | x | > l2    | x | x | x | x | > l2    | x | x | x | x | x | > l2      +    
+    | x | x | x | > l3    | x | x | x | x | > l3    | x | x | x | x | x | > l3      +    
+    -------------         | x | x | x | x | > l4    | x | x | x | x | x | > l4      +   
+     ^   ^   ^            -----------------         | x | x | x | x | x | > l5      +
+     c1  c2  c3             ^   ^   ^   ^           ---------------------           +
+                           c1  c2  c3  c4             ^   ^   ^   ^   ^             +
+                                                      c1  c2  c3  c4  c5            +
+                                                                                    +
======================================================================================
''')    
        print('Matriz oculta para correção do código')
        for i in board:
            for j in i:
                print(f'| {j} |', end='')
            print('\n')

        if finalizar == 1:
            while contadorRodadas < gameConfigs['Encerrar']:
                print(f'''
========================== Round {contadorRodadas + 1} ========================
                ''')
                p1Play = input(f'''{gameStats['Jogador 1'][0][0]} | Digite a linha ou coluna que deseja chutar o valor: ''')
                
                if difficulty == 3:
                    while p1Play != 'c1' and p1Play != 'c2' and p1Play != 'c3' and p1Play != 'l1' and p1Play != 'l2' and p1Play != 'l3':
                        p1Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a dificuldade escolhida |Até c3 ou l3|: ''')
                elif difficulty == 4:
                    while p1Play != 'c1' and p1Play != 'c2' and p1Play != 'c3' and p1Play != 'c4' and p1Play != 'l1' and p1Play != 'l2' and p1Play != 'l3' and p1Play != 'l4': 
                        p1Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a dificuldade escolhida |Até c4 ou l4|: ''')
                elif difficulty == 5:
                    while p1Play != 'c1' and p1Play != 'c2' and p1Play != 'c3' and p1Play != 'c4' and p1Play != 'c5' and p1Play != 'l1' and p1Play != 'l2' and p1Play != 'l3' and p1Play != 'l4' and p1Play != 'l5': 
                        p1Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a dificuldade escolhida |Até c5 ou l5|: ''')
                
                p1PlaySum = int(input(f'''{gameStats['Jogador 1'][0][0]} | Digite o valor que deseja chutar: '''))
                
                p2Play = input(f'''{gameStats['Jogador 2'][0][0]} | Digite a linha ou coluna que deseja chutar o valor: ''')
                if difficulty == 3:
                    while p2Play != 'c1' and p2Play != 'c2' and p2Play != 'c3' and p2Play != 'l1' and p2Play != 'l2' and p2Play != 'l3':
                        p2Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a dificuldade escolhida |Até c3 ou l3|: ''')
                elif difficulty == 4:
                    while p2Play != 'c1' and p2Play != 'c2' and p2Play != 'c3' and p2Play != 'c4' and p2Play != 'l1' and p2Play != 'l2' and p2Play != 'l3' and p2Play != 'l4': 
                        p2Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a dificuldade escolhida |Até c4 ou l4|: ''')
                elif difficulty == 5:
                    while p2Play != 'c1' and p2Play != 'c2' and p2Play != 'c3' and p2Play != 'c4' and p2Play != 'c5' and p2Play != 'l1' and p2Play != 'l2' and p2Play != 'l3' and p2Play != 'l4' and p2Play != 'l5': 
                        p2Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a dificuldade escolhida |Até c5 ou l5|: ''')
               
                p2PlaySum = int(input(f'''{gameStats['Jogador 2'][0][0]} | Digite o valor que deseja chutar: '''))


                p1pTabel, p2pTabel = assignTableValues(p1Play,p2Play,sumtab)
                interval1, interval2,biggerORsmaller, biggerORsmaller2= intervalVerifier(p1pTabel, p1PlaySum, p2pTabel, p2PlaySum)
                roundWin, bigger_or_smaller = roundWinner(interval1,interval2,biggerORsmaller,biggerORsmaller2)
                statusReceiver(p1Play, p1PlaySum, p2Play, p2PlaySum, gameStats)
                winnerplay, moreOrLess = returnWinnerPlay(p1Play, p2Play, roundWin, biggerORsmaller, biggerORsmaller2)
                numToSwap, swapListPoint = returnNumToSwap(roundWin,winnerplay,biggerORsmaller, biggerORsmaller2,column, plays, lines)
                matind, numind = searchNumIndexInMainBoard(board,numToSwap)
                fakematr = tableSwap(numToSwap,fakeMatrice,matind,numind)
                fakeMatrice = fakematr
                
                print(f'''
 ====================== Status da rodada {contadorRodadas + 1} ===============================    
                ''')
                if roundWin == 1:
                    print(f'''
                    {gameStats['Jogador 1'][0][0]} foi o vencedor da rodada''')
                    gameStats['Jogador 1'][0][1] += 1
                    if moreOrLess == True:
                        print('O valor chutado é maior que a soma')    
                    else:
                        print('O valor chutado é menor que a soma') 

                elif roundWin == 2:
                    print(f'''{gameStats['Jogador 2'][0][0]} foi o vencedor da rodada''')
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
                    gameStats['Jogador 1'][0][1] += len(numToSwap)
                elif roundWin == 5:
                    print('O jogador 2 acertou a soma em cheio! Todas as casas da respectiva linha/coluna serão reveladas')
                    gameStats['Jogador 2'][0][1] += len(numToSwap)
                elif roundWin == 6:
                    print('Os dois jogadores acertaram a soma! Verdadeiros mestres da matriz.')
                    gameStats['Jogador 1'][0][1] += len(swapListPoint[0])
                    gameStats['Jogador 2'][0][1] += len(swapListPoint[1])
                print('')

                for i in fakematr:
                    for j in i:
                        print(f'| {j} |', end='')
                    print('\n')

                print(f'''
{gameStats['Jogador 1'][0][0]} | Possui {gameStats['Jogador 1'][0][1]} Casas Reveladas       
{gameStats['Jogador 2'][0][0]} | Possui {gameStats['Jogador 2'][0][1]} Casas Reveladas       
                ''')

                #Percorrer o histórico de jogadas
                for i in range(len(gameStats['Jogador 1'][1][0])):
                    quadPlay = gameStats['Jogador 1'][1][0][i]
                    numSumPlay = gameStats['Jogador 1'][1][1][i]
                    print(f'''
{i + 1}º Rodada | {gameStats['Jogador 1'][0][0]}
Escolheu a jogada {quadPlay} de soma {numSumPlay}''')
                #Percorrer o histórico de jogadas
                for i in range(len(gameStats['Jogador 2'][1][0])):
                    quadPlay = gameStats['Jogador 2'][1][0][i]
                    numSumPlay = gameStats['Jogador 2'][1][1][i]
                    print(f'''
{i + 1}º Rodada | {gameStats['Jogador 2'][0][0]}
Escolheu a jogada {quadPlay} de soma {numSumPlay} 

    ''')        #incremento contador
                contadorRodadas += 1
        elif finalizar == 2:   
            while fakeMatrice != board:
                print(f'''
========================== Round {contadorRodadas + 1} ========================
                ''')
                p1Play = input(f'''{gameStats['Jogador 1'][0][0]} | Digite a linha ou coluna que deseja chutar o valor: ''')
                if difficulty == 3:
                    while p1Play != 'c1' and p1Play != 'c2' and p1Play != 'c3' and p1Play != 'l1' and p1Play != 'l2' and p1Play != 'l3':
                        p1Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a dificuldade escolhida |Até c3 ou l3|: ''')
                elif difficulty == 4:
                    while p1Play != 'c1' and p1Play != 'c2' and p1Play != 'c3' and p1Play != 'c4' and p1Play != 'l1' and p1Play != 'l2' and p1Play != 'l3' and p1Play != 'l4': 
                        p1Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a dificuldade escolhida |Até c4 ou l4|: ''')
                elif difficulty == 5:
                    while p1Play != 'c1' and p1Play != 'c2' and p1Play != 'c3' and p1Play != 'c4' and p1Play != 'c5' and p1Play != 'l1' and p1Play != 'l2' and p1Play != 'l3' and p1Play != 'l4' and p1Play != 'l5': 
                        p1Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a dificuldade escolhida |Até c5 ou l5|: ''')
                
                p1PlaySum = int(input(f'''{gameStats['Jogador 1'][0][0]} | Digite o valor que deseja chutar: '''))
                
                p2Play = input(f'''{gameStats['Jogador 2'][0][0]} | Digite a linha ou coluna que deseja chutar o valor: ''')
                if difficulty == 3:
                    while p2Play != 'c1' and p2Play != 'c2' and p2Play != 'c3' and p2Play != 'l1' and p2Play != 'l2' and p2Play != 'l3':
                        p2Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a dificuldade escolhida |Até c3 ou l3|: ''')
                elif difficulty == 4:
                    while p2Play != 'c1' and p2Play != 'c2' and p2Play != 'c3' and p2Play != 'c4' and p2Play != 'l1' and p2Play != 'l2' and p2Play != 'l3' and p2Play != 'l4': 
                        p2Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a dificuldade escolhida |Até c4 ou l4|: ''')
                elif difficulty == 5:
                    while p2Play != 'c1' and p2Play != 'c2' and p2Play != 'c3' and p2Play != 'c4' and p2Play != 'c5' and p2Play != 'l1' and p2Play != 'l2' and p2Play != 'l3' and p2Play != 'l4' and p2Play != 'l5': 
                        p2Play = input(f'''Jogada inválida | Digite a linha ou coluna conforme a dificuldade escolhida |Até c5 ou l5|: ''')
               
                p2PlaySum = int(input(f'''{gameStats['Jogador 2'][0][0]} | Digite o valor que deseja chutar: '''))

                p1pTabel, p2pTabel = assignTableValues(p1Play,p2Play,sumtab)
                interval1, interval2,biggerORsmaller, biggerORsmaller2= intervalVerifier(p1pTabel, p1PlaySum, p2pTabel, p2PlaySum)
                roundWin, bigger_or_smaller = roundWinner(interval1,interval2,biggerORsmaller,biggerORsmaller2)
                statusReceiver(p1Play, p1PlaySum, p2Play, p2PlaySum, gameStats)
                winnerplay, moreOrLess = returnWinnerPlay(p1Play, p2Play, roundWin, biggerORsmaller, biggerORsmaller2)
                numToSwap, swapListPoint = returnNumToSwap(roundWin,winnerplay,biggerORsmaller, biggerORsmaller2,column, plays, lines)
                matind, numind = searchNumIndexInMainBoard(board,numToSwap)
                fakematr = tableSwap(numToSwap,fakeMatrice,matind,numind)
                fakeMatrice = fakematr
                
                print(f'''
 ======================== Status da rodada ===============================    
                ''')
                if roundWin == 1:
                    print(f'''
                    {gameStats['Jogador 1'][0][0]} foi o vencedor da rodada
                    ''')
                    gameStats['Jogador 1'][0][1] += 1
                    if moreOrLess == True:
                        print('O valor chutado é maior que a soma')    
                    else:
                        print('O valor chutado é menor que a soma') 

                elif roundWin == 2:
                    print(f'''{gameStats['Jogador 2'][0][0]} foi o vencedor da rodada''')
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
                    gameStats['Jogador 1'][0][1] += len(numToSwap)
                elif roundWin == 5:
                    print('O jogador 2 acertou a soma em cheio! Todas as casas da respectiva linha/coluna serão reveladas')
                    gameStats['Jogador 2'][0][1] += len(numToSwap)
                elif roundWin == 6:
                    print('Os dois jogadores acertaram a soma! Verdadeiros mestres da matriz.')
                    gameStats['Jogador 1'][0][1] += len(swapListPoint[0])
                    gameStats['Jogador 2'][0][1] += len(swapListPoint[1])
                
                for i in fakematr:
                    for j in i:
                        print(f'| {j} |', end='')
                    print('\n')

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
Escolheu a jogada {quadPlay} de soma {numSumPlay}''')
                contadorRodadas += 1
        
        
        if gameStats['Jogador 1'][0][1] > gameStats['Jogador 2'][0][1]:
            print(f'''
======================== Fim de jogo =============================== 
+                                                                  + 
        {gameStats['Jogador 1'][0][0]} saiu vitorioso!
        |{gameStats['Jogador 1'][0][1]}| Casas reveladas
+                                                                  +
======================== Fim de jogo ===============================
''')       
            menu = int(input('''
================================================
+                                              +  
+    ________________                          + 
+   |                |                         +
+   |    Revanche?   |     [1] - Aceito        +  
+   |                |     [3] - Vou arregar   + 
+   |________________|                         + 
+    ∧＿∧  ||                                  +
+   (⌐■_■) ||                                  +  
+   /     づ                                   +
================================================  
            '''))
        elif gameStats['Jogador 1'][0][1] < gameStats['Jogador 2'][0][1]:
            
            print(f'''
======================== Fim de jogo =============================== 
+                                                                  + 
        {gameStats['Jogador 2'][0][0]} saiu vitorioso!
        |{gameStats['Jogador 2'][0][1]}| Casas reveladas
+                                                                  +
======================== Fim de jogo ===============================
''')    
            menu = int(input('''
================================================
+                                              +  
+    ________________                          + 
+   |                |                         +
+   |    Revanche?   |     [1] - Aceito        +  
+   |                |     [3] - Vou arregar   + 
+   |________________|                         + 
+    ∧＿∧  ||                                  +
+   (⌐■_■) ||                                  +  
+   /     づ                                   +
================================================  
            '''))
        else:
            
            print(f'''
======================== Fim de jogo ===============================
+                                                                  + 
+        Houve um empate! O número de casas reveladas é o mesmo    +
+                                                                  + 
======================== Fim de jogo =============================== 
''')        
            menu = int(input('''
================================================
+                                              +  
+    ________________                          + 
+   |                |                         +
+   |    Revanche?   |     [1] - Aceito        +  
+   |                |     [3] - Vou arregar   + 
+   |________________|                         + 
+    ∧＿∧  ||                                  +
+   (⌐■_■) ||                                  +  
+   /     づ                                   +
================================================  
            '''))
            



