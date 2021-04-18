'''
  Classe Bola: Crie uma classe que modele uma bola:
  Atributos: Cor, circunferência, material
  Métodos: trocaCor e mostraCor
'''

class Bola:
  def __init__(self, cor='n/a', circ=0, mat='n/a'):
    self.cor = cor # Cor
    self.circ = circ # Circunferência
    self.mat = mat # Material
  
  def trocaCor(self):
    self.cor = input('Para qual cor gostaria de trocar? ')

  def mostraCor(self):
    print('A cor atual é {}'.format(self.cor))

def main():
  bola = Bola('n/a', 0, 'n/a')

  while True:
    bola.mostraCor()

    escolha = input('Você gostaria de mudar a cor? [s/n]: ')
    escolha = escolha[0].lower()

    if escolha == 's':
      bola.trocaCor()
    else:
      pass
 
main()
