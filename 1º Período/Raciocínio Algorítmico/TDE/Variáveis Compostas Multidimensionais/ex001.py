#   Implemente um algoritmo em Python para permitir a aposta de 5 jogadores em um bolão da Copa do Mundo.
#   Cada jogador indicará o resultado dos 3 primeiros jogos do Brasil, no seguinte formato:
#   Jogo 1: 2 x 0
#   Jogo 2: 5 x 1
#   Jogo 3: 3 x 0

jogo1 = []
jogo2 = []
jogo3 = []
jogadores = 5
for jogador in range(jogadores):
    print("=================")
    print("  Jogador", jogador + 1)
    print
    for jogo in range(3):
        print("=================")
        print("Jogo", jogo+1)
        print("=================")
        time1 = int(input("1º Time: "))
        time2 = int(input("2º Time: "))
        placar = [time1, time2]
        if(jogo == 0):
            jogo1.append(placar)
        elif(jogo == 1):
            jogo2.append(placar)
        elif(jogo == 2):
            jogo3.append(placar)
jogos = [jogo1, jogo2, jogo3]
for jogador in range(jogadores):
    print("===================")
    print("     Jogador", jogador + 1)
    print("===================")
    for jogo in range(len(jogos)):
        print("Jogo", jogo+1,":", jogos[jogo][jogador][0], "X", jogos[jogo][jogador][1])
