# Construa uma lista com 5 notas de alunos, lidas pelo teclado.
# Depois imprima na tela a média das 5 notas.
# Imprima as notas maiores que a média calculada.

notas = []
for cont_notas in range(5):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)
soma = 0
for cont_notas in range(5):
    soma += notas[cont_notas]
media = soma / 5
print("Media:", media)
for cont_notas in range(5):
    if notas[cont_notas] > media:
        print("Nota maior que a média:", notas[cont_notas])
