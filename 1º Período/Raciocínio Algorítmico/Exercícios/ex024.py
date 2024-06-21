# Implemente um algoritmo que leia um inteiro e calcule o seu fatorial.
# Dica: o fatorial de 5 é 120, obtido como: 5! = 5 * 4 * 3 * 2 * 1

fatorial = int(input("Digite um número, para ver seu fatorial: "))
while fatorial < 0:
    print("[ERRO] Número Inválido!")
    print("Tente Novamente!")
    fatorial = int(input("Digite um número, para ver seu fatorial: "))

calculo = fatorial
for cont in range(fatorial-1, 0, -1):
    calculo = calculo * cont

print(fatorial, "! =", calculo)