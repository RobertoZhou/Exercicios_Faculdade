# Implemente um programa em Python para ler do teclado a nota de um aluno.
# Verificar se o valor lido é uma nota válida.
# Se não for, ler este valor até que a mesma seja válida.

nota = float(input("Digite um nota: "))
while nota < 0 or nota > 10:
    print("[ERRO] Valor Inválido!")
    nota = float(input("Digite um nota: "))
print("A nota do aluno(a) é", nota)