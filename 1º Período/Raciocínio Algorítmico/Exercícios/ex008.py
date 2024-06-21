# Dada a idade de uma pessoa, avaliar se ela pode ou nâo pode dirigir.

idade = int(input("Digite sua Idade: "))
if(idade < 18):
  print("Tem", idade, "anos. Não pode dirigir!")
if(idade >= 18):
  print("Tem", idade, "anos. Pode dirigir!")