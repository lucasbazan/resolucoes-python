'''
Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e 
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou 
em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e 
    os respectivos preços em 3 situações:
      comprar apenas latas de 18 litros;
      comprar apenas galões de 3,6 litros;
      misturar latas e galões, de forma que o desperdício de tinta seja menor. 
      Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. 
'''
def calcular_tinta(m):
  litros = m / 6
  litros = litros + litros * 0.10
  latas = litros / 18
  galoes = litros / 3.6

  if latas % 18 != 0:
    latas += 1
  
  elif galoes % 18 != 0:
    galoes += 1

  latas = round(latas)
  galoes = round(galoes)
  valor_latas = latas * 80
  valor_galoes = galoes * 25

  if valor_latas > valor_galoes:
    print(f"Comprar apenas {galoes} galoes de 3,6 litros por R${valor_galoes:.2f}")
  else:
    print(f"Comprar apenas {latas} latas de 18 litros por R${valor_latas:.2f}")

area = float(input("Insira a metragem quadrada da area a ser pintada: "))

calcular_tinta(area)
