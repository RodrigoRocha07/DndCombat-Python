from classes import *
import random

class Teste():
    def __init__(self, nome):
        self.nome = nome

def cadastrar():
    menuClasse = int(input('Selecione sua classe: \n1 - Guerreiro   2 - Clerigo   3 - Monstro: '))

    personagem = None

    nome = input('Nome: ')
    vida = int(input('Vida: '))
    forca = int(input('Força: '))
    pro = int(input('Proeficiencia: '))
    ca = int(input('Classe de armadura: '))
    inteligencia = int(input('Inteligencia: '))
    sabedoria = int(input('Sabedoria: '))

    if menuClasse == 1:
        personagem = Guerreiro(nome, vida, forca, pro, ca, inteligencia, sabedoria)
    elif menuClasse == 2:
        personagem = Clerigo(nome, vida, forca, pro, ca, inteligencia, sabedoria)
    elif menuClasse == 3:
        personagem = Monstro(nome, vida, forca, pro, ca, inteligencia, sabedoria)


    

    return personagem
