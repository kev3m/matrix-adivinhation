# def roundWinner(p1P, p2P,maiMen1, maiMen2):
#     if p1P < p2P:
#         return 1, maiMen1
#     elif p1P > p2P:
#         return 2, maiMen2
#      #mesma aproximação   
#     elif p1P == p2P :
#         maiMen1 = maiMen2 = 'Mesma aproximação'
#         return 3, maiMen1, maiMen2
#     elif p1P == 0:
#         maiMen1 = 'P1 | Acertou a soma'
#         return 4, maiMen1
#     elif p2P == 0:
#         maiMen2 = 'P2 | Acertou a soma'
#         return 5, maiMen2
#     elif p1P == 0 and p1P == 0:
#         maiMen1 = maiMen2 = 'Ambos acertaram a soma'
#         return 6, maiMen1, maiMen2

# mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# mat2 = []
# fakemat = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

# def roundWinner(p1P, p2P,maiMen1, maiMen2):
#     if p1P < p2P:
#         return 1, maiMen1
#     elif p1P > p2P:
#         return 2, maiMen2
#      #mesma aproximação   
#     elif p1P == p2P:
#         maiMen1 = maiMen2 = 'Mesma aproximação'
#         return 3, maiMen1, maiMen2
#     elif p1P == 0:
#         maiMen1 = 'P1 Acertou a soma'
#         return 4, maiMen1
#     elif p2P == 0:
#         maiMen2 = 'P2 Acertou a soma'
#         return 5, maiMen2
#     elif p1P == 0 and p1P == 0:
#         maiMen1 = maiMen2 = 'Ambos acertaram a soma'
#         return 6, maiMen1, maiMen2


def createColumns(mat1, mat2):
    colunas = []
    colunas2 = []
    for i in range(len(mat1)):
        col = []
        for j in mat:
            col.append(j[i])
        colunas.append(col)
    for i in range(len(mat2)):
        col = []
        for j in mat2:
            col.append(j[i])
        colunas2.append(col)

    return colunas, colunas2

mat = [[1,2,3], [4,5,6], [7,8,9]]
mat2 = []
plays = [['c1', 'c2', 'c3', 'c4', 'c5'], ['l1', 'l2', 'l3', 'l4', 'l5']]

coluna1, colunas2 = createColumns(mat, mat2)
fakemat = [[0,0,0], [0,0,0], [0,0,0]]
print(coluna1, colunas2)
for i in coluna1:
    print(i)

play = 'l1'
test = True


def returnNum(winnerPlay,maiorOumenor,coluna,playsTab, matriz):
    if winnerPlay[0] == 'c':
        indexcolumn = playsTab[0].index(winnerPlay)
        if maiorOumenor == True:
            swapNum = max(coluna[indexcolumn])
        elif maiorOumenor == False:
            swapNum = min(coluna[indexcolumn])

    if winnerPlay[0] == 'l':
        indexcolumn = playsTab[1].index(winnerPlay)
        if maiorOumenor == True:
            swapNum = max(matriz[indexcolumn])
        elif maiorOumenor == False:
            swapNum = min(matriz[indexcolumn])
    return swapNum

def searchindex(matriz,num):
    for i in matriz:
        if num in i:
            return matriz.index(i), i.index(num)

def tableSwap(numero,fakemat,matrizInd, numInd):
    fakemat[matrizInd][numInd] = numero
    return fakemat

nume = returnNum(play,test,coluna1, plays, mat)
matind, numind = searchindex(mat,nume)
fakematr = tableSwap(nume,fakemat,matind,numind)

for i in fakematr:
    print(i)
