# Crie uma matriz de notas para 3 alunos com 4 notas cada.
# Depois imprima na tela a média individual de cada aluno.

n_Linhas = 3
n_Colunas = 4
notas = [0] * n_Linhas
for linha in range(n_Linhas):
    notas[linha] = [0] * n_Colunas
    
for linha in range(n_Linhas):
    for coluna in range(n_Colunas):
        notas[linha][coluna] = float(input('Digite uma nota: '))

print(notas)

for linha in range(n_Linhas):
    soma = 0
    for coluna in range(n_Colunas):
        soma = soma + notas[linha][coluna]
    media = soma/n_Colunas
    print('Media:', media)
