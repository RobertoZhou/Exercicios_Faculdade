# Imprima na tela a tabuada de um número inteiro lido pelo teclado

contador = 1
soma = 0
numero = int(input("Numero para calculo da tabuada: "))
while contador < 11:
    soma = numero * contador
    print(numero, "x", contador, "=", soma)
    contador = contador + 1
