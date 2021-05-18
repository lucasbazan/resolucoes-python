'''
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
Imprima os três vetores. 
'''
numeros = []
par = []
impar = []

for i in range(1, 21):
  n = int(input(f"Insira o valor {i}: "))
  numeros.append(n)
  if n % 2 == 0:
    par.append(n)
  else:
    impar.append(n)

print(f"Numeros inseridos: {numeros}")
print(f"Numeros pares: {par}")
print(f"Numeros impares: {impar}")
