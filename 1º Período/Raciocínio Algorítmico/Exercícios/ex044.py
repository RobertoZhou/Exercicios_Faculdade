# Um vendedor de carros está com dificuldade em calcular sua comissão a cada
# venda que realiza. Você irá ajudá-lo implementado um programa capaz de, dado
# o valor da venda (valor do carro) e o percentual da comissão, indicar quanto o
# vendedor ganhará.
#   • Exemplo:
#       • Valor da venda: 50.000,00 reais
#       • Comissão: 3%
#       • Ganho do vendedor: 1.500,00 reais
#   • PS: Obrigatório uso de função neste programa.

def calcular_comissao(valor, comissao):
    comissao_venda = valor * comissao
    return comissao_venda

valor_venda = float(input("Digite o valor da venda: R$"))
comissao_venda = float(input("Digite a comissão da venda: "))

valor_comissao = calcular_comissao(valor_venda, comissao_venda)
print("A comissão é de R$", valor_comissao)
