# Leia do teclado o valor da temperatura corrente. Caso o valor seja, negativo, solicitar a leitura novamente.

temperatura = float(input("Digite a temperatura: "))
while temperatura < 0:
    print("Temperatura menor que zero.")
    temperatura = float(input("Digite a temperatura: "))
print("Temperatura:", temperatura)
