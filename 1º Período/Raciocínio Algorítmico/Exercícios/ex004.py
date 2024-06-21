# Um cinema possui um programa de fidelidade que oferece descontos para os clientes mais assíduos.
# Implemente um programa em Python para calcular quanto alguém deve pagar pela entrada do cinema, sabendo-se:
#   • Cada cliente pode comprar quantas entradas quiser;
#   • O cliente deve apresentar no ato do pagamento sua carteira que informa qual é o seu desconto atual (0 a 100%);
#   • O cliente poderá também descontar o valor do ticket do estacionamento no ato da compra.

valor_ingresso = float(input("Digite o valor do ingresso = "))
numero_ingressos = int(input("Digite o número de ingressos = "))
desconto = float(input("Digite seu desconto = "))
valor_estacionamento = float(input("Digite o valor estacionamento = "))
valor_pagar = (valor_ingresso * numero_ingressos) - ((valor_ingresso * numero_ingressos) * desconto)/100 - valor_estacionamento
print("Valor a pagar = ", valor_pagar)