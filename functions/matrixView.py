def searchNumIndexInMainBoard(defaultboard,num):
    #Verificar se num é uma lista ou não
    if isinstance(num,list) == False:
        for i in defaultboard:
            if num in i:
                return defaultboard.index(i), i.index(num)
    elif isinstance(num,list) == True:
        whichList = []
        whichListPos = []
        for j in num:
            for i in defaultboard:
                if j in i:
                    whichList.append(defaultboard.index(i))
                    whichListPos.append(i.index(j))
        return whichList, whichListPos

def tableSwap(numero,fakemat,matrizInd, numInd):
    if isinstance(numero,list) == False:
        fakemat[matrizInd][numInd] = numero
        return fakemat
    elif isinstance(numero,list) == True:
        #Indica que é uma linha
        if isinstance(matrizInd,list) == False:
            for i in range(len(numero)):
                matrizIndice = matrizInd
                numIndice = numInd[i]
                fakemat[matrizIndice][numIndice] = numero[i]
        #Indica que é uma coluna        
        else:
            for i in range(len(numero)):
                matrizIndice = matrizInd[i]
                numIndice = numInd[i]
                fakemat[matrizIndice][numIndice] = numero[i]
        return fakemat