# Implemente uma calculadora em Python capaz de realizar as
# seguintes operações elementares envolvendo inteiros:
#   • Somar dois valores;
#   • Dividir dois valores;
#   • Multiplicar dois valores;
#   • Subtrair dois valores;
#       • Todos os resultados devem ser impressos na tela (fora do módulo);
#       • Utilizar passagem de parâmetros e retorno.

def adicao(num1, num2):
    return num1 + num2

def divisao(num1, num2):
    return num1 / num2

def multiplicacao(num1, num2):
    return num1 * num2

def subtracao(num1, num2):
    return num1 - num2

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número:"))

somar = adicao(num1, num2)
divir = divisao(num1, num2)
multiplicar = multiplicacao(num1, num2)
subtrair = subtracao(num1, num2)

print(num1, "+", num2, "=", somar)
print(num1, "/", num2, "=", divir)
print(num1, "x", num2, "=", multiplicar)
print(num1, "-", num2, "=", subtrair)