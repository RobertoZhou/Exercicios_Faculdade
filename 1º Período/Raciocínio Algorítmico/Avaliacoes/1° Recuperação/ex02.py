# Marli foi ao shopping comprar um vestido para a
# formatura de sua filha. Ela decidiu pagar o vestido da
# seguinte forma: 50% de entrada e o restante dividido
# em 4 parcelas. Sabendo-se o valor do vestido (lido
# pelo teclado), implemente um programa em Python
# para imprimir o valor da entrada e o valor de cada
# parcela.

valor_vestido = float(input("Valor vestido: "))
valor_entrada = valor_vestido/2
print("Valor da entrada", valor_entrada)
valor_parcela = (valor_vestido/2)/4
print("Valor parcela", valor_parcela)
