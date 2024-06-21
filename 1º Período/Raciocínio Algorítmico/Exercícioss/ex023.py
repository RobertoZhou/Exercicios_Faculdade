# Implemente um programa em Pyhton para ler 10 inteiros do teclado.
# Imprima cada número lido na tela, desde que o mesmo seja positivo.
# Dica: você vai precisar utilizar o for e o if neste exercício.

for contador in range(0, 10, 1):
    numero = int(input("Digite um numero: "))
    if numero >= 0:
        print("Numero:", numero)
    else:
        print("Nao positivo")