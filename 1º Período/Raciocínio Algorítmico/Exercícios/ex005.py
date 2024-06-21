# Escreva um algoritmo capaz de imprimir na tela o número de minutos transcorridos entre duas medidas realizadas em um mesmo dia e lidas pelo teclado de acordo com o formato a seguir:
#   • Exemplo: M1 = 9h30; M2 = 11h10

hora_inicial = int(input("Digite a hora inicial = "))
minuto_inicial = int(input("Digite o minuto inicial = "))
hora_final = int(input("Digite a hora final = "))
minuto_final = int(input("Digite o minuto final = "))
hora_inicial_transcorrido = hora_inicial*60 + minuto_inicial
hora_final_transcorrido = hora_final*60 + minuto_final
diferenca = hora_final_transcorrido - hora_inicial_transcorrido
print("Minutos transcorridos = ", diferenca)