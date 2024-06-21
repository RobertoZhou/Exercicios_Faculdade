# • Captcha:
#   • Acrônimo da expressão “Completely Automated Public Turing test to tell Computers and
#       Humans Apart” (teste de Turing público automatizado para diferenciação entre
#       computadores e humanos) (fonte: Wikipedia).
#   • Implementar um programa em Python capaz de gerar um Captcha e permitir sua avaliação.
# • Detalhes
#   • O programa deverá ser capaz de gerar um captcha de 6 caracteres. O captcha
#       obrigatoriamente deve conter letras (a-z) e números (0-9).
#   • Após sua geração, o programa deve permitir a leitura de um conjunto de caracteres pelo
#       teclado e a comparação com o captcha anteriormente gerado.

# Importanto biblioteca
from random import choice

lista_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_letra = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

tabela_caracteres = []
for contador in range(3):
    numero_aleatorio = choice(lista_numeros)
    letra_aleatorio = choice(lista_letra)
    tabela_caracteres.append(letra_aleatorio)
    tabela_caracteres.append(numero_aleatorio)

captcha = ""
for caracter in tabela_caracteres:
    captcha += str(caracter)

for tentativa in range(5, -1, -1):
    print(f"{captcha}")
    usuario = input("Digite o Captcha acima: ")
    if(usuario == captcha):
        print("Captcha Correto!")
        break
    else:
        print(f"[Captcha Incorreto!] {tentativa} Tentativa!")