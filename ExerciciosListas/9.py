'''
Faça um Programa que leia um vetor A com 10 números inteiros, 
calcule e mostre a soma dos quadrados dos elementos do vetor.
'''
A = []
Q = []

for i in range(1, 11):
  n = int(input(f"Insira o valor {i}: "))
  A.append(n)

for x in range(0, 10):
  Q.append(A[x] ** 2)

print(f"A soma dos quandrados equivale a {sum(Q)}")
