from classes import *
import random
from cadastro import cadastrar
menuGeral = None
personagens = []
while menuGeral != 0:
    menuGeral = int(input('1 = Cadastrar 2 - Mostrar personagens  3 - Combate   0 - FINALIZAR:  '))

    if menuGeral == 1: 
        personagem = cadastrar()
        personagens.append(personagem)
    elif menuGeral == 2:
        if len(personagens) == 0:
            print('Nenhum personagem cadastrado!')
        else:
            for a in range (len(personagens)):
                print(f'{personagens[a].nome} -|- {personagens[a].classe}')


    elif menuGeral == 3:
        if len(personagens) == 0:
            print('Nenhum personagem cadastrado!')
        else:
            print("Selecione o jogador: ")
            for a in range (len(personagens)):
                print(f'{a} - {personagens[a].nome}')
            jogador = int(input(''))
            acao = int(input('AÇÃO: \n 1 -  Atacar   2 - Curar'))
            print('SELECIONE O ALVO')
            for a in range (len(personagens)):
                print(f'{a} - {personagens[a].nome}')
            alvo = int(input())
            if acao == 1:
                personagens[jogador].atacar(personagens[alvo])
            elif acao == 2:
                if personagens[jogador].classe == 'Clerigo':
                    personagens[jogador].curar(personagens[alvo])
                else:
                    print('VOCE NAO TEM ESSA HABILIDADE!')

print('FIM!')


#PROXIMOS PASSOS:
# organizar estrutura e laço do combate - se estiver vivo ataca se n mostra que esta morto



