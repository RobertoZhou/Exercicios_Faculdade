# Existe um cálculo simples para saber se o álcool é ou
# não mais vantajoso que a gasolina para abastecer
# automóveis: basta dividir o preço do litro do álcool
# pelo preço do litro da gasolina. Se o resultado for
# menor ou igual a 0.7, o álcool é mais vantajoso. Faça
# um programa em Python para imprimir na tela se o
# álcool é vantajoso, lendo do teclado o valor da
# gasolina e do álcool.

valor_gasolina = float(input("Valor gasolina: "))
valor_alcool = float(input("Valor álcool: "))
relacao = valor_alcool/valor_gasolina
if relacao <= 0.7:
    print("Alcool é mais vantajoso")
else:
    print("Gasolina é mais vantajosa")
