# Dada a idade de uma pessoa, avaliar se ela pode ou não pode dirigir.
# Se não puder dirigir, informar enquanto tempo (em meses) poderá dirigir.

idade = int(input("Digite sua idade: "))
if(idade < 18):
    tempo_meses = (18 - idade) * 12
    print("Não pode dirigir!")
    print("Poderá dirigir após", tempo_meses, "meses!")
else:
    print("Pode dirigir!")
