#Faça um programa que leia 5 números e informe a soma e a média dos números. 
numeros = []

for i in range(1, 6):
  n = float(input(f"Insira o valor {i}: "))
  numeros.append(n)

soma = sum(numeros)
media = soma / len(numeros)

print(f"A soma dos numeros equivale a {soma}")
print(f"A media aritmetica dos numeros equivale a {media}")
