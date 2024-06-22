# Modifique os algoritmos a seguir para usarem o while em substituição ao for:

#       1º Teste de mesa

#   Utilizando o for:
var = 60
for cont in range(10, 100, 10):
    if cont == var:
        print("Saindo antes")
        break

    var = var - 10
    
print("Var = ", var)

#   Utilizando o while:
var = 10
cont = 10
while cont < 100:
    if cont == var:
        print("Saindo antes")
        break

    var = var - 10
    cont = cont + 10

print("Var = ", var)


#       2º Teste de mesa

#   Utilizando o for:
var = 5
for cont_ext in range(4):
    for cont_int in range(4):
        if cont_ext == cont_int:
            print("Var = ", var)

    print(cont_ext)

#   Utilizando o while:
var = 5
cont_ext = 0
while cont_ext < 4:
    cont_int = 0
    while cont_int < 4:
        if cont_ext == cont_int:
            print("Var = ", var)
        cont_int = cont_int + 1

    print(cont_ext)
    cont_ext = cont_ext + 1