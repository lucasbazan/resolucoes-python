'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
  a) o produto do dobro do primeiro com metade do segundo .
  b) a soma do triplo do primeiro com o terceiro.
  c) o terceiro elevado ao cubo. 
'''
numeros = []

def calcular(n1, n2, n3):
  a = (n1 * 2) * (n2 / 2)
  b = n1 * 3 + n3
  c = n3 ** 3
  print(f"O produto do dobro do primeiro com metade do segundo => {a:.1f}")
  print(f"A soma do triplo do primeiro com o terceiro => {b:.1f}")
  print(f"O terceiro elevado ao cubo => {c:.1f}")

for i in range(1, 4):
  num = float(input(f"Insira o valor {i}: "))
  numeros.append(num)

calcular(numeros[0], numeros[1], numeros[2])
  
