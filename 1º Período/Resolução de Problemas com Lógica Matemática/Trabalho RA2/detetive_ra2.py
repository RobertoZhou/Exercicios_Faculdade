import os
from random import choice

os.system ("cls") # Limpa a tela do terminal

culpado_do_crime = "filho" 
arma_do_crime = "faca"
pistas = [
"Um copo quebrado no escritório. No escritório do Sr. Toduro, um copo de vidro foi encontrado quebrado perto da mesa. Havia marcas de sangue no vidro quebrado, indicando que alguém se machucou durante o incidente. Fragmentos do copo estavam espalhados, sugerindo que ele foi arremessado ou derrubado durante uma luta.",

"Uma carta ameaçadora na mesa. Sobre a mesa do Sr. Toduro, uma carta com conteúdo ameaçador foi encontrada. A carta dizia: 'Se não pagar sua dívida, você vai pagar com a vida.' A caligrafia parecia familiar aos empregados, lembrando a do filho do Sr. Toduro. A carta estava datada de dois dias antes do assassinato.",

"Marcas de lama no corredor. No corredor que leva ao escritório, foram encontradas marcas de lama fresca, sugerindo que alguém entrou ou saiu da mansão pelo jardim recentemente. As marcas pareciam vir da direção do jardim e seguiam até o escritório, indicando que o assassino pode ter passado por ali.",

"A empregada viu alguém sair às pressas. A empregada relatou que viu o filho do Sr. Toduro sair da mansão às pressas pouco depois da hora do crime. Ela descreveu que ele estava nervoso e carregava algo que parecia ser uma arma. A empregada reconheceu o filho do Sr. Toduro pela roupa que ele usava na noite anterior.",

"O mordomo tinha um álibi duvidoso. O mordomo alegou que estava na cidade comprando mantimentos na hora do assassinato, mas não conseguiu apresentar recibos ou testemunhas que pudessem confirmar seu álibi. Além disso, ele foi visto entrando na mansão pouco depois do crime, o que levantou suspeitas sobre sua possível participação.",

"Um pedaço de tecido rasgado na janela. Um pedaço de tecido azul escuro, semelhante ao do casaco do filho do Sr. Toduro, foi encontrado preso na janela do escritório. A janela estava aberta, sugerindo que alguém pode ter entrado ou saído por ali. O tecido parecia estar rasgado de forma abrupta, indicando uma fuga apressada.",

"A arma do crime foi encontrada no jardim. A arma está scondida entre os arbustos. Ele havia tentado pedir dinheiro ao pai várias vezes sem sucesso, o que fornecia um forte motivo financeiro para o crime.",

"Empregados mencionam uma discussão acalorada. Vários empregados relataram ter ouvido uma discussão acalorada entre o Sr. Toduro e seu filho na noite anterior ao assassinato. A discussão parecia estar relacionada a problemas financeiros e dívidas, e terminou com o filho saindo furioso do escritório.",

"O diário do Sr. Toduro menciona uma ameaça. O diário do Sr. Toduro continha anotações recentes sobre ameaças que ele estava recebendo, mencionando especificamente problemas financeiros e dívidas com agiotas. Uma entrada dizia: 'Meu próprio filho está envolvido, não sei mais em quem confiar. ",

"O filho do Sr. Toduro tinha uma grande dívida. Descobriu-se que o filho do Sr. Toduro estava com uma grande dívida de jogo e devia dinheiro a agiotas perigosos. A faca tinha lama e impressões digitais que correspondiam ao filho do Sr. Toduro. A arma combinava com as feridas encontradas no corpo do Sr. Toduro, confirmando ser a arma do crime."
]

print("="*22, "A MORTE DE DOUGLAS" , "="*22)


def menu(escolhas):
    print('='*64)
    for opcao in range(len(escolhas)):
        print(f'{opcao+1} - {escolhas[opcao]} ')
    print('='*64)
    opcao = int(input('Escolha sua opção (NÚMERO): '))
    return opcao

opcoes = ['Dica', 'Arma do Crime', 'Culpado']

print('Na remota Mansão Maromba,\no milionário Sr. Toduro foi encontrado morto\nem seu escritório.\nComo detetive, sua missão é descobrir\nquem o matou e qual foi a arma do crime.')

while True:
    escolha = menu(opcoes)
    if escolha == 1:
        if len(pistas) != 0:
            pistasAleatorias = choice(pistas)
            salvandoPista = pistasAleatorias
            pistas.remove(salvandoPista)
            print(salvandoPista)
        else:
            print('Não há mais pistas.')
    elif escolha == 2:
        if opcoes[1] == 'Arma do Crime':
            arma = str(input('Digite a arma do crime: ')).lower()
            if arma_do_crime in arma:
                print(arma_do_crime)
                print('Você acertou!')
                opcoes.remove('Arma do Crime')
            else:
                print('\033[31mVocê errou! Tente Novamente.\033[m')
        elif opcoes[1] == 'Culpado':
            culpado = str(input('Digite o culpado do crime: ')).lower()
            if culpado_do_crime in culpado:
                print(culpado_do_crime)
                print('Você acertou!')
                opcoes.remove('Culpado')
            else:
                print('\033[31mVocê errou! Tente Novamente.\033[m')
    elif escolha == 3:
        culpado = str(input('Digite o culpado do crime: ')).lower()
        if culpado_do_crime in culpado:
            print(culpado_do_crime)
            print('Você acertou!')
            opcoes.remove('Culpado')
        else:
            print('\033[31mVocê errou! Tente Novamente.\033[m')
    else:
        print('Opção inválida')


    
    if len(opcoes) == 1:
        print('Você descobriu o culpado e a arma do crime. Você é um ótimo detetive!')
        break