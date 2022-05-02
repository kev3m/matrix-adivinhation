import random

# boardNumbers = 1
# dificulty = ['M', 60]

# matrice = []
# board = []
# for i in range(1, dificulty[1] + 1):
#     matrice.append(i)
#     random.shuffle(matrice)

# if boardNumbers == 1 and dificulty == 'F':
#         board = [[matrice[0],matrice[1],matrice[2]],
#         [matrice[3],matrice[4],matrice[5]],
#         [matrice[6],matrice[7],matrice[8]]]
# if boardNumbers == 1 and dificulty[0] == 'M':
#         board = [[matrice[0],matrice[1],matrice[2]],
#         [matrice[3],matrice[4],matrice[5]],
#         [matrice[6],matrice[7],matrice[8]]]


# print(board)
def createMatrice(boardNumbers, dificulty):
    numList = []

    if dificulty == 3:
        interval = 30
    elif dificulty == 4:
        interval = 60
    elif dificulty == 5:
        interval = 100

    for i in range(1, interval + 1):
        numList.append(i)
    random.shuffle(numList)
    copyofNumList = numList.copy()
    
    matrice = []
    secondMatrice = []

    for i in range(dificulty):
            numbers = random.sample(numList, dificulty)
            for j in numbers:
                numList.pop(numList.index(j))
            matrice.append(numbers)

    if boardNumbers == 2:
        for i in range(dificulty):
            numbers = random.sample(copyofNumList, dificulty)
            for j in numbers:
                copyofNumList.pop(copyofNumList.index(j))
            secondMatrice.append(numbers)
    
    return matrice, secondMatrice
    
    
        
tab = int(input('a> '))
dif = int(input('b> '))
board1, board2 = createMatrice(tab,dif)
print(board1)
print(board2)

# def criarMatriz(boardNumbers, dificulty):
#     matrice = []
#     #Shuffle problem
#     oldMatriz = []
#     for i in range(1,dificulty+1):
#         matrice.append(i)
#         random.shuffle(matrice)
#     oldMatriz = matrice
#     if boardNumbers == 1:
#         board = [[matrice[0],matrice[1],matrice[2]],[matrice[3],matrice[4],matrice[5]],[matrice[6],matrice[7],matrice[8]]]
#         if dificulty == 60:
#             board[0].append(matrice[9]),board[1].append(matrice[10]), board[2].append(matrice[11]) 
#             board.append([matrice[12], matrice[13], matrice[14], matrice[15]])   
#         elif dificulty == 100:
#             board[0].append(matrice[9]),board[0].append(matrice[10]), board[1].append(matrice[11]), board[1].append(matrice[12]), board[2].append(matrice[13]),board[2].append(matrice[14])
#             board.append([matrice[15], matrice[16], matrice[17], matrice[18], matrice[19]]),board.append([matrice[20], matrice[21], matrice[22], matrice[23], matrice[24]]) 
#         return board
#     elif boardNumbers == 2:
#         board = [[matrice[0],matrice[1],matrice[2]],[matrice[3],matrice[4],matrice[5]],[matrice[6],matrice[7],matrice[8]]]
#         random.shuffle(matrice)
#         secondBoard = [[matrice[0],matrice[1],matrice[2]],[matrice[3],matrice[4],matrice[5]],[matrice[6],matrice[7],matrice[8]]]
#         #MÉTODO COPY
#         if dificulty == 60:
#             board[0].append(oldMatriz[9]),board[1].append(oldMatriz[10]), board[2].append(oldMatriz[11]) 
#             board.append([oldMatriz[12], oldMatriz[13], oldMatriz[14], oldMatriz[15]])  
#             secondBoard[0].append(matrice[9]),secondBoard[1].append(matrice[10]), secondBoard[2].append(matrice[11])
#             secondBoard.append([matrice[12], matrice[13], matrice[14], matrice[15]])   
#         elif dificulty == 100:
#             board[0].append(oldMatriz[9]),board[0].append(oldMatriz[10]), board[1].append(oldMatriz[11]), board[1].append(oldMatriz[12]), board[2].append(oldMatriz[13]),board[2].append(oldMatriz[14])    
#             board.append([oldMatriz[15], oldMatriz[16], oldMatriz[17], oldMatriz[18], oldMatriz[19]]), board.append([oldMatriz[20], oldMatriz[21], oldMatriz[22], oldMatriz[23], oldMatriz[24]])
#             secondBoard[0].append(matrice[9]), secondBoard[0].append(matrice[10]), secondBoard[1].append(matrice[11]), secondBoard[1].append(matrice[12]), secondBoard[2].append(matrice[13]), secondBoard[2].append(matrice[14])
#             secondBoard.append([matrice[15], matrice[16], matrice[17], matrice[18], matrice[19]]), secondBoard.append([matrice[20], matrice[21], matrice[22], matrice[23], matrice[24]])    
#         return board, secondBoard



# if tab == 1:
#         c1,c2,c3 = (board[0][0] + board[1][0] + board[2][0]), (board[1][0] + board[1][1] + board[2][1]), (board[2][0] + board[2][1] + board[2][2])
#         l1, l2, l3 = (sum(board[0])), (sum(board[1])), (sum(board[2]))
#         somasTab = {'Colunas': [c1,c2,c3], 'Linhas': [l1,l2,l3] }
#         if dif == 60:
#             c1 += board[3][0]
#             c2 += board[3][1]
#             c3 += board[3][2]
#             c4 = board[0][3] + board[1][3] + board[2][3] + board[3][3]
#             l4 = sum(board[3])
#             somasTab = {'Colunas': [c1,c2,c3,c4], 'Linhas': [l1,l2,l3,l4] }
#         elif dif == 100:
#             c1 += board[2][0]
#             c2 += board[3][1]
#             c3 += board[3][2]
#             c4 = board[0][3] + board[1][3] + board[2][3] + board[3][3] + board[4][3]
#             c5 = board[0][4] + board[1][4] + board[2][4] + board[3][5] + board[4][4]
#             l4 = sum(board[3])
#             l5 = sum(board[4])
#             somasTab = {'Colunas': [c1,c2,c3,c4,c5], 'Linhas': [l1,l2,l3,l4,l5] }

# print(somasTab)

