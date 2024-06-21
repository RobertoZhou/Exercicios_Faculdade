# Escreva um algoritmo que dado o peso de um boxeador, informe a categoria a qual ele pertence, seguindo a tabela abaixo:
"""
    Categoria           Peso (Kg)
    Palha               Menor que 50 Kg
    Pluma               50 - 59,99
    Leve                60 - 75,99
    Pesado              76 - 87,99
    Super Pesado        Maior que 88 Kg
"""
peso = float(input("Digite o peso = "))
if peso < 50:
    print("Peso palha")
elif peso >= 50 and peso < 60:
    print("Peso pluma")
elif peso >= 60 and peso < 76:
    print("Peso Leve")
elif peso >= 76 and peso < 88:
    print("Peso pesado")
else:
    print("Peso super pesado")
