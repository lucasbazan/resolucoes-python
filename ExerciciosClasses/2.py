'''
Classe Quadrado: Crie uma classe que modele um quadrado:

    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área; 
'''
class Quadrado(object):
    def __init__(self, lado:float):
        self.lado = lado
    
    def retorna_lado(self):
        return self.lado
    
    def calcula_area(self):
        return self.lado ** 2
    
obj = Quadrado(2)
obj.retorna_lado()
obj.calcula_area()
