'''
Classe Bola: Crie uma classe que modele uma bola:

    Atributos: Cor, circunferência, material
    Métodos: trocaCor e mostraCor 
'''
class Bola(object):
    def __init__(self, cor:str, circ:float, material:str):
        self.cor = cor
        self.circ = circ
        self.material = material
        
    def troca_cor(self, cor:str):
        self.cor = cor
        
    def mostra_cor(self):
        return self.cor
    
obj = Bola("azul", 3.5, "metal")
obj.troca_cor("verde")
obj.mostra_cor()
