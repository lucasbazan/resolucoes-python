#Faça um programa que leia 5 números e informe o maior número. 
numeros = []

for i in range(1, 6):
  n = float(input(f"Insira o valor {i}: "))
  numeros.append(n)

print(round(max(numeros)))
