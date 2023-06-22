from classes import *
import random
from personagens import personagens

def repeticao():
    continuar = int(input('Continuar? 1 - Sim  2 - Não: '))
    if continuar == 1:
        return  True
    elif continuar == 2:
        return  False
    

continuar = True
while continuar:
    print("Selecione seu alvo: ")
    for a in range (len(personagens)):
        print(f'{a} - {personagens[a].nome}')

        alvo = int(input(''))      





    continuar = repeticao()





