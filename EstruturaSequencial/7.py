#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. 
def calcular_area(l):
  area = l ** 2
  print(f"O dobro da area equivale a {area * 2:.1f}")

lado = float(input("Insira um dos lados do quadrado: "))

calcular_area(lado)
