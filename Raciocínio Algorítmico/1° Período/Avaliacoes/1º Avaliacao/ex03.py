#   O tempo de voo entre São Paulo e Curitiba pode variar em função de diversos fatores, dentre eles o tipo do avião.
#   O gerente de uma empresa de táxi aéreo gostaria de saber o tempo médio de viagens feitas neste trecho.
#   Para tal, ele te contratou para escrever um programa em Python capaz de ler o tempo gasto no trecho para cada tipo de avião.
#   A empresa tem 3 tipos diferentes de aviões:
#   “pequenos”, “médios” e “grandes”.
#   O cálculo será feito para 10 viagens no total.
#   Ao final, imprimir na tela o tempo médio gasto para o trecho, por tipo.

#   OBS: A SOLUÇÃO DESSE EXERCÍCIO E O MESMO DO ex05.py

tempo_aviao_pequeno = 0
tempo_aviao_medio = 0
tempo_aviao_grande = 0

for cont in range(10):
    print("1 - Avião Pequeno")
    print("2 - Avião Médio")
    print("3 - Avião Grande")
    tipo_aviao = int(input("Digite o Tipo de Avião: "))
    while tipo_aviao <= 0 or tipo_aviao > 3:
        print("Opção Inválida. Digite Uma Opção Valida!!!")
        tipo_aviao = int(input("Digite o Tipo de Avião: "))

    tempo_gasto = int(input("Digite o Tempo Gasto/Minutos: "))
    while tempo_gasto <= 0:
        print("Opção Inválida. Digite um Tempo em Minutos Valida!!!")
        tempo_gasto = int(input("Digite o Tempo Gasto/Minutos: "))
    if(tipo_aviao == 1):
        media_aviao_pequeno = media_aviao_pequeno + tempo_gasto
    elif(tipo_aviao == 2):
        media_aviao_medio = media_aviao_medio + tempo_gasto
    else:
        media_aviao_grande = media_aviao_grande + tempo_gasto

    tempo_media_pequeno = tempo_aviao_pequeno / 10
    tempo_media_medio = tempo_aviao_medio / 10
    tempo_media_grande = tempo_aviao_grande / 10

print("Tempo Gasto dos Aviões:")
print("Avião Pequeno/Minutos:", tempo_media_pequeno)
print("Avião Média/Minutos:", tempo_media_medio)
print("Avião Grande/Minutos:", tempo_media_grande)
