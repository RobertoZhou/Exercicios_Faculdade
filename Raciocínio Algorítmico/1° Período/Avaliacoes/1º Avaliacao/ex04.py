#   Se a variável A tem conteúdo igual a 1 e a variável B tem conteúdo igual a 2, como trocar o conteúdo de ambas entre si?
#   Implemente um programa em Python para trocar o conteúdo das duas variáveis e imprimi-las na tela.

var_A = 1
var_B = 2
var_temporario = var_A
var_A = var_B
var_B = var_temporario
print("Variavel A:", var_A)
print("Variavel B:", var_B)