import random

# Cria as matrizes 
def createMatrice(boardNumbers, difficulty):
    #Lista de números que serão pegos aleatoriamente
    numList = []
    interval = 0

    #Verifica a dificuldade
    if difficulty == 3:
        interval = 30
    elif difficulty == 4:
        interval = 60
    elif difficulty == 5:
        interval = 100

    #Delimita os números que serão adicionados na lista de acordo com a dificuldade
    for i in range(1, interval + 1):
        numList.append(i)
    random.shuffle(numList)
    copyofNumList = numList.copy()
    
    matrice = []
    secondMatrice = []

    #Recolhe os números da lista de forma aleatória
    for i in range(difficulty):
            numbers = random.sample(numList, difficulty)
            for j in numbers:
                #Remove os números já escolhidos para evitar que se repitam na matriz
                numList.pop(numList.index(j))
            matrice.append(numbers)

    #Gerador para a segunda matriz(no caso do jogo ser composto por dois tabuleiros)
    if boardNumbers == 2:
        for i in range(difficulty):
            numbers = random.sample(copyofNumList, difficulty)
            for j in numbers:
                copyofNumList.pop(copyofNumList.index(j))
            secondMatrice.append(numbers)      
    return matrice, secondMatrice

# Cria uma matriz falsa composta por zeros para exibição
def createFakeMatrice(difficulty):
    fakeMatriz = []

    #Utiliza a mesma lógica que createMatrice, porém adiciona apenas zeros
    for i in range(difficulty):
        invVar = []
        for j in range(difficulty):
            invVar.append(0)
        fakeMatriz.append(invVar)
    return fakeMatriz       

# Cria matrizes compostas por colunas em formatos de linhas. 
# Utilizada para manipular os elementos quando o chute do jogador envovler uma casa 
def createColumnsMatrice(matrice1, matrice2):
    colunas = []
    colunas2 = []
    for i in range(len(matrice1)):
        col = []
        for j in matrice1:
            col.append(j[i])
        colunas.append(col)

    for i in range(len(matrice2)):
        col = []
        for j in matrice2:
            col.append(j[i])
        colunas2.append(col)
    return colunas, colunas2        