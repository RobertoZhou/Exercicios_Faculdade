# Implemente um programa em Python para controlar a conta
# bancária de uma pessoa, permitindo algumas operações
# básicas como:
#   • Criar a conta (com a definição do saldo inicial);
#   • Depósito;
#   • Retirada (somente se houver saldo);
#   • Impressão do saldo.

def criar_conta(saldo_inicial):
    global saldo
    saldo = saldo_inicial

def imprimir_saldo():
    print("Saldo:", saldo)

def depositar(novo_saldo):
    global saldo
    saldo += novo_saldo

def sacar(valor_sacado):
    global saldo
    if(saldo > 0):
        if(valor_sacado > 0 and valor_sacado <= saldo):
            saldo = saldo - valor_sacado
        else:
            print("Valor Insuficiente!")

criar_conta(200)
imprimir_saldo()
depositar(100)
valor_sacado = float(input("Digite o valor para sacar: R$"))
sacar(valor_sacado)
imprimir_saldo()
