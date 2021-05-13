'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e 
a velocidade de um link de Internet (em Mbps), calcule e informe o 
tempo aproximado de download do arquivo usando este link (em minutos). 
'''
def calcular_download(mb, mbps):
  tempo = mb / (mbps / 8) / 60
  print(f"O tempo aproximado de download equivale a {int(tempo)} minuto(s)")

tamanho = float(input("Insira o tamanho do arquivo em MB: "))
velocidade = float(input("Insira a velocidade da internet em Mbps: "))

calcular_download(tamanho, velocidade)
