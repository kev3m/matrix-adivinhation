def sumMatrice(boardNumbers, difficulty, board, board2):
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
    elif difficulty == 5:
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

def assignTableValues(p1P, p2P,sumtab):
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

