# Construa um programa contendo um módulo capaz de calcular o consumo de
# combustível de um veículo. O módulo deve retornar o consumo calculado.

def calcular_consumo():
    litros = float(input("Digite a Quant. de litros consumidos: "))
    quilometros = float(input("Digite a Quantidade de km rodados: "))
    if litros > 0:
        consumo = quilometros/litros
    else:
        return -1
    return consumo

print("Consumo:", calcular_consumo(), "km/l")
