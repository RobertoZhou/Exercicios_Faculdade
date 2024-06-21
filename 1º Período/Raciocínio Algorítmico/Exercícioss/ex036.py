# Imprimir o conteúdo de uma matriz bidimensional de
# ordem 5 a partir da última linha e última coluna em direção a
# primeira linha e primeira coluna. O conteúdo da matriz deve
# ser lido previamente do teclado.

matriz_inicDireta = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
for linha in range(3):
    print("Linha", linha)
    for coluna in range(3):
        print(matriz_inicDireta[linha][coluna])
        
for linha in range(2, -1, -1):
    print("Linha", linha)
    for coluna in range(2, -1, -1):
        print(matriz_inicDireta[linha][coluna])
