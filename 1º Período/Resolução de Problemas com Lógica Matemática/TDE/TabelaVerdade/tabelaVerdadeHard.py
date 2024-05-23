#       Construir um interpretador de proposições compostas.

#   Na classe TabelaVerdade: Crie uma matriz para duas variáveis: p, q. Para cada variável atribua o valor de V ou F que a tabela verdade pede. Faça isso em um método chamado atribuicaoValoresTabela()
#   Na classe TabelaVerdade: crie um método para calcular a implicação de p -> q e adicione os resultados na matriz
#   Na classe TabelaVerdade: crie um método para calcular a implicação de p ^ q e adicione os resultados na matriz
#   Na classe TabelaVerdade: crie um método para calcular a implicação de p <-> q e adicione os resultados na matriz

#   Na classe Principal: peça para o usuário digitar uma fórmula com até 2 conectivos, exemplos de entradas válidas:
#       p -> q <-> p
#       q ^ p v p
#       p ^ p v p
#       ~p ^ q -> p00
#       ~(p v q) ^ q
#   Mas lembre-se: agora seu usuário pode digitar 2 conectivos (ou mais )! E pode digitar negação.
#   Verifique a operação que o usuário deseja fazer (^ v -> <->).
#   Apresente o resultado da tabela verdade!

#   Importando Módulo
from random import choice

class TabelaVerdade:
    def __init__(self, conectivos, expressao):
        self.conectivos = conectivos
        self.expressao = expressao
        self.possibilidades = []
        self.resolucao = []

    #   Função que cria todas as possibilidades possiveis de V e F e a resolução da expressão
    def atribuicaoValoresTabela(self):
        while len(self.possibilidades) < 2 ** (len(self.conectivos)):
            varTemp = []
            varTemp.append(self.expressao[0])
            for var in self.conectivos:
                varTemp[0] = varTemp[0].replace(var, choice(["V", "F"]))

            if(varTemp not in self.possibilidades):
                self.possibilidades.append(varTemp)
            #   Resolvendo a expressão da Tabela Verdade   
                resolvendo = varTemp[0]
                #   Negação (not/~)
                resolvendo = resolvendo.replace("~ V", "F")
                resolvendo = resolvendo.replace("~ F", "V")
                #   Conjunção (and/^)
                resolvendo = resolvendo.replace("F and F", "F")
                resolvendo = resolvendo.replace("F and V", "F")
                resolvendo = resolvendo.replace("V and F", "F")
                resolvendo = resolvendo.replace("V and V", "V")
                #   Disjunção (or)
                resolvendo = resolvendo.replace("F or F", "F")
                resolvendo = resolvendo.replace("F or V", "V")
                resolvendo = resolvendo.replace("V or F", "V")
                resolvendo = resolvendo.replace("V or V", "V")
                #   Implicação (=>)
                resolvendo = resolvendo.replace("F => F", "V")
                resolvendo = resolvendo.replace("F => V", "V")
                resolvendo = resolvendo.replace("V => F", "F")
                resolvendo = resolvendo.replace("V => V", "V")
                #   Bi-Implicação/Bicondicional (<=>)
                resolvendo = resolvendo.replace("F <=> F", "V")
                resolvendo = resolvendo.replace("F <=> V", "F")
                resolvendo = resolvendo.replace("V <=> F", "F")
                resolvendo = resolvendo.replace("V <=> V", "V")
                self.resolucao.append(resolvendo)
        return self.possibilidades, self.resolucao

class Principal:
    def __init__(self, conectivos, expressao):
        self.conectivos = conectivos
        self.expressao = expressao
        #   Organizando a expressão
        self.expressao[0] = self.expressao[0].replace(" ", "")
        self.expressao[0] = self.expressao[0].replace("~", " ~ ")
        self.expressao[0] = self.expressao[0].replace("not", " ~ ")
        self.expressao[0] = self.expressao[0].replace("^", " and ")
        self.expressao[0] = self.expressao[0].replace("and", " and ")
        self.expressao[0] = self.expressao[0].replace("or", " or ")
        self.expressao[0] = self.expressao[0].replace("=>", " => ")
        self.expressao[0] = self.expressao[0].replace("<=>", " <=> ")

        tabela = TabelaVerdade(self.conectivos, self.expressao)
        self.possibilidades, self.resolucao, = tabela.atribuicaoValoresTabela()

    def montarTabela(self, corColuna=4, corTabela=3):
        #   Cor da Tabela Verdade
        corColuna = f"\033[7;3{corColuna}m"     #   4 - Cor Azul
        corTabela = f"\033[7;3{corTabela}m"     #   3 - Cor Amarelo
        corFinalizar = "\033[m"                 #   Indica o final da cor

        #   Função que cria a linha da tabela
        def linha(linha=".", coluna=".."):
            self.coluna = coluna
            print(f"{corColuna}|{self.coluna}|{linha * (len(self.possibilidades[0][0]) + 5)}", end="")
            print(f"|{self.coluna}|{linha * (len(self.expressao[0]) + 5)}|{self.coluna}|{corFinalizar}")
        linha()  
        #   Preenchendo a Tabela Verdade
        print(f"{corColuna}|{self.coluna}{corTabela}|{self.expressao[0] :^{(len(self.possibilidades[0][0]) + 7) + (len(self.expressao[0]) + 7)}}|{corColuna}{self.coluna}|")
        linha()
        for cont, var in enumerate(self.possibilidades):
            print(f"{corColuna}|{self.coluna}|{corTabela}{var[0] :^{len(self.possibilidades[0][0]) + 5}}", end="")
            print(f"{corColuna}|{self.coluna}|{corTabela}{self.resolucao[cont] :^{len(self.expressao[0]) + 5}}{corColuna}|{self.coluna}|{corFinalizar}")
        linha()

x = Principal(["p", "q"], ["p andq orp"])
x.montarTabela()
