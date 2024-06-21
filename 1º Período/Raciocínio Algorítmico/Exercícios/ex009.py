# Um caminhão tem capacidade de transportar C caixas contendo exclusivamente livros.
# Cada caixa tem a capacidade de adicionar L livros.
# Calcule:
#   • quantos livros podem ser transportados pelo caminhão;
#   • se cada livro pesa P quilos, qual a carga total transportada?

caixas = int(input("Digite a quantidade de caixas: "))
livros = int(input("Digite a quantidade de livros por caixa: "))
peso = float(input("Digite o peso do livro: "))

quantidade_livros = livros * caixas
peso_total = livros * peso

print("A quantidade que pode ser transportados é", quantidade_livros, "livros")
print("A carga total transportada é", peso_total, "Kg")