# Em um restaurante que vende comida por quilo, o gerente resolveu
# avaliar quanto as pessoas costumam comer. Para isso, o gerente te
# contratou para desenvolver um programa em Python para calcular o valor
# médio, em quilos, de um prato. Assim, seu programa deve permitir a entrada
# do peso de cada prato (serão N no total) e imprimir na tela o peso médio.
# O programa deve também imprimir quantos pratos tem peso maior que 800 gramas.

numero_pratos_maior_800 = 0
quantidade_pratos = int(input("Digite quantos pratos: "))
peso_total = 0
for cont_pratos in range(quantidade_pratos):
    peso_prato = float(input("Digite o pesso em gramas: "))
    if peso_prato > 800:
        numero_pratos_maior_800 = numero_pratos_maior_800 + 1
    peso_total = peso_total + peso_prato

peso_medio = (peso_total / 1000) / quantidade_pratos
print("Peso médio dos pratos:", peso_medio, "Kg")
print("Numero de pratos acima 800g:", numero_pratos_maior_800)
