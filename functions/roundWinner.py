#Recebe os valores das somas retornados por AssignTableValues, os compora com os chutes dos jogadores e retorna o intervalo entre os dois.
def intervalVerifier(p1P,p1Sum, p2P, p2Sum):
    # p1P = Num Original | P1Sum = Chute escolhido pelo user
    # bigger_or_smaller = False se o chute for menor que a soma. Do contrário recebe True
    if p1P > p1Sum:
        p1P = (p1P - p1Sum)
        bigger_or_smaller = False
    elif p1P < p1Sum:
        p1P = (p1Sum - p1P)
        bigger_or_smaller = True
    elif p1P == p1Sum:
        p1P = 0
        bigger_or_smaller = True
    if p2P > p2Sum: 
        p2P = (p2P - p2Sum)
        bigger_or_smaller2 = False
    elif p2P < p2Sum:
        p2P = (p2Sum - p2P)
        bigger_or_smaller2 = True
    elif p2P == p2Sum:
        p2P = 0
        bigger_or_smaller2 = True
    #Retorna  o intervalo
    return p1P, p2P, bigger_or_smaller, bigger_or_smaller2    

# Retorna os casos de vitória com base na diferença entre os intervalos
def roundWinner(p1P, p2P,biggerORsmaller, biggerORsmaller2):
    #BiggerORsmaller | Parâmetro que recebe se determinada chute é maior ou menor que a soma
    if p1P < p2P and p1P != 0:
        return 1, biggerORsmaller
    elif p1P > p2P and p2P != 0:
        return 2, biggerORsmaller2
    elif p1P == p2P and p1P != 0 and p2P != 0:
        biggerORsmaller = biggerORsmaller2 = 'Mesma aproximação'
        return 3, biggerORsmaller, biggerORsmaller2
    elif p1P == 0 and p2P != 0:
        biggerORsmaller = 'P1 Acertou a soma'
        return 4, biggerORsmaller
    elif p2P == 0 and p1P != 0:
        biggerORsmaller2 = 'P2 Acertou a soma'
        return 5, biggerORsmaller2
    elif p1P == 0 and p1P == 0:
        biggerORsmaller = biggerORsmaller2 = 'Ambos acertaram a soma'
        return 6, biggerORsmaller

#Recebe o caso de vitória e retorna a jogada vencedora
def returnWinnerPlay(p1P, p2P, roundWinner, biggerORsmaller, biggerORsmaller2):
        if roundWinner == 1 or roundWinner == 4:
            return p1P, biggerORsmaller
        elif roundWinner == 2 or roundWinner == 5:
            return p2P, biggerORsmaller2
        elif roundWinner == 3:
            p1P = [p1P, p2P]
            biggerORsmaller = [biggerORsmaller,biggerORsmaller2]
            return p1P, biggerORsmaller
        elif roundWinner == 6:
            p1P = [p1P, p2P]
            return p1P, biggerORsmaller


# Retorna o(s) número(s) a serem substituidos na matriz falsa
def returnNumToSwap(winnerPlay, winnerPlayCase,bigger_or_smaller, bigger_or_smaller2,coluna,playsTab, linha):
    linha = linha.copy()
    swaplistPont = []
    if winnerPlay == 1 or winnerPlay == 4:
        #Para casos de escolha da coluna
        if winnerPlayCase[0] == 'c':
            indexcolumn = playsTab[0].index(winnerPlayCase)
            if winnerPlay == 1:
                if bigger_or_smaller == True:
                    swapNum = max(coluna[indexcolumn])
                    coluna[indexcolumn].remove(swapNum)
                elif bigger_or_smaller == False:
                    swapNum = min(coluna[indexcolumn])
                    coluna[indexcolumn].remove(swapNum)
            elif winnerPlay == 4:
                #Não da pra usar pop pois remove a matriz, e neste caso removemos apenas os números dentro da matriz               
                swapNum = coluna[indexcolumn].copy()  
                coluna[indexcolumn].clear()
        #Para casos de escolha da lista                
        elif winnerPlayCase[0] == 'l':
            indexcolumn = playsTab[1].index(winnerPlayCase)
            if winnerPlay == 1:
                if bigger_or_smaller == True:
                    swapNum = max(linha[indexcolumn])
                    linha[indexcolumn].remove(swapNum)
                elif bigger_or_smaller == False:
                    swapNum = min(linha[indexcolumn])
                    linha[indexcolumn].remove(swapNum)
            elif winnerPlay == 4:
                swapNum = linha[indexcolumn].copy()  
                linha[indexcolumn].clear()    
        return swapNum, swaplistPont

    elif winnerPlay == 2 or winnerPlay == 5:
        if winnerPlayCase[0] == 'c':
            indexcolumn = playsTab[0].index(winnerPlayCase)
            if winnerPlay == 2:
                if bigger_or_smaller2 == True:
                    swapNum = max(coluna[indexcolumn])
                    coluna[indexcolumn].remove(swapNum)
                elif bigger_or_smaller2 == False:
                    swapNum = min(coluna[indexcolumn]) 
                    coluna[indexcolumn].remove(swapNum)
            elif winnerPlay == 5:
                swapNum = linha[indexcolumn].copy()  
                coluna[indexcolumn].clear() 

        elif winnerPlayCase[0] == 'l':
            indexcolumn = playsTab[1].index(winnerPlayCase)
            if winnerPlay == 2:
                if bigger_or_smaller2 == True:
                    swapNum = max(linha[indexcolumn])
                    linha[indexcolumn].remove(swapNum)
                elif bigger_or_smaller2 == False:
                    swapNum = min(linha[indexcolumn])
                    linha[indexcolumn].remove(swapNum)
            elif winnerPlay == 5:
                swapNum = linha[indexcolumn].copy()  
                linha[indexcolumn].clear() 
        return swapNum, swaplistPont
    
    elif winnerPlay == 6:
        swaplist = []
        for i in winnerPlayCase:
            if i[0] == 'c':
                indexcolumn = playsTab[0].index(i)
                    #Não da pra usar pop pois remove a matriz, e neste caso removemos apenas os números dentro da matriz               
                swapNum = coluna[indexcolumn].copy()  
                coluna[indexcolumn].clear()
                swaplist.append(swapNum)
                swaplistPont.append(swapNum)
                for i in swapNum:   
                    swaplist.append(i)
            #Para casos de escolha da lista                
            elif i[0] == 'l':
                indexcolumn = playsTab[1].index(i)
                swapNum = linha[indexcolumn].copy()  
                linha[indexcolumn].clear() 
                swaplistPont.append(swapNum)
                for i in swapNum:   
                    swaplist.append(i)
        return swaplist, swaplistPont
