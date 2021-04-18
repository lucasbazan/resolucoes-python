# Classe Quadrado: Crie uma classe que modele um quadrado:
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
  def __init__(self, lado=0):
    self.lado = lado
  
  def mudarLado(self):
    self.lado = int(input('Insira o o valor do lado: '))
  
  def retornarLado(self):
    print('O lado é igual à {}'.format(self.lado))

  def calcularArea(self):
    area = self.lado ** 2
    print('A área é igual à {}'.format(area))

def main():
  quadrado = Quadrado(0)
  
  while True:
    quadrado.retornarLado()
    
    escolha = input('Deseja alterar o lado? [s/n]: ') 
    escolha = escolha[0].lower()

    if escolha == 's':
      quadrado.mudarLado()
      quadrado.calcularArea()
    else:
      pass
 
main()
