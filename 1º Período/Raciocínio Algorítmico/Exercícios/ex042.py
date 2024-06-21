# Implemente um programa em Python para verificar se um número
# passado como argumento para um módulo está em um determinado
# intervalo de valores, também passado como argumento. Se estiver o
# módulo retorna True , senão False

def verificar_numero(lista):
    numero = int(input("Digite um número inteiro para verificar: "))
    for contador in range(len(lista)):
        if(lista[contador] == numero):
            return True
    return False

lista_numero = []
for contador in range(5):
    numero = int(input("Digite um número inteiro: "))
    lista_numero.append(numero)

verificar = verificar_numero(lista_numero)
if(verificar == True):
    print("O número existe!")
elif(verificar == False):
    print("O número não existe!")