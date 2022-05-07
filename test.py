gameStats = { 'Jogador 1': [['Nome', 0],[[], []]], 'Jogador 2': [['Nome', 0],[[], []]]}


def statusReceiver(p1P,p1Sum, p2P, p2Sum,statsTab):
    statsTab['Jogador 1'][1][0].append(p1P)
    statsTab['Jogador 1'][1][1].append(p1Sum)
    statsTab['Jogador 2'][1][0].append(p2P)
    statsTab['Jogador 2'][1][1].append(p2Sum)

teste = 1
while teste != 0:
    p1Play = input(f'''{gameStats['Jogador 1'][0][0]} | Digite a linha ou coluna que deseja chutar o valor: ''')
    p1PlaySum = int(input(f'''{gameStats['Jogador 1'][0][0]} | Digite o valor que deseja chutar: '''))
    p2Play = input(f'''{gameStats['Jogador 2'][0][0]} | Digite a linha ou coluna que deseja chutar o valor: ''')
    p2PlaySum = int(input(f'''{gameStats['Jogador 2'][0][0]} | Digite o valor que deseja chutar: '''))
    teste = int(input('> '))
    statusReceiver(p1Play, p1PlaySum, p2Play, p2PlaySum, gameStats)
print(gameStats)

for i in range(len(gameStats['Jogador 1'][1][0])):
    quadPlay = gameStats['Jogador 1'][1][0][i]
    numSumPlay = gameStats['Jogador 1'][1][1][i]
    print(f'{i + 1}º Rodada | Jogador 1 escolheu a jogada {quadPlay} de soma {numSumPlay} ')

for i in range(len(gameStats['Jogador 2'][1][0])):
    quadPlay = gameStats['Jogador 2'][1][0][i]
    numSumPlay = gameStats['Jogador 2'][1][1][i]
    print(f'{i + 1}º Rodada | Jogador 2 escolheu a jogada {quadPlay} de soma {numSumPlay} ')
    