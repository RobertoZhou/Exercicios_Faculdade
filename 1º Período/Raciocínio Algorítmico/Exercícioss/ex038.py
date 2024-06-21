# Implemente um algoritmo em Python para permitir a aposta
# de 5 jogadores em um bolão da Copa do Mundo. Cada
# jogador indicará o resultado dos 3 primeiros jogos do Brasil,
# no seguinte formato:
#   Jogo 1: 2 x 0
#   Jogo 2: 5 x 1
#   Jogo 3: 3 x 0

time1 = []
time2 = []

for jogador in range(5):
    print("===================")
    print("     Jogador", jogador+1)
    placar1 = []
    placar2 = []
    for jogo in range(3):
        print("======Jogo", jogo+1, "======")
        aposta1 = int(input("Digite o placar do primeiro time: "))
        aposta2 = int(input("Digite o placar do segundo time: "))
        placar1.append(aposta1)
        placar2.append(aposta2)
    time1.append(placar1)
    time2.append(placar2)

for jogador in range(5):
    print("===================")
    print("     Jogador", jogador+1)
    print("===================")
    for jogo in range(3):
        print("Jogo", jogador+1, ":", time1[jogador][jogo], "x", time2[jogador][jogo])