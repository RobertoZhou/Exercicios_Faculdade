# Dado o saldo de uma conta corrente, verificar se este é positivo ou negativo.
# Se negativo, imprimir o valor atual do saldo.

saldo = float(input("Digite seu saldo: R$"))
if(saldo < 0):
  print("Saldo negativo: R$", saldo)
if(saldo >= 0):
  print("Saldo Positivo")