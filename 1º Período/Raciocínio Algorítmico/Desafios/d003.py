# O n-grama pode ser entendido como uma subsequência de elementos
# dentro de uma sequência qualquer. O n-grama tem várias utilidades
# especialmente no processamento de textos. Quando n = 2, diz-se
# bigramas. Dada uma string lida pelo teclado, implementar um
# algoritmo que imprima na tela o número de bigramas únicos
# encontrados.
# • Exemplos:
#   • “parar” = {pa, ar, ra, ar} (4 bigramas e 2 únicos: pa, ra)
#   • “parado” = {pa, ar, ra, ad, do} (5 bigramas e 5 únicos: pa, ar, ra, ad, do)
#   • “amor” = {am, mo, or} (3 bigramas, sendo 3 únicos: am, mo, or)

palavra = input("Digite uma palavra: ")

# Lista para armazenar os bigramas
lista_bigrama = []
# Lista para armazenar bigramas únicos
bigramas_unicos = []
# Lista para armazenar bigramas iguais
bigramas_iguais = []

# Iteração para criar os bigramas e identificar únicos e iguais
for cont in range(len(palavra)-1):
    bigrama = palavra[cont:cont+2]
    lista_bigrama.append(bigrama)
    if bigrama not in bigramas_unicos:
        bigramas_unicos.append(bigrama)
    elif bigrama not in bigramas_iguais:  # Verifica se já está nos iguais para evitar repetições
        bigramas_iguais.append(bigrama)

unico = []
for cont in range(len(bigramas_unicos)):
    if(bigramas_unicos[cont] not in bigramas_iguais):
        unico.append(bigramas_unicos[cont])

# Imprimindo resultados
print(f"{palavra}: {lista_bigrama}")
print(f"{len(lista_bigrama)} bigramas, sendo {len(unico)} únicos: {unico}")
