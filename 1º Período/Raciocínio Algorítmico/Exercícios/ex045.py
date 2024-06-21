# Um pesquisador mediu a altura de 30 crianças e anotou em uma tabela. O seu
# objetivo é calcular a altura média das crianças, além de identificar a altura da
# maior criança bem como da menor. Sua tarefa é criar um programa em Python
# que ajude o pesquisador a realizar seu objetivo.

tabela_altura = []
for crianca in range(30):
    print(crianca+1, "º Criança")
    altura = float(input("Digite a altura da criança: "))
    tabela_altura.append(altura)

def media_altura(lista):
    altura_total = 0
    for crianca in range(len(lista)):
        altura_total += lista[crianca]
    media_altura = altura_total / len(lista)
    return media_altura

def verificar_maior_altura(lista):
    maior_altura = 0
    for crianca in range(len(lista)):
        if(lista[crianca] > maior_altura):
            maior_altura = lista[crianca]
    return maior_altura

def verificar_menor_altura(lista):
    menor_altura = lista[0]
    for crianca in range(len(lista)):
        if(lista[crianca] < menor_altura):
            menor_altura = lista[crianca]
    return menor_altura

maior_altura = verificar_maior_altura(tabela_altura)
menor_altura = verificar_menor_altura(tabela_altura)
media = media_altura(tabela_altura)
print("Maior altura:", maior_altura)
print("Menor altura:", menor_altura)
print("Média das alturas:", media)