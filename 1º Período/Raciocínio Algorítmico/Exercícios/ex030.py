# Dado um vetor de inteiros de 10 posições lido pelo teclado, desenvolver um
# programa para localizar e imprimir na tela a posição de um elemento qualquer,
# digitado pelo usuário. Caso o elemento não esteja armazenado no vetor, imprimir
# "Não está no vetor".

"""     1º Versão

vetor = []
for cont in range(10):
    valor = int(input("Digite um numero: "))
    vetor.append(valor)
print(vetor)
argPesquisa = int(input("Digite o numero para busca: "))
if vetor.count(argPesquisa) == 0:
    print("Nao está no vetor")
else:
    print("Dado encontrado na posição: ", vetor.index(argPesquisa))
"""

#       2º Versão
lista = []
for cont in range(5):
    lista.append(int(input("Digite um numero: ")))

arg = int(input("Digite um numero para localização: "))
cont = 0
while cont < (len(lista)):
    if lista[cont] == arg:
        break
    cont += 1

if cont <= (len(lista) - 1):
    print("Localizou em : ", cont)
else:
    print("Não Localizou")
