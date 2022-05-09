plays = [['c1', 'c2', 'c3', 'c4', 'c5'], ['l1', 'l2', 'l3', 'l4', 'l5']]
play = 'l3'


if play[0] == 'c':
    print(plays[0].index(play))
elif play[0] == 'l':
    print(plays[1].index(play))
