# Anacleto tem 1,50 metro e cresce 2 centímetros por ano, enquanto
# Felisberto tem 1,10 metro e cresce 3 centímetros por ano. Construa um
# algoritmo em Python que calcule e mostre quantos anos serão necessários
# para que Felisberto seja maior que Anacleto.

altura_anacleto = 1.50
altura_felisberto = 1.10
tempo_em_anos = 0
while altura_anacleto > altura_felisberto:
    altura_anacleto = altura_anacleto + 0.02
    altura_felisberto = altura_felisberto + 0.03
    tempo_em_anos = tempo_em_anos + 1
print("Tempo em anos:", tempo_em_anos)
