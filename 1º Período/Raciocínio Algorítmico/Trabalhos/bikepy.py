# Descrição:
# • Implementar um programa em Python capaz
# de simular a operação do Sistema de
# Pagamentos de um serviço de locação de
# bicicletas.

# • O funcionamento do sistema será o seguinte:
# • Para usar, o consumidor deverá comprar créditos. Cada crédito permite o uso
# por uma hora.
# • Para usar, o consumidor deverá fornecer um login e senha.
# • O sistema deverá registrar o dia e horário de retirada e o dia e horário de
# devolução para cada locação feita.
# • Os créditos são atualizados a cada utilização do serviço.
# • O sistema deve permitir a impressão de relatórios (listar as utilizações
# realizadas anteriormente).
# • Permitir a atualização/modificação da quantidade de créditos disponíveis.
# • Não pode haver locação sem ao menos 5 créditos disponíveis.

contas = [["EVA", 1234]]
registro_de_uso = []


#   Função que cria um titulo personalizado
def titulo(texto):
    print("=======================================")
    print("     ", texto)
    print("=======================================")

#   Função que cria as opções do menu
def menu(lista):
    for contador in range(len(lista)):
        print(contador + 1, "-", lista[contador])
    print("Por favor, Digite Somente NÚMEROS!!!")

opcao = 0
while opcao != 3:
    titulo("MENU [ BikePY ]")
    menu(["Login", "Registrar-se", "Encerrar Programa"])
    opcao = int(input("Escola Uma Opção: "))

#   Parte do Menu de Login e Registro
    #   Login do Usuário
    if(opcao == 1):
        titulo("LOGIN [ BikePY ]")
        #   Usuário(a) tem até 3 tentativas de login, após isso ele voltará ao menu principal
        for tentativa in range(3, -1, -1):
            usuario = 0
            login = input("Digite seu Login: ")
            senha = int(input("Digite Sua Senha: "))
            #   Verificando se o Usuário existe
            for contador in range(len(contas)):
                if(login == contas[contador][0] and senha == contas[contador][1]):
                    usuario += contador
                    print("BEM-VINDO(a), Usuário(a)", login,",Entrando na Conta!!!")
            if(login == contas[usuario][0] and senha == contas[usuario][1]):
                break
            elif(tentativa > 0):
                print("Login Não Encontrado!!! Tente Novamente!!!")
                print("Tentativas Restantes:", tentativa)
                print("=======================================")
            else:
                print("VOLTANDO PARA O MENU!!!")
        if(login == contas[contador][0] and senha == contas[contador][1]):
            while opcao != 4:
                titulo("MENU DE USUÁRIO(a) [ BikePY ]")
                menu("Alugar uma Bike [1hora]", "Relatório de Uso", "Depositar Crédito", "Encerrar Sessão")
                opcao = int(input("Escolha uma Opção:"))

    elif(opcao == 2):
        titulo("REGISTRAR-SE [ BikePY ]")
        #   Criando novo(a) Usuário
        login = input("Digite seu Login: ")
        senha = int(input("Digite Sua Senha: "))
        creditos = float(input("Digite Quantos Créditos Gostaria de Depositar: R$"))
        contas.append([login, senha])

    elif(opcao != 1 and opcao != 2 and opcao != 3):
        print("=======================================")
        print("OPÇÃO INVALIDA!!! TENTE NOVAMENTE!!!")