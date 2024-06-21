# Implemente um programa em Python para verificar quantos números uma
# aposta acertou na Megasena. O programa deve ler do teclado os 6 números
# sorteados e comparar com 6 números apostados.
# OBS: utilizar comparação posição a posição dos vetores.

print("============================")
sorteio = [0] * 6
for cont in range(6):
    print(cont + 1, "º Número")
    numero = int(input("Digite o número do sorteio: "))
    sorteio[cont] = numero


print("============================")
aposta = [0] * 6
for cont in range(6):
    print(cont + 1, "º Número")
    numero = int(input("Digite o número apostado: "))
    aposta[cont] = numero

contIguais = 0
for contSorteio in range(len(sorteio)):
    for contAposta in range(len(aposta)):
        if sorteio[contSorteio] == aposta[contAposta]:
            contIguais += 1
print("Iguais:", contIguais)
