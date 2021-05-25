'''
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

    Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; 
    Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, 
    o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, 
    um campo calculado, então não devemos criar um atributo para armazenar esta informação 
    por que ela pode ser calculada a qualquer momento. 
'''    
class Tamagushi(object):
    def __init__(self, nome, fome=False, saude=100, idade=0, humor=["Irritado", "Feliz"]):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.humor = humor
    
    def retorna_nome(self):
        return self.nome
    
    def retorna_fome(self):
        if self.fome == True:
            print(f"{self.nome} esta com fome!")
        else:
            print(f"{self.nome} nao esta com fome!")
    
    def retorna_saude(self):
        return self.saude
    
    def envelhece(self, idade):
        self.idade += idade
        self.saude -= 10
    
    def retorna_idade(self):
        return self.idade
    
    def retorna_humor(self):
        if self.fome == True and self.saude < 50:
            self.humor = self.humor[0]
            return self.humor
        else:
            self.humor = self.humor[1]
            return self.humor
            
obj = Tamagushi("Scooby", True, 40)
