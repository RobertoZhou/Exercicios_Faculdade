# A partir de uma string lida pelo teclado, como você faria para contar
# o número de palavras presentes na string? Implemente a solução em
# uma função que recebe a string e retorna a quantidade de palavras.

def contar_palavras(texto):
    # Remove espaços em branco extras no início e no final
    texto = texto.strip()

    # Divida a string em palavras usando split()
    palavras = texto.split()

    # Retorne o número de palavras
    return len(palavras)

texto = input("Digite uma frase para contar as palavras: ")
numero_palavras = contar_palavras(texto)
print(f"O número de palavras na frase é: {numero_palavras}")