# Implemente um programa em Python que lê números inteiros pelo teclado de forma repetida.
# A repetição encerra-se quando o usuário digitar 0 (zero).
# Dica: este exercício não faz uso de contador.

numero = int(input("Digite um numero: "))
while numero != 0:
    numero = int(input("Digite um numero: "))
print("Valor digitado: ", numero)