# Implemente um algoritmo em Python capaz de ler 5 inteiros do
# teclado e imprimir na tela o maior número digitado.
# Dica: você vai precisar utilizar o for e o if neste exercício.

atualMaiorNumero = int(input("Digite um numero inteiro: "))
for contNumero in range(1, 5, 1):
    novoNumero = int(input("Digite um numero inteiro: "))
    if novoNumero > atualMaiorNumero:
        atualMaiorNumero = novoNumero

print("Maior numero digitado:", atualMaiorNumero)