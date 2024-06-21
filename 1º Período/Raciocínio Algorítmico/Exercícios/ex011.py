# A tabela progressiva mensal do Imposto de Renda Retido na Fonte estabelece as seguintes alíquotas (valores e limites não atualizados):
#   • para salário de R$ 1.257,13 até R$ 2.512,08, alíquota de 15%
#   • para salário acima de R$ 2.512,08, alíquota de 27,5 %
# Escreva um algoritmo em Python que leia o salário de um funcionário e calcule o valor do desconto (aplicação da alíquota).


salario = float(input("Digite sua salário: R$"))
if(salario >= 1257.13 and salario <= 2512.08):
    imposto = salario * 0.15
    print(imposto)
elif(salario > 2512.08):
    imposto = (salario * 27.5) - salario
salario_descontado = salario - imposto
print("O salário é R$", salario_descontado)