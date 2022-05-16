import random

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