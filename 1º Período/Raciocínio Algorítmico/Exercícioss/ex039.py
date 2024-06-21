# Implementar um programa contendo um procedimento em
# Python para calcular o valor que deve ser pago por uma
# pessoa que deixa seu carro estacionado por X horas em um
# estacionamento que cobra Y reais por hora. O procedimento
# deve receber os valores X e Y via argumentos.

def calcular_total(valor_hora, horas_cheias):
    total_pagar = valor_hora * horas_cheias
    print(total_pagar)
    
valor = float(input("Digite o valor da hora (reais): "))
horas = int(input("Digite o valor das horas: "))

calcular_total(valor, horas)
