from classes import *
import random

rodrigo = Guerreiro('Rodrigo',15, 4, 3, 15,4,4)
elisa = Guerreiro('Elisa',15, 4, 3, 15,4,4)
ciclope = Monstro('Ciclope', 40, 4, 3, 12,4,4)

ordem = {rodrigo.iniciativa : rodrigo, elisa.iniciativa: elisa}

ordem.sort(reverse=True)

print(ordem[0].nome)