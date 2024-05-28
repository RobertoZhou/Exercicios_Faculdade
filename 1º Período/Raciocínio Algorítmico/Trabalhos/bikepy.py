#   Criando listas para armazenar informações
usuario = [0] * 3
registro_data = []
registro_horario = []
preco_hora = 5

#   titulo:
#       entrada: titulo
#       saida: cria um titulo personalizado
def titulo(texto):
    print("=======================================")
    print("     ", texto)
    print("=======================================")

#   menu:
#       entrada: recebe uma lista de opções
#       saída: cria as opções do menu de uma lista, e retorna a opção selecionada
def menu(lista):
    for contador in range(len(lista)):
        print(contador + 1, "-", lista[contador])
    print("Por favor, Digite Somente NÚMEROS!!!")
    opcao = int(input("Digite sua Opção: "))
    return opcao

#   criar_conta:
#       entrada: login, senha
#       saída: adiciona a lista usuario a conta criada
def criar_conta(login, senha, creditos):
    usuario[0] = login
    usuario[1] = senha
    usuario[2] = creditos
    print("Usuário Cadastrado(a), Com Sucesso!!!")

#   dica-senha:
#       entrada: login do usuário(a) cadastrado(a)
#       saída: dica de senha do usuário(a) cadastrado(a)
def dica_senha(login):
    if(login == usuario[0]):
        print("Começa com: [", usuario[1][0], "]")
        print("Termina com: [", usuario[1][-1], "]")
        return True
    else:
        print("LOGIN NÃO ENCONTRADO!!!")
        return False

#   visualizar_registro:
#       entrada: data e horario
#       saída: Imprimi na tela o histórico
def visualizar_registro(lista):
    for data in range(len(lista)):
        print("Data:", lista[data][0], "-", lista[data][1])
        print("Horário:", lista[data][0], "-", lista[data][1])

#   perguntar_data:
#       entrada: não recebe nenhum parâmetro de entrada
#       saída: retorna uma lista com a data, mês e ano
def perguntar_data():
    dia = 0
    mes = 0
    ano = 0
    lista = []
    while dia <= 0  or mes <= 0 or ano <= 0:
        dia = int(input("Digite o Dia Atual [DD]: "))
        mes = int(input("Digite o Mês Atual [MM]: "))
        ano = int(input("Digite o Ano Atual [YYYY]: "))
        if(dia <= 0  or mes <= 0 or ano <= 0):
            print("ERRO!!! DIA/MÊS/ANO INFORMADO INVÁLIDO!!!")
    lista.append(dia)
    lista.append(mes)
    lista.append(ano)
    return lista

#   perguntar_horario:
#       entrada: não recebe nenhum parâmetro de entrada
#       saída: retorna uma lista com as horas e minutos
def perguntar_horario():
    hora = -1
    minuto = -1
    lista = []
    while hora < 0 or minuto < 0:
        hora = int(input("Digite as Horas Atuais [DD]: "))
        minuto = int(input("Digite os Minutos Atuais [MM]: "))
        if(hora < 0 or minuto < 0):
            print("ERRO!!! HORA:MINUTOS INFORMADO INVÁLIDO!!!")
    lista.append(hora)
    lista.append(minuto)
    return lista


#   data_em_minutos:
#       entrada: dia, mês e ano
#       saída: transforma o dia+mês+ano em minutos
def data_em_minutos(dia, mes, ano):
    #   Info:
    #       1 dia = 24h
    #       1 hora = 60 min
    #       1 ano = 12 messes
    #       1 mês = 30 dias
    #   1. (Transforma DIA em horas e horas em minutos)
    #   2. (Transforma MÊS em dias, dias em horas e horas em minutos)
    #   3. (Transforma ANO em messes, messes em dias, dias em horas e horas em minutos)
    #   4. E soma tudo dando a data em minutos.
    calculo = (dia * 24 * 60) + (mes * 30 * 24 * 60) + (ano * 12 * 30 * 24 * 60)
    return calculo                                        

#   horario_em_minutos:
#       entrada: horas, minutos
#       saída: transforma o horario em minutos
def horario_em_minutos(horas, minutos):
    #   Info:
    #       1h = 60min
    return (horas * 60) + minutos

#   transforma_str:
#       entrada: recebe uma lista
#       saída: transforma os itens da lista em str
def transforma_str(lista):
    for contador in range(len(lista)):
        lista[contador] = str(lista[contador])
    return lista


#   Registrando o(a) usuário(a), salvando o login, senha e créditos
titulo("REGISTRAR-SE [BikePY]")
login = str(input("Digite Seu Login: "))
senha = str(input("Digite Sua Senha: "))
creditos = -1
while creditos < 0:
    creditos = float(input("Digite Quandos Créditos, Gostaria de Depositar: R$"))
    if(creditos < 0):
        print("ERRO!!! VALOR INFORMADO INVALIDO!!!")
        print("Tente Novamente!!!")
conta = criar_conta(login, senha, creditos)

opcao = 0
while opcao != 3:
    #   Menu princial
    titulo("MENU [BikePY]")
    lista_opcao = ["Login", "Esqueci minha senha", "Encerrar Programa"]
    opcao = menu(lista_opcao)

    if(opcao == 1):
        #   Sistema de login com 3 tentativas de login
        for contador in range(3, -1, -1):
            titulo("LOGIN [BikePY]")
            login = input("Digite Seu Login: ")
            senha = input("Digite Sua Senha: ")
            if(login == usuario[0] and senha == usuario[1]):
                break
            else:
                print("USUÁRIO NÃO ENCONTRADO!!!")
                print("Tentativas Restantes:", contador)

        if(login == usuario[0] and senha == usuario[1]):
            while opcao != 4:
                #   Menu de usuário
                titulo("MENU USUÁRIO [BikePY]")
                lista_opcao = ["Utilizar Serviço", "Visualizar Histórico", "Recarregar Créditos", "Encerrar Sessão"]
                opcao = menu(lista_opcao)
                if(opcao == 1):
                    titulo("UTILIZANDO O SERVIÇO [BikePY]")
                    if(usuario[2] >= 5):
                        print("Preço: R$", preco_hora, "[1 HORA]")
                        print("AVISO: Se o preço ultrapassar alguns minutos será cobrada a diferença!!!")
                        print("As DATAS e HORÁRIOS Digitar Somente Números!!!")
                        #   Sistema de utilização do serviço
                        #       Solicitando o dia, mês e ano da retirada da bike
                        print("=======================================")
                        data_inicial = perguntar_data()
                        print("=======================================")
                        horario_inicial = perguntar_horario()
                        titulo("ENCERRANDO SERVIÇO [BikePY]")
                        data_final = perguntar_data()
                        print("=======================================")
                        horario_final = perguntar_horario()

                        #   Transformando a data inicial e final em minutos
                        data_alugel = data_em_minutos(data_inicial[0], data_inicial[1], data_inicial[2])
                        horario_alugel = horario_em_minutos(horario_inicial[0], horario_inicial[1])
                        #   Transformando o horário inicial e final em minutos
                        data_devolucao = data_em_minutos(data_final[0], data_final[1], data_final[2])
                        horario_devolucao = horario_em_minutos(horario_final[0], horario_final[1])

                        #   Transformando o horário e data em str
                        data_inicial = transforma_str(data_inicial)
                        data_final = transforma_str(data_final)
                        horario_inicial = transforma_str(horario_inicial)
                        horario_final = transforma_str(horario_final)

                        #   transforma o horario no formato [DD/MM/YYYY] e adiciona no registro_data
                        data = [0] * 2
                        data[0] = data_inicial[0] + "/" + data_inicial[1] + "/" + data_inicial[2]
                        data[1] = data_final[0] + "/" + data_final[1] + "/" + data_final[2]
                        registro_data.append(data)
                        #   transforma a data no formato [DD:MM] e adiciona no registro_horario
                        horario = [0] * 2
                        horario[0] = horario_inicial[0] + ":" + horario_inicial[1]
                        horario[1] = horario_final[0] + ":" + horario_final[1]

                        #   Calculando a diferença de minutos entre o horario inicial e final
                        calcular_minutos = (data_devolucao + horario_devolucao) - (data_alugel + horario_alugel)
                        #   Cobra o valor do serviço de 1 hora
                        #   Caso o usuário passe alguns minutos a mais será cobrado a diferença
                        print("=======================================")
                        if(calcular_minutos >= 1):
                            registro_horario.append(horario)
                            if(calcular_minutos >= 1 and calcular_minutos <= 60):
                                preco_cobrado = preco_hora
                                usuario[2] = usuario[2] - preco_cobrado
                                print("Preço Do Serviço: R$", preco_cobrado)
                                print("Créditos Atuais: R$", usuario[2])
                            elif(calcular_minutos > 60):
                                preco_cobrado = (calcular_minutos / 60) * preco_hora
                                usuario[2] = usuario[2] - preco_cobrado
                                print("Preço Do Serviço: R$", preco_cobrado)
                                print("Créditos Atuais: R$", usuario[2])

                        else:
                                print("DATA ou HORÁRIO, Informado Invalido!!!")
                                print("VOLTANDO AO MENU!!!")
                    elif(usuario[2] >= 0 and usuario[2] < 5):
                        print("Preço do Serviço [1 HORA]: R$", preco_hora)
                        print("Créditos Atuais: R$", usuario[2])
                        print("CRÉDITOS INSUFICIENTE!!!")
                    if(usuario[2] < 0):
                        #   Caso o Usuário fique com Saldo Negativo um aviso será exibido
                        print("CRÉDITO NEGATIVO!!!")
                        print("AVISO: NA PROXIMA RECARGA O VALOR SERÁ DESCONTADO!!!")

                elif(opcao == 2):
                    #   Imprimi a data e o horario de uso do serviço
                    titulo("VISUALIZAR HISTÓRICO [BikePY]")
                    if(len(registro_horario) == 0):
                        print("Nenhum Registro Salvo no Momento")
                    else:
                        for data in range(len(registro_data)):
                            print("Data:", registro_data[data][0], "-", registro_data[data][1])
                            print("Horário:", registro_horario[data][0], "-", registro_horario[data][1])
                            print("=======================================")

                #   Sistema de deposito de crédito
                elif(opcao == 3):
                    titulo("RECARREGAR CRÉDITOS [BikePY]")
                    creditos = -1
                    while creditos < 0:
                        creditos = float(input("Digite Quantos Créditos Gostaria de Recarregar: R$"))
                        if(creditos < 0):
                            print("ERRO!!! VALOR DIGITADO INVÁLIDO!!!")
                            print("Tente Novamente!!!")
                    usuario[2] = usuario[2] + creditos
                    print("Crédito Atual: R$", usuario[2])
                    print("Preço do Serviço [1 HORA]: R$", preco_hora)
                elif(opcao == 4):
                    print("ENCERRANDO SESSÃO!!!")
                else:
                    print("OPÇÃO INVALIDO!!! Tente Novamente!!!")

    #   Dica da senha caso o usuário(a) esqueça sua senha dando o primeiro e ultimo digito da senha
    elif(opcao == 2):
        titulo("DICA DE SENHA [BikePY]")
        login = str(input("Digite Seu Login: "))
        dica = dica_senha(login)
        print("Voltando Para o Menu!!!")
    elif(opcao == 3):
        print("ENCERRANDO O PROGRAMA!!!")
    else:
        print("OPÇÃO INVALIDA!!! TENTE NOVAMENTE!!!")