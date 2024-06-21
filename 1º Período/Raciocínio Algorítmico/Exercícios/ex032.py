# Um armazém trabalha com 100 mercadorias diferentes identificadas pelos
# números inteiros de 1 a 100. O dono do armazém anota a quantidade de cada
# mercadoria vendida durante o mês. Ele tem uma tabela que indica para cada
# mercadoria o preço de venda. Escreva o algoritmo para calcular o faturamento
# mensal do armazém, isto é:
# faturamento = Quantidade * preço

tabela_precos = []

# Preenchimento da lista de preços de venda das mercadorias
print("Digite os preços de venda das 100 mercadorias:")
for contador in range(100):
    print("Produto", contador)
    preco = float(input("Digite o preço do produto: R$"))
    tabela_precos.append(preco)

# Preenchimento da lista de quantidades vendidas das mercadorias
quantidade_vendida = []
print("Digite as quantidades vendidas das 100 mercadorias:")
for contador in range(100):
    print("Mercadoria", contador)
    quantidade = int(input("Digite a quantidade vendida da mercadoria: "))
    quantidade_vendida.append(quantidade)

faturamento_total = 0

# Calcular o faturamento para cada mercadoria
for contador in range(100):
    quantidade = quantidade_vendida[contador]
    preco = tabela_precos[contador]
    faturamento = quantidade * preco
    faturamento_total = faturamento_total + faturamento

print("faturamento mensal do armazém é: R$", faturamento_total)