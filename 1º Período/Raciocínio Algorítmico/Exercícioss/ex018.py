# Construa um algoritmo que calcule a quantidade de latas de tinta necessárias e o custo para pintar
# tanques cilíndricos de combustível, em que são fornecidos a altura e o raio desse cilindro.
# • Sabe-se que:
#       • a lata de tinta custa 50,00 reais;
#       • cada lata contém 5 litros;
#       • cada litro de tinta pinta 3 metros quadrados.
#   • Dados de entrada: altura (H) e raio (R)
#   • Dados de saída: custo (C) e quantidade (QTDE)
# • Ajuda:
#       • custo é dado por quantidade de latas * 50.00;
#       • quantidade de latas é dada por quantidade total de litros/5;
#       • quantidade total de litros é dada por área do cilindro/3;
#       • área do cilindro = área da base + área lateral;
#       • área da base = (PI * R * R);
#       • área lateral = altura * comprimento: (2 * PI * R * H);
#       • sendo que R (raio) e H ( altura) são dados de entrada e PI é uma constante de valor conhecido: 3.14.

altura = float(input("Digite a altura: "))
raio = float(input("Digite o raio: "))
area_base = 3.14 * raio * raio
area_lateral = 2 * 3.14 * raio * altura
area_cilindro = area_base + area_lateral
quantidade_litros = area_cilindro / 3
quantidade_latas = quantidade_litros / 5
custo_total = quantidade_latas * 50.00
print("Custo total: ", custo_total)
print("Quantidade de latas: ", quantidade_latas)
