import random

class Guerreiro():
    def __init__(self, nome, vida, forca, pro, ca,  inteligencia, sabedoria):
        self.nome = nome
        self.vida = vida
        self.vidaMax = vida
        self.forca = forca
        self.pro = pro
        self.ca = ca
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.vivo = True
        self.classe = 'Guerreiro'
        self.iniciativa = random.randint(1,20)


    def atacar(self, alvo):
        self.d20 = random.randint(1, 20)
        self.dano = random.randint(1, 8)
        danoTotal = self.dano + self.forca + self.pro
        if (self.d20 == 20):
            print(f'D20: {self.d20}')
            alvo.vida -= danoTotal*2
            print(f'{self.nome} causou {danoTotal *2} de dano em {alvo.nome}')
        else:
            if ((self.d20 + self.forca + self.pro) >= alvo.ca):
                print(f'D20: {self.d20}')
                alvo.vida -= danoTotal
                print(f'{self.nome} causou {danoTotal} de dano em {alvo.nome}')
            else:
                print(f'D20: {self.d20}')
                print(f'{self.nome} ERROU')
            



class Monstro:
    def __init__(self, nome, vida, forca, pro, ca,  inteligencia, sabedoria):
        self.nome = nome
        self.vida = vida
        self.vidaMax = vida
        self.forca = forca
        self.pro = pro
        self.ca = ca
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.vivo = True
        self.classe = 'Monstro'
        self.iniciativa = random.randint(1,20)
    def atacar(self, alvo):
        self.d20 = random.randint(1, 20)
        self.dano = random.randint(1, 8)
        danoTotal = self.dano + self.forca + self.pro
        if (self.d20 == 20):
            print(f'D20: {self.d20}')
            alvo.vida -= danoTotal*2
            print(f'{self.nome} causou {danoTotal *2} de dano em {alvo.nome}')
        else:
            if ((self.d20 + self.forca + self.pro) >= alvo.ca):
                print(f'D20: {self.d20}')
                alvo.vida -= danoTotal
                print(f'{self.nome} causou {danoTotal} de dano em {alvo.nome}')
            else:
                print(f'D20: {self.d20}')
                print(f'{self.nome} ERROU')
            


class Clerigo :
    def __init__(self, nome, vida, forca, pro, ca, inteligencia, sabedoria):
        self.nome = nome
        self.vida = vida
        self.vidaMax = vida
        self.forca = forca
        self.pro = pro
        self.ca = ca
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.vivo = True
        self.classe = 'Clerigo'
        self.iniciativa = random.randint(1,20)

    def atacar(self, alvo):
        self.d20 = random.randint(1, 20)
        self.dano = random.randint(1, 8)
        danoTotal = self.dano + self.forca + self.pro
        if (self.d20 == 20):
            print(f'D20: {self.d20}')
            alvo.vida -= danoTotal*2
            print(f'{self.nome} causou {danoTotal *2} de dano em {alvo.nome}')
        else:
            if ((self.d20 + self.forca + self.pro) >= alvo.ca):
                print(f'D20: {self.d20}')
                alvo.vida -= danoTotal
                print(f'{self.nome} causou {danoTotal} de dano em {alvo.nome}')
            else:
                print(f'D20: {self.d20}')
                print(f'{self.nome} ERROU')
    def curar(self, alvo):
        dCura = random.randint(1, 10)
        curaTotal = dCura + self.pro + self.sabedoria
        alvo.vida += curaTotal
        if alvo.vidaMax < alvo.vida+curaTotal:
            alvo.vida = alvo.vidaMax
        print(f'{self.nome} curou {curaTotal} pontos de vida de {alvo.nome}')

