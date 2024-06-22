# Implemente um programa em Python para criptografar palavras (lidas pelo
# teclado) utilizando a seguinte estratégia: cada letra da palavra original será
# modificada por outra letra, como segue:
# Original  |   Criptografia
#   A               D
#   B               E
#   C               F
#   D               G
#   E               H
#  ...             ...
#   X               A
#   Y               B
#   Z               C
# • Imprimir na tela a palavra criptografada.

def criptografar_texto(alfabeto_original, alfabeto_criptografada, texto_criptografada):
    texto_original = ""
    for letra in range(len(texto_criptografada)):
        for criptografada in range(len(alfabeto_criptografada)):
            if(texto_criptografada[letra] ==  alfabeto_criptografada[criptografada]):
                texto_original += alfabeto_original[criptografada]
    return texto_original

original = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

criptografia = ["D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C"]

frase_criptografada = input("Digite o Texto Criptografado: ").upper()
frase_original = criptografar_texto(original, criptografia, frase_criptografada)
print("Texto Criptografado:", frase_criptografada)
print("Texto Descriptografado:", frase_original)