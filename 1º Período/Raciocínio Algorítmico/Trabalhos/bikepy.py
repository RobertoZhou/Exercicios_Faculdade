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

contas = [["EVA", 1234, 5]]
registro_horario = []
registro_data = []
preco_hora = 5

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
                menu(["Alugar uma Bike [1hora]", "Relatório de Uso", "Depositar Crédito", "Encerrar Sessão"])
                opcao = int(input("Escolha uma Opção:"))
                if(opcao == 1):
                    if(contas[usuario][2] >= 5):
                        horario = []
                        titulo("Serviço BikePY")
                        print("AVISO: SERÁ COBRADO A DIFERENÇA SE PASSAR DE ALGUNS MINUTOS, DEPOIS DE 1 HORA!!!")
                        print("Alugando uma BIKE [ 1 hora ]")
                        #   Solicitando o ANO, MÊS e DIA Iniciais
                        dia_inicial = int(input("Digite o dia inicial: "))
                        mes_inicial = int(input("Digite o mês inicial: "))
                        ano_inicial = int(input("Digite o ano inicial: "))

                        #   Solicitando a HORA, Minutos Iniciais
                        hora_inicial = int(input("Digite Quantas Horas São [HH]: "))
                        minutos_inicial = int(input("Digite Quantos Minutos São [MM]: "))
                        horario.append([hora_inicial, minutos_inicial])

                        titulo("Finalizando Serviço BikePY")
                        #   Solicitando o ANO, MÊS e Dia finais
                        dia_final = int(input("Digite o dia final: "))
                        mes_final = int(input("Digite o mês final: "))
                        ano_final = int(input("Digite o ano final: "))

                        #   Solicitando a HORA, MINUTOS finais
                        hora_final = int(input("Digite Quantas Horas São [HH]: "))
                        minutos_final = int(input("Digite Quantos Minutos São [MM]: "))
                        horario.append([hora_final, minutos_final])

                        registro_horario.append(horario)

                        #   12 = Mêsses do ano
                        #   30 = Dias
                        #   24 = Horas
                        #   60 = Minutos
                        #   Calculo para ver a diferença de tempo inicial e final
                        calculando_dias_iniciais = (ano_inicial * 12 * 30 * 24 * 60) + (mes_inicial * 30 * 24 * 60) + (dia_inicial * 24 * 60)
                        calcular_minutos_iniciais = (hora_inicial * 60) + minutos_inicial

                        calcular_dias_finais = (ano_final * 12 * 30 * 24 * 60) + (mes_final * 30 * 24 * 60) + (dia_final * 24 * 60)
                        calcular_minutos_final = (hora_final * 60) + minutos_final

                        calcular_minutos = (calcular_dias_finais + calcular_minutos_final) - (calculando_dias_iniciais + calcular_minutos_iniciais)

                        #   Calcula o preço do serviço
                        if(calcular_minutos <= 60 and calcular_minutos > 0):
                            calcular_preco = 5
                        elif(calcular_minutos > 60 and calcular_minutos > 0):
                            calcular_preco = (calcular_minutos / 60 )* 5
                        
                        contas[usuario][2] = contas[usuario][2]- calcular_preco
                        print("Preço do Serviço: R$", calcular_preco)
                        print("Créditos Atuais:", contas[usuario][2])

                    else:
                        print("SALDO INSUFICIENTE!!")
                        print("Preço do Serviço de Bike: R$", preco_hora)
                        print("Créditos Atuais: R$", contas[usuario][2])
                        if(contas[usuario][2] < 0):
                            print("SALDO NEGATIVO!!! NA RECARGA O VALOR SERÁ COBRADO!!!")

    elif(opcao == 2):
        titulo("REGISTRAR-SE [ BikePY ]")
        #   Criando novo(a) Usuário
        login = input("Digite seu Login: ")
        senha = int(input("Digite Sua Senha: "))
        saldo_creditos = -1
        while saldo_creditos < 0:
            saldo_creditos = float(input("Digite Quantos Créditos Gostaria de Depositar: R$"))
        contas.append([login, senha, saldo_creditos])

    elif(opcao != 1 and opcao != 2 and opcao != 3):
        print("=======================================")
        print("OPÇÃO INVALIDA!!! TENTE NOVAMENTE!!!")