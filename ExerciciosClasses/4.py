'''
Classe Pessoa: Crie uma classe que modele uma pessoa:

    Atributos: nome, idade, peso e altura
    Métodos: Envelhercer, engordar, emagrecer, crescer. 
    Obs: Por padrão, a cada ano que nossa pessoa envelhece, 
    sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm. 
'''
class Pessoa(object):
    def __init__(self, nome:str, idade:int, peso:float, altura:float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def envelhecer(self, idade):
        if self.idade < 21:
            self.altura += 0.5
        self.idade += idade
        return self.idade
    
    def engordar(self, peso):
        self.peso += peso
        return self.peso
        
    def emagrecer(self, peso):
        self.peso -= peso
        return self.peso
        
    def crescer(self, altura):
        self.altura += altura
        return self.altura

lucas = Pessoa("Lucas", 21, 74.4, 1.71)
lucas.envelhecer(1)
lucas.engordar(2)
lucas.emagrecer(1)
lucas.crescer(0.05)
