# Implemente um algoritmo para somar o conteúdo de duas
# matrizes bidimensionais de ordem 2 do tipo inteiro, lidas pelo
# teclado, para uma terceira matriz.

n_Linhas = 2
n_Colunas = 2
matrizA = [0] * n_Linhas
matrizB = [0] * n_Linhas
matrizC = [0] * n_Linhas
for linha in range(n_Linhas):
    matrizA[linha] = [0] * n_Colunas
    matrizB[linha] = [0] * n_Colunas
    matrizC[linha] = [0] * n_Colunas

print('Matriz A')
for linha in range(n_Linhas):
    for coluna in range(n_Colunas):
        matrizA[linha][coluna] = int(input('Digite um valor: '))

print('Matriz B')
for linha in range(n_Linhas):
    for coluna in range(n_Colunas):
        matrizB[linha][coluna] = int(input('Digite um valor: '))
print('Matriz C')
for linha in range(n_Linhas):
    for coluna in range(n_Colunas):
        matrizC[linha][coluna] = matrizA[linha][coluna] + matrizB[linha][coluna]
print(matrizC)
