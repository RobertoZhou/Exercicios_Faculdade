#   Um desenvolvedor é conhecido como “Mister Digitação”, pois digita muito rapidamente os textos utilizando o teclado.
#   Implemente um programa em Python para calcular e imprimir na tela a quantidade de páginas que ele consegue digitar por hora.
#   O programa deve ler a quantidade de caracteres digitados em um minuto.
#   Cada página de texto tem 1.000 caracteres.

quantidade_caracteres_digitado = int(input("Quantidade Caracteres/Minutos: "))
quantidade_caracteres_hora = quantidade_caracteres_digitado * 60
quantidade_paginas = quantidade_caracteres_hora / 1000 
print("Quantidade de Páginas/Hora:", quantidade_paginas)