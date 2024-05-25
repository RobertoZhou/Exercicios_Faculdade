#   O gerente de uma pizzaria gostaria de saber qual é o tempo médio de preparo de uma pizza.
#   Para tal, ele te contratou para escrever um programa, em Python, capaz de ler o tempo gasto de preparo de cada pizza.
#   A pizzaria produz 3 tipos diferentes de pizza:
#   “grande”, “gigante” e “hoje eu me acabo”.
#   O cálculo será feito para 10 preparos de pizza.
#   Ao final, imprimir na tela o tempo médio gasto para o preparo das pizzas, por tipo.

#   OBS: A SOLUÇÃO DESSE EXERCÍCIO E O MESMO DO ex03.py

tempo_pizza_grande = 0
tempo_pizza_gigante = 0
tempo_pizza_hoje_eu_me_acabo = 0

for cont in range(10):
    print("1 - Pizza Grande")
    print("2 - Pizza Gigante")
    print("3 - Pizza Hoje Eu Me Acabo")

    tipo_pizza = int(input("Digite o Tipo de Pizza: "))
    while tipo_pizza <= 0 or tipo_pizza > 3:
        print("Opção Inválida. Digite Uma Opção Valida!!!")
        tipo_pizza = int(input("Digite o Tipo de Pizza: "))

    tempo_preparo = int(input("Digite o Tempo Gasto do Preparo/Minutos: "))
    while tempo_preparo <= 0:
        print("Opção Inválida. Digite um Tempo em Minutos Valida!!!")
        tempo_preparo = int(input("Digite o Tempo Gasto do Preparo/Minutos: "))
    
    if(tipo_pizza == 1):
        tempo_pizza_grande = tempo_pizza_grande + tempo_preparo
    elif(tipo_pizza == 2):
        tempo_pizza_gigante = tempo_pizza_gigante + tempo_preparo
    else:
        tempo_pizza_hoje_eu_me_acabo = tempo_pizza_hoje_eu_me_acabo + tempo_preparo

    tempo_medio_pizza_grande = tempo_pizza_grande / 10
    tempo_medio_pizza_gigante = tempo_pizza_gigante / 10
    tempo_medio_pizza_hoje_eu_me_acabo = tempo_pizza_hoje_eu_me_acabo / 10

print("Tempo de Preparo das Pizzas:")
print("Pizza Grande/Minutos:", tempo_medio_pizza_grande)
print("Pizza Gigante/Minutos:", tempo_medio_pizza_gigante)
print("Pizza Hoje Eu Me Acabo/Minutos:", tempo_medio_pizza_hoje_eu_me_acabo)