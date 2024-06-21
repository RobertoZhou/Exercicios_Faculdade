# Implemente um programa em Python para ler do teclado a nota de um aluno.
# Verificar se o valor lido é uma nota válida.
# Se não for, ler este valor até que a mesma seja válida.

nota = float(input("Digite a nota (entre 0 e 10): "))
while nota < 0 or nota > 10:
    print("Nota invalida. Digite novamente.")
    nota = float(input("Digite a nota (entre 0 e 10): "))