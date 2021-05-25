'''
Classe Retangulo: Crie uma classe que modele um retangulo:

    Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
    Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
    Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
    Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de 
    rodapés necessárias para o local. 
'''
class Retangulo(object):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def muda_lados(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcula_area(self):
        return self.base * self.altura
    
    def calcula_perimetro(self):
        return self.base ** 2 + self.altura ** 2
    
    def calcula_piso(self, piso):
        self.piso = piso
        return Retangulo(self.base, self.altura).calcula_area()/piso
    
base = float(input("Insira a base: "))
altura = float(input("Insira a altura: "))
piso = int(input("Insira o tamanho do piso (cm quadrados): "))

obj = Retangulo(base, altura)
print(f"{int(obj.calcula_piso(piso))} piso(s) de {piso} centimetros quadrados")
