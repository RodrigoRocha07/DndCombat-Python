from classes import *
import random

rodrigo = Guerreiro('Rodrigo',15, 4, 3, 15,4,4)
elisa = Guerreiro('Elisa',15, 4, 3, 15,4,4)
ciclope = Monstro('Ciclope', 400, 4, 3, 12,4,4)



while (elisa.vida > 0 and ciclope.vida > 0):
#Ataque rodrigo
    if rodrigo.vida <= 0:
        rodrigo.vivo = False

    if rodrigo.vivo :
        rodrigo.atacar(ciclope)
    else:
        print(f'{rodrigo.nome} Morto')

#Ataque Elisa
    if elisa.vida <= 0:
        elisa.vivo = False


    if elisa.vivo:
        elisa.atacar(ciclope)
    else:
        print(f'{elisa.nome} Morto')

    if ciclope.vida <= 0:
        ciclope.vivo = False


#Ataque Ciclope
    if ciclope.vivo:
        if (rodrigo.vida > 0):
            ciclope.atacar(rodrigo)
        else:
            ciclope.atacar(elisa)
    else:
        print(f'{ciclope.nome} Morreu')

#Vida de cada um
    print("____________________")
    print(f'Rodrigo vida {rodrigo.vida}')
    print(f'Elisa vida {elisa.vida}')
    print(f'Ciclope vida {ciclope.vida}')
    print("____________________")






