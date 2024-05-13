#   Faça o teste de mesa dos algoritmos a seguir e informe no quadro em branco o que será impresso na tela:

var = 60
for cont in range(20, 100, 10):
    if cont == var:
        print("Saindo antes")
        break
    var = var - 10
print("Var = ", var)
#   Saindo antes
#   Var =  40


var = 8
for cont_ext in range(4):
    for cont_int in range(4):
        if cont_ext == cont_int:
            print("Var = ", var)
    print(cont_ext)
#   Var =  8
#   0
#   Var =  8
#   1
#   Var =  8
#   2
#   Var =  8
#   3