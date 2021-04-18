'''
  Classe Retangulo: Crie uma classe que modele um retangulo:
  Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
  Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
  Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
  Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
'''
class Retangulo:
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura
  
  def mudarLados(self):
    self.base = int(input('Insira o comprimento do local: '))
    self.altura = int(input('Insira a largura do local: '))

  def retornarLados(self):
    print('O comprimento é igual à {} e a largura é igual à {}'.format(self.base, self.altura))
  
  def calcularArea(self):
    area = self.base * self.altura
    self.area = area
  
  def calcularPerimetro(self):
    perim = (self.base * 2) + (self.altura * 2)
    self.perim = perim

  def calcularPiso(self):
    piso = float(input('Qual a medida do piso em metros (ex: 0.45): '))
    piso = piso ** 2
    calc_piso = (self.area / piso) + (self.area / piso) * 0.10
    print('Serão necessários {} pisos'.format(int(calc_piso)))

  def calcularRodape(self):
    porta = float(input('Insira a largura da porta em metros (ex: 2): '))
    rodape = self.perim - porta
    print('Serão necessários {} metros de rodapé'.format(int(rodape)))

def main():
  retangulo = Retangulo(0, 0)

  while True:
    retangulo.retornarLados()
    retangulo.mudarLados()

    retangulo.calcularArea()
    retangulo.calcularPerimetro()
    
    retangulo.calcularPiso()
    retangulo.calcularRodape()

main()
