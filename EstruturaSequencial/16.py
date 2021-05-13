'''
Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e 
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas 
e o preço total. 
'''
def calcular_latas(m):
  litros = round(m / 3)
  latas = round(litros / 18)
  valor_latas = latas * 80

  print(f"Devera utilizar {latas} latas")
  print(f"O valor total equivale a R${valor_latas:.2f}")

area = float(input("Insira a metragem quadrada da area a ser pintada: "))

calcular_latas(area)
