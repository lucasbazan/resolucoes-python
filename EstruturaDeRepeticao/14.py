'''
Faça um programa que peça 10 números inteiros, 
calcule e mostre a quantidade de números pares e a 
quantidade de números impares. 
'''
numeros_pares = []
numeros_impares = []

for i in range(1, 11):
  n = int(input(f"Insira o valor {i}: "))
  
  if n % 2 == 0:
    numeros_pares.append(n)
  else:
    numeros_impares.append(n)

print(f"Foram inseridos {len(numeros_pares)} numeros pares")
print(f"Foram inseridos {len(numeros_impares)} numeros impares")
