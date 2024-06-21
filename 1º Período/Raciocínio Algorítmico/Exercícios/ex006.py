# Dado o exercício do cálculo da média, verificar se o aluno está aprovado.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if(media >= 7):
  print("Aprovado!")
if(media < 7):
  print("Reprovado!")