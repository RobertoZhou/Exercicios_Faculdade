# Implemente um programa em Python para imprimir na tela a
# sequência de trocas de discos para resolver o problema das torres de
# Hanoi para n discos.
#   • Dica:
#       • def hanoi(discos, origem, destino, temp)

def hanoi(discos, origem, destino, temp):
    if discos == 1:
        print("Mova o disco ", discos, " de ", origem, " para ", destino)
    else:
        hanoi(discos - 1, origem, temp, destino)
        print("Mova o disco ", discos, " de ", origem, " para ", destino)
        hanoi(discos-1, temp, destino, origem)
        
print("Entre com o numero de discos: ")
total_discos = int(input())
hanoi(total_discos,'A','B','C')
