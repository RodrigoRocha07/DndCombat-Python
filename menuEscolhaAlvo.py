from classes import *
import random

rodrigo = Guerreiro('Rodrigo',5, 4, 3, 15,4,4)
elisa = Clerigo('Elisa',50, 4, 3, 15,4,4)
karol = Clerigo('Karol', 40, 4, 3, 12, 4,4)
ciclope = Monstro('Ciclope', 40, 4, 3, 12, 4,4)


personagens = [rodrigo, elisa, ciclope, karol]


for a in range (len(personagens)):
   print(f'{a} - {personagens[a].nome}')

alvo = int(input('Selecione seu alvo: '))
print(f'{personagens[alvo].nome} Selecionado!!! ')


rodrigo.atacar(personagens[alvo])
