# Implemente em Python a brincadeira de adivinhar o número que outra pessoa pensou.
# Funciona assim:
#   I. A pessoa A pensa um número “secreto” entre 1 e 100 e anota em um papel;
#   II. A pessoa B tenta acertar o número “chutando” um valor;
#   III. A pessoa A então informa se o número indicado por B está correto.
#       Se não estiver, a pessoa A indica se o número secreto é maior ou menor que o número dito por B;
#   IV. A brincadeira termina quando B acerta o número “secreto”.

pessoaA = int(input("Digite um número, entre 1 e 100: "))
pessoaB = int(input("Adivinhe o número digitado, entre 1 e 100: "))
while pessoaB != pessoaA:
    print("Número Incorreto!")
    if(pessoaB < pessoaA):
        print("É maior que", pessoaB)
    else:
        print("É menor que", pessoaB)
    print("Tente Novamente!")
    pessoaB = int(input("Adivinhe o número digitado, entre 1 e 100: "))
print("Você Acertou!")
