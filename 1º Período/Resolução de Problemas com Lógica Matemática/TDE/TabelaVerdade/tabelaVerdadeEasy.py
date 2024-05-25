#       Construir um interpretador de proposições compostas.

#   Na classe TabelaVerdade: Crie uma matriz para duas variáveis: p, q. Para cada variável atribua o valor de V ou F que a tabela verdade pede. Faça isso em um método chamado atribuicaoValoresTabela()
#   Na classe TabelaVerdade: crie um método para calcular a implicação de p -> q e adicione os resultados na matriz
#   Na classe TabelaVerdade: crie um método para calcular a implicação de p ^ q e adicione os resultados na matriz
#   Na classe TabelaVerdade: crie um método para calcular a implicação de p <-> q e adicione os resultados na matriz
#   Na classe Principal: peça para o usuário digitar uma fórmula com até 2 conectivos, exemplos de entradas válidas:

#   Importando módulo
from random import choice

class TabelaVerdade:
    def __init__(self, variaveis, expressao):
        self.variaveis = variaveis
        self.expressao = expressao

        #   Função que pega todas as possibilidade de V e F
    def atribuicaoValoresTabela(self):
        self.valoresTabela = []
        while len(self.valoresTabela) < 2 ** (len(self.variaveis)):
            varTemp = []
            for var in self.variaveis:
                varTemp.append(choice(["V", "F"]))
            if(varTemp not in self.valoresTabela):
                self.valoresTabela.append(varTemp)
        return sorted(self.valoresTabela, reverse=True)

    #   Função que da a resposta da expressao de 2 parâmetros    
    def resposta(self):
        #   Dividi a expressão em partes
        self.expressao[0].replace("not", " ~ ")
        self.expressao[0].replace("^", " and ")
        self.expressao = self.expressao[0].split()
        #   Análisa o sinal da expressao para dar a resposta da Tabela
        if(self.expressao[1] == "and"):
            return ["V", "F", "F", "F"]
        elif(self.expressao[0] == "~"):
            return ["F", "V"]
        elif(self.expressao[1] == "or"):
            return ["V", "V", "v", "F"]
        elif(self.expressao[1] == "=>"):
            return ["V", "F", "V", "V"]
        elif(self.expressao[1] == "<=>"):
            return ["V", "F", "F", "V"]



class Principal:
    def __init__(self, expressao, variaveis=["p", "q"]):
        self.expressao = expressao
        self.variaveis = variaveis
        tabela = TabelaVerdade(self.variaveis, self.expressao)
        self.resposta = tabela.resposta()
        self.possibilidades = tabela.atribuicaoValoresTabela()

    def montarTabela(self, corColuna=4, corTabela=3):
        #   Cor da Tabela Verdade
        corColuna = f"\033[7;3{corColuna}m"     #   4 - Cor Azul
        corTabela = f"\033[7;3{corTabela}m"     #   3 - Cor Amarelo
        corFinalizar = "\033[m"                 #   Indica o final da cor

        #   Função que cria a linha da tabela
        def linha(linha=".", coluna=".."):
            self.coluna = coluna
            for var in self.variaveis:
                print(f"{corColuna}|{self.coluna}|{linha * (len(var) + 5)}", end="")
            print(f"|{self.coluna}|{linha * (len(self.expressao[0]) + 7)}|{self.coluna}|{corFinalizar}")

        #   Montando a Tabela
        linha()
        #   Parte do head da tabela os parâmetros e a expressao
        for var in self.variaveis:
            print(f"{corColuna}|{self.coluna}|{corTabela}{var :^{len(var) + 5}}", end="")
        print(f"{corColuna}|{self.coluna}|{corTabela}{self.expressao[0] :^{len(self.expressao[0]) + 7}}{corColuna}|{self.coluna}|")
        linha()
        #   Preenchendo a tabela com as variaveis possiveis
        for quatdade, var in enumerate(self.possibilidades):
            for cont in range(len(self.variaveis)):
                print(f"{corColuna}|{self.coluna}|{corTabela}{var[cont] :^{len(self.variaveis[cont]) + 5}}", end="")
            #   Preenchendo a resolução da expressão
            print(f"{corColuna}|{self.coluna}|{corTabela}{self.resposta[quatdade] :^{len(self.expressao[0]) + 7}}{corColuna}|{self.coluna}|")
        linha()
        print("")

tabela1 = Principal(["~ p"], ["p"])
tabela2 = Principal(["p and q"])
tabela3 = Principal(["p or q"])
tabela4 = Principal(["p => q"])
tabela5 = Principal(["p <=> q"])

tabela1.montarTabela()
tabela2.montarTabela()
tabela3.montarTabela()
tabela4.montarTabela()