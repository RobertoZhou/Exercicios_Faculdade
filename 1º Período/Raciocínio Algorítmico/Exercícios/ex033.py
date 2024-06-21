# Implemente um programa em Python que seja capaz de criar uma
# string e imprimir na tela:
#   • quantas vezes foram encontradas as letras vogais;
#   • quantos espaços existem no texto.

texto = input("Digite um texto: ")
cont_Vogal = 0
cont_Espaco = 0
for cont in range(len(texto)):
    if texto[cont] == 'a' or texto[cont] == 'A' \
        or texto[cont] == 'e'or texto[cont] == 'E' \
        or texto[cont] == 'i' or texto[cont] == 'I' \
        or texto[cont] == 'o' or texto[cont] == 'O' \
        or texto[cont] == 'u' or texto[cont] == 'U':
        cont_Vogal += 1
    else:
        if texto[cont] == ' ':
            cont_Espaco += 1
print("Vogais:", cont_Vogal)
print("Espaços:", cont_Espaco)
