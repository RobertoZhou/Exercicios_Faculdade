verificar_registro = 0
while verificar_registro < 4:
    #   Registrar CLIENTE
    if(verificar_registro == 0):
        print("=====================================")
        print("         REGISTRAR CLIENTE")
        print("=====================================")
        print("Digite Apenas Números!!!")
        usuario_id = int(input("Digite Seu ID de Usuário: "))
        if(usuario_id > 0):
            verificar_registro = verificar_registro + 1
        else:
            print("Por Favor, Preencha o Campo Com Um ID, Maior Que ZERO!!!")
    if(verificar_registro == 1):
        usuario_senha = int(input("Digite Sua Senha: "))
        if(usuario_senha > 0):
            verificar_registro = verificar_registro + 1
        else:
            print("Por Favor, Preencha o Campo Com Uma Senha, Maior Que ZERO!!!")
    #   Registrar ADMINISTRADOR
    if(verificar_registro == 2):
        print("=====================================")
        print("      REGISTRAR ADMINISTRADOR")
        print("=====================================")
        print("Digite Apenas Números!!!")
        admin_id = int(input("Digite Seu ID de Administrador: "))
        if(admin_id > 0):
            verificar_registro = verificar_registro + 1
        else:
            print("Por Favor, Preencha o Campo Com Um ID, Maior Que ZERO!!!")
    if(verificar_registro == 3):
        admin_senha = int(input("Digite Sua Senha: "))
        if(admin_senha > 0):
            while(verificar_registro < 4):
                print("=====================================")
                preco_passagem = float(input("Por Favor, Digite o Valor da Passagem: R$"))
                print("=====================================")
                if(preco_passagem > 0):
                    verificar_registro = verificar_registro + 1
                    print("Preço da Passagem: R$", preco_passagem)
                else:
                    print("ERRO NO PREÇO DA PASSAGEM!!!")
                    print("Digite Um Valor Maior que ZERO!!!")
        else:
            print("Por Favor, Preencha o Campo Com Uma Senha, Maior Que ZERO!!!")

opcao = 0
saldo_credito = 0
#   Menu de Login
while opcao != 3:
    print("=====================================")
    print("                 MENU")
    print("=====================================")
    print("1 - Usuário.")
    print("2 - Administrador.")
    print("3 - Encerrar Sessão.")
    print("=====================================")
    print("Por Favor, Escolha entre [ 1, 2 e 3 ]")
    opcao = int(input("Qual Usuário acima você é: "))
    print("=====================================")

    if(opcao == 1):
        #   Login Cliente
        for contador in range(3, -1, -1):
            print("            LOGIN USUÁRIO")
            print("=====================================")
            print("Digite Apenas Números!!!")
            login_id_usuario = int(input("Digite o ID de USUÁRIO: "))
            login_senha_usuario = int(input("Digite a Senha de USUÁRIO: "))
            print("=====================================")
            if(login_id_usuario == usuario_id and login_senha_usuario == usuario_senha):
                break
            else:
                print("ID ou Senha Invalida!!!")
                print("Tentativas Restantes:", contador, "Tentativa")
                print("=====================================")
                if(contador == 0):
                    print("Voltando Para o Menu!!!")
        #   Menu Cliente
        if(login_id_usuario == usuario_id and login_senha_usuario == usuario_senha):
            while opcao != 5:
                print("=====================================")
                print("             MENU USUÁRIO")
                print("=====================================")
                print("1 - Visualizar Créditos.")
                print("2 - Depositar Crédito.")
                print("3 - Utilizar o Cartão.")
                print("4 - Atualizar Senha.")
                print("5 - ENCERRANDO SESSÃO.")
                print("=====================================")
                print("Por Favor, Escolha entre [ 1, 2, 3, 4 e 5 ]")
                opcao = int(input("Digite a Sua Opção:"))
                print("=====================================")
                #   Visualizar Créditos
                if(opcao == 1):
                    print("ID do Usuário:", usuario_id)
                    print("Créditos Possuído: R$", saldo_credito)

                #   Depositar Crédito
                elif(opcao == 2):
                    deposito_credito = 0
                    while deposito_credito <= 0:
                        print("=====================================")
                        print("ID do Usuário:", usuario_id)
                        print("Créditos Possuído: R$", saldo_credito)
                        print("Valor da Passagem: R$", preco_passagem)
                        print("=====================================")
                        deposito_credito = float(input("Digite o Valor Que Gostaria de Depositar: R$"))
                        print("=====================================")
                        if(deposito_credito > 0):
                            saldo_credito = saldo_credito + deposito_credito
                            print("Saldo Atual: R$", saldo_credito)
                        else:
                            print("ERRO DE DEPOSITO!!!")
                            print("Deposite Um Valor Maior que ZERO!!!")
                #   Utilizar o Cartão
                elif(opcao == 3):
                    if(saldo_credito >= preco_passagem):
                        print("Preço da Passagem: R$", preco_passagem)
                        print("PASSAGEM PASSADO COM SUCESSO!!!")
                        print("Boa-Viagem, Cliente do ID:", usuario_id)
                        saldo_credito = saldo_credito - preco_passagem
                        print("Saldo Restante: R$", saldo_credito, "Créditos")
                    else:
                        print("ERRO! Créditos Insuficiente!!!")
                        print("Valor da Passagem: R$", preco_passagem)
                        print("Crédito Atual: R$", saldo_credito, "Créditos")
                #   Atualizar Senha
                elif(opcao == 4):
                    print("ID do Usuário:", usuario_id)
                    print("Digite Apenas Números!!!")
                    usuario_senha = int(input("Digite a Nova Senha: "))
                    print("Nova Senha Cadastrado Com Sucesso")
                    print("Nova Senha:", usuario_senha)
                elif(opcao == 5):
                    print("ENCERRANDO SESSÃO!!!")
                #   Erro de Opção
                else:
                    print("OPÇÃO INVALIDA!!!")
    elif(opcao == 2):
        #   Login ADMINISTRADOR
        for contador in range(3, -1, -1):
            print("           LOGIN ADMINISTRADOR")
            print("=====================================")
            print("Digite Apenas Números!!!")
            login_id_admin = int(input("Digite o ID de ADMINISTRADOR: "))
            login_senha_admin = int(input("Digite a Senha de ADMINISTRADOR: "))
            print("=====================================")
            if(login_id_admin == admin_id and login_senha_admin == admin_senha):
                break
            else:
                print("ID ou Senha Invalida!!!")
                print("Tentativas Restantes:", contador, "Tentativa")
                print("=====================================")
                if(contador == 0):
                    print("Voltando Para o Menu!!!")
        #   Menu Administrador
        if(login_id_admin == admin_id and login_senha_admin == admin_senha):
            while opcao != 5:
                print("=====================================")
                print("         MENU ADMINISTRADOR")
                print("=====================================")
                print("1 - Visualizar Créditos do Usuário.")
                print("2 - Visualizar Preço da Passagem.")
                print("3 - Atualizar o Valor da Passagem.")
                print("4 - Atualizar Senha de Administrador.")
                print("5 - ENCERRANDO SESSÃO.")
                print("=====================================")
                opcao = int(input("Digite a Sua Opção:"))
                print("=====================================")
                #   Visualizar Créditos do Usuário
                if(opcao == 1):
                    print("ID do Cliente:", usuario_id)
                    print("Créditos Atuais: R$", saldo_credito)
                #   Visualizar Preço da Passagem
                elif(opcao == 2):
                    print("Preço da Passagem: R$", preco_passagem)
                #   Atualizar o Valor da Passagem
                elif(opcao == 3):
                    novo_preco_passagem = 0
                    while novo_preco_passagem <= 0:
                        novo_preco_passagem = float(input("Digite o Novo Preço da Passagem: R$"))
                        if(novo_preco_passagem > 0):
                            preco_passagem = novo_preco_passagem
                            print("Novo Preço da Passagem: R$", preco_passagem)
                        else:
                            print("ERRO NO VALOR DA PASSAGEM!!!")
                            print("Digite Um Valor Maior Que ZERO!!!")
                #   Atualizar Senha de Administrador    
                elif(opcao == 4):
                    print("ID do Administrador:", admin_id)
                    print("Digite Apenas Números!!!")
                    admin_senha = int(input("Digite a Nova Senha: "))
                    print("Nova Senha Cadastrado Com Sucesso")
                    print("Nova Senha:", admin_senha)
                #   Encerrando Sessão
                elif(opcao == 5):
                    print("ENCERRANDO SESSÃO!!!")
                #   Erro de Opção
                else:
                    print("OPÇÃO INVALIDA!!!")
    elif(opcao == 3):
        print("ENCERRANDO O PROGRAMA!!!")
    else:
        print("OPÇÃO INVALIDA!!!")
