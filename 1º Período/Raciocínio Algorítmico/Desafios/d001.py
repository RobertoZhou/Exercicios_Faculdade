# Um determinado material radioativo perde metade de sua
# massa a cada 50 segundos. Dada a massa inicial, em gramas,
# fazer um algoritmo que determine o tempo necessário para que
# a massa se torne menor do que 0,5 grama. Imprima como dado
# de saída a massa final e o tempo calculado em segundos.

# Solicita a massa inicial do material radioativo
massa_inicial = float(input("Digite a massa inicial do material (em gramas): "))

# Define a constante de tempo para a perda de metade da massa
tempo_decaimento = 50  # em segundos
massa_final = massa_inicial
tempo_total = 0

# Loop para calcular o tempo necessário até que a massa seja menor que 0,5 grama
while massa_final >= 0.5:
    massa_final = massa_final / 2
    tempo_total += tempo_decaimento

# Exibe a massa final e o tempo total calculado
print(f"A massa final é {massa_final:.2f} gramas.")
print(f"O tempo total necessário é {tempo_total} segundos.")