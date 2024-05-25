#    Um professor quando corrige suas provas atribui uma nota de 0 a 100.
#   Ocorre que a escola onde trabalha este professor divulga as notas aos alunos sob a forma de conceitos, como apresentado na tabela abaixo:

#   Nota     Conceito
# 0             E
# 1 a 35        D
# 36 a 60       C
# 61 a 85       B
# 86 a 100      A

#   Você deve escrever um programa em Python que recebe uma nota no sistema numérico e determina (imprimir na tela) o conceito correspondente.

nota = float(input("Digite a Nota do Aluno: "))
if nota == 0:
    print("Conceito E")
elif nota >= 1 and nota <= 35:
    print("Conceito D")
elif nota >= 36 and nota <= 60:
    print("Conceito C")
elif nota >= 61 and nota <= 85:
    print("Conceito B")
elif nota >= 86 and nota <= 100:
    print("Conceito A")
else:
    print("Nota Inválida!!!")
