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

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
mat2 = []
fakemat = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]


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

def tableReveal(roundwin, realtable, faketable, column, column2, p1P, p2P):#p1p e p2p são da função atribuirValores
    if roundwin == 1:

