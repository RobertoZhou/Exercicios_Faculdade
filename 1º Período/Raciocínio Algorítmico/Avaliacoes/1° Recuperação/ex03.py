# Apresente no quadro a seguir o algoritmo capaz de ler
# NUM números inteiros pelo teclado e imprimir na tela
# se este é maior, menor ou igual a zero.

NUM = 10
for cont in range(NUM):
    numero = int(input("Digite um numero: "))
    if numero == 0:
        print("Igual a zero")
    elif numero > 0:
        print("Maior que zero")
    else:
        print("Menor que zero")
