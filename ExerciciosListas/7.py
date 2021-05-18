'''
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, 
a multiplicação e os números. 
'''
vetor = []

for i in range(1, 6):
  n = int(input(f"Insira o valor inteiro {i}: "))
  vetor.append(n)

print("A soma dos numeros equivale a", sum(vetor))

print("A multiplicacao dos numeros equivale a", vetor[0] * vetor[1] * vetor[2] * vetor[3] * vetor[4])
print("Os numeros inseridos sao:", vetor)
