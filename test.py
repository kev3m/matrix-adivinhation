import random
    
    def criarMatriz(boardNumbers, dificulty):
    if boardNumbers == 1 and dificulty == 'F':
        #Lista de Números disponiveis para serem usados na matriz
        matriz = []
        for i in range(1,30+1):
            matriz.append(i)
        random.shuffle(matriz)
        #Criando a board adicionando os números da matriz em ordem
        board = [[matriz[0],matriz[1],matriz[2]],
        [matriz[3],matriz[4],matriz[5]],
        [matriz[6],matriz[7],matriz[8]]]
    elif boardNumbers == 1 and dificulty == 'M':
        matriz = []
        for i in range(1,60+1):
            matriz.append(i)
        random.shuffle(matriz)
        board = [[matriz[0],matriz[1],matriz[2], matriz[3]],
        [matriz[4],matriz[5],matriz[6], matriz[7]],
        [matriz[8],matriz[9],matriz[10], matriz[11]],]
    elif boardNumbers == 1 and dificulty == 'D':
        matriz = []
        for i in range(1,100+1):
            matriz.append(i)
        random.shuffle(matriz)
        board = [[matriz[0],matriz[1],matriz[2], matriz[3], matriz[4]],
        [matriz[5],matriz[6],matriz[7], matriz[8], matriz[9]],
        [matriz[10],matriz[11],matriz[12], matriz[13], matriz[14]],]

    #Configurações com dois tabuleiros
    if boardNumbers == 2 and dificulty == 'F':
        #Lista de Números disponiveis para serem usados na matriz
        matriz = []
        matriz2 = []
        for i in range(1,30+1):
            matriz.append(i)
        random.shuffle(matriz)
        #Criando a board adicionando os números da matriz em ordem
        board = [[matriz[0],matriz[1],matriz[2]],
        [matriz[3],matriz[4],matriz[5]],
        [matriz[6],matriz[7],matriz[8]]]
        random.shuffle(matriz)
        board2 = [[matriz[0],matriz[1],matriz[2]],
        [matriz[3],matriz[4],matriz[5]],
        [matriz[6],matriz[7],matriz[8]]]
    elif boardNumbers == 2 and dificulty == 'M':
        matriz = []
        for i in range(1,60+1):
            matriz.append(i)
        random.shuffle(matriz)
        board = [[matriz[0],matriz[1],matriz[2], matriz[3]],
        [matriz[4],matriz[5],matriz[6], matriz[7]],
        [matriz[8],matriz[9],matriz[10], matriz[11]],]
        random.shuffle(matriz)
        board2 = [[matriz[0],matriz[1],matriz[2], matriz[3]],
        [matriz[4],matriz[5],matriz[6], matriz[7]],
        [matriz[8],matriz[9],matriz[10], matriz[11]],]
    elif boardNumbers == 2 and dificulty == 'D':
        matriz = []
        for i in range(1,100+1):
            matriz.append(i)
        random.shuffle(matriz)
        board = [[matriz[0],matriz[1],matriz[2], matriz[3], matriz[4]],
        [matriz[5],matriz[6],matriz[7], matriz[8], matriz[9]],
        [matriz[10],matriz[11],matriz[12], matriz[13], matriz[14]],]
        random.shuffle(matriz)
        board2 = [[matriz[0],matriz[1],matriz[2], matriz[3], matriz[4]],
        [matriz[5],matriz[6],matriz[7], matriz[8], matriz[9]],
        [matriz[10],matriz[11],matriz[12], matriz[13], matriz[14]],]