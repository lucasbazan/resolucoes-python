'''
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. 
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas. 
'''    
class Televisao(object):
    def __init__(self, canal, volume=50):
        self.canal = canal
        self.volume = volume
        if self.canal < 0 or self.canal > 12:
            print("Canal Invalido!")
        elif self.volume < 0 or self.volume > 100:
            print("Apenas volume 0-100% permitido!")
        else:
            pass
    
    def aumentar(self, volume):
        self.volume += volume
        if self.canal < 0 or self.canal > 12:
            print("Canal Invalido!")
        elif self.volume < 0 or self.volume > 100:
            print("Apenas volume 0-100% permitido!")
        else:
            pass
        
    def diminuir(self, volume):
        self.volume -= volume
        if self.canal < 0 or self.canal > 12:
            print("Canal Invalido!")
        elif self.volume < 0 or self.volume > 100:
            print("Apenas volume 0-100% permitido!")
        else:
            pass

obj = Televisao(12, 80)
