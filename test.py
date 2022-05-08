def roundWinner(p1P, p2P,maiMen1, maiMen2):
    if p1P < p2P:
        return 1, maiMen1
    elif p1P > p2P:
        return 2, maiMen2
     #mesma aproximação   
    elif p1P == p2P :
        maiMen1 = maiMen2 = 'Mesma aproximação'
        return 3, maiMen1, maiMen2
    elif p1P == 0:
        maiMen1 = 'P1 | Acertou a soma'
        return 4, maiMen1
    elif p2P == 0:
        maiMen2 = 'P2 | Acertou a soma'
        return 5, maiMen2
    elif p1P == 0 and p1P == 0:
        maiMen1 = maiMen2 = 'Ambos acertaram a soma'
        return 6, maiMen1, maiMen2
