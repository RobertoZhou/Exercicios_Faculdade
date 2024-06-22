# Implemente um programa em Python para verificar se um CPF digitado pelo
# teclado é um número válido.
#   – Um CPF tem nove dígitos e mais dois dígitos verificadores. Para verificar se um CPF é válido, utiliza-se
#       estes dois últimos dígitos como teste, após um cálculo que envolve os outros 9 dígitos.
#   – Inicialmente, multiplica-se cada um dos nove dígitos por um peso, e acumula-se em uma variável de
#       soma S1:
#           d1 d2 d3 d4 d5 d6 d7 d8 d9 (dígitos)
#            x 10 9 8 7 6 5 4 3 2 (pesos)
#   • O décimo dígito, d10, será obtido através do cálculo:
#       d10 = 11 - (resto de S1/11).
#   • Caso d10 seja maior que nove, então d10 recebe 0 (zero).
#        – Para calcular o décimo primeiro dígito repetimos o procedimento, considerando agora o décimo dígito:
#            d1 d2 d3 d4 d5 d6 d7 d8 d9 d10 (dígitos)
#             x 11 10 9 8 7 6 5 4 3 2 (pesos)
#   • O décimo primeiro dígito, d11, será obtido através do cálculo:
#       d11 = 11 - (resto de S2/11).
#   • Caso d11 seja maior que nove, então d11 recebe 0 (zero).
#       – CPF para teste: 001234567-97

def verificar_CPF(numCPF):
    soma = 0
    for cont_digito in range(9):
        soma += numCPF[cont_digito] * (10 - cont_digito)
    
    soma = 11 - (soma % 11)
    if soma > 9:
        soma = 0

    if soma != numCPF[9]:
        print("Problema 1º digito")
        return False
    
    soma = 0
    for cont_digito in range(10):
        soma += numCPF[cont_digito] * (11 - cont_digito)
    soma = 11 - (soma % 11)
    if soma > 9:
        soma = 0

    if soma != numCPF[10]:
        print("Problema 2º digito")
        return False
    return True

CPF = [0,0,1,2,3,4,5,6,7,9,7]
result = verificar_CPF(CPF)
if result == True:
    print("CPF válido")
else:
    print("CPF inválido")