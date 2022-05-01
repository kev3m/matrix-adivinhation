import random

# boardNumbers = 1
# dificulty = ['M', 60]

# matriz = []
# board = []
# for i in range(1, dificulty[1] + 1):
#     matriz.append(i)
#     random.shuffle(matriz)

# if boardNumbers == 1 and dificulty == 'F':
#         board = [[matriz[0],matriz[1],matriz[2]],
#         [matriz[3],matriz[4],matriz[5]],
#         [matriz[6],matriz[7],matriz[8]]]
# if boardNumbers == 1 and dificulty[0] == 'M':
#         board = [[matriz[0],matriz[1],matriz[2]],
#         [matriz[3],matriz[4],matriz[5]],
#         [matriz[6],matriz[7],matriz[8]]]


# print(board)
lista = []
for i in range(1, 60+1):
    lista.append(i)
random.shuffle(lista)

nivel = 5
matriz = []
for i in range(nivel):
    teste = random.sample(lista, 5)
    print(teste)
    matriz.append(teste)
    # lista.remove(teste)
    
    
    

print(matriz)



# def criarMatriz(boardNumbers, dificulty):
#     matriz = []
#     #Shuffle problem
#     oldMatriz = []
#     for i in range(1,dificulty+1):
#         matriz.append(i)
#         random.shuffle(matriz)
#     oldMatriz = matriz
#     if boardNumbers == 1:
#         board = [[matriz[0],matriz[1],matriz[2]],[matriz[3],matriz[4],matriz[5]],[matriz[6],matriz[7],matriz[8]]]
#         if dificulty == 60:
#             board[0].append(matriz[9]),board[1].append(matriz[10]), board[2].append(matriz[11]) 
#             board.append([matriz[12], matriz[13], matriz[14], matriz[15]])   
#         elif dificulty == 100:
#             board[0].append(matriz[9]),board[0].append(matriz[10]), board[1].append(matriz[11]), board[1].append(matriz[12]), board[2].append(matriz[13]),board[2].append(matriz[14])
#             board.append([matriz[15], matriz[16], matriz[17], matriz[18], matriz[19]]),board.append([matriz[20], matriz[21], matriz[22], matriz[23], matriz[24]]) 
#         return board
#     elif boardNumbers == 2:
#         board = [[matriz[0],matriz[1],matriz[2]],[matriz[3],matriz[4],matriz[5]],[matriz[6],matriz[7],matriz[8]]]
#         random.shuffle(matriz)
#         secondBoard = [[matriz[0],matriz[1],matriz[2]],[matriz[3],matriz[4],matriz[5]],[matriz[6],matriz[7],matriz[8]]]
#         #MÉTODO COPY
#         if dificulty == 60:
#             board[0].append(oldMatriz[9]),board[1].append(oldMatriz[10]), board[2].append(oldMatriz[11]) 
#             board.append([oldMatriz[12], oldMatriz[13], oldMatriz[14], oldMatriz[15]])  
#             secondBoard[0].append(matriz[9]),secondBoard[1].append(matriz[10]), secondBoard[2].append(matriz[11])
#             secondBoard.append([matriz[12], matriz[13], matriz[14], matriz[15]])   
#         elif dificulty == 100:
#             board[0].append(oldMatriz[9]),board[0].append(oldMatriz[10]), board[1].append(oldMatriz[11]), board[1].append(oldMatriz[12]), board[2].append(oldMatriz[13]),board[2].append(oldMatriz[14])    
#             board.append([oldMatriz[15], oldMatriz[16], oldMatriz[17], oldMatriz[18], oldMatriz[19]]), board.append([oldMatriz[20], oldMatriz[21], oldMatriz[22], oldMatriz[23], oldMatriz[24]])
#             secondBoard[0].append(matriz[9]), secondBoard[0].append(matriz[10]), secondBoard[1].append(matriz[11]), secondBoard[1].append(matriz[12]), secondBoard[2].append(matriz[13]), secondBoard[2].append(matriz[14])
#             secondBoard.append([matriz[15], matriz[16], matriz[17], matriz[18], matriz[19]]), secondBoard.append([matriz[20], matriz[21], matriz[22], matriz[23], matriz[24]])    
#         return board, secondBoard

# tab = int(input('a> '))
# dif = int(input('b> '))
# board,secondBoard = criarMatriz(tab,dif)
# print(board)
# print(secondBoard)

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

