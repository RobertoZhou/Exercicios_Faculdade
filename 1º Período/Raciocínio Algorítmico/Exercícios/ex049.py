# Descubra como calcular o IMC (Índice de Massa Corporal) e crie uma
# função para retornar o IMC de uma pessoa.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = 70  # em quilogramas
altura = 1.75  # em metros

imc = calcular_imc(peso, altura)
print("O IMC é:", imc)