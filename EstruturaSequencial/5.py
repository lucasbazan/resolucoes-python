#Faça um Programa que converta metros para centímetros. 
def converterMTemCM(metros):
  cm = metros * 100
  print(f"O valor de {metros} equivale a {cm:.0f} centimetros")

m = float(input("Insira o valor em metros: "))

converterMTemCM(m)
