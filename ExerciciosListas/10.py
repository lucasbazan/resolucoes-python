'''
Faça um Programa que leia dois vetores com 10 elementos cada. 
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser 
compostos pelos elementos intercalados dos dois outros vetores. 
'''
A = []
B = []
C = []

for x in range(1, 11):
  V_A = float(input(f"Insira o valor {x} para o Vetor A: "))
  A.append(V_A)

for y in range(1, 11):
  V_B = float(input(f"Insira o valor {y} para o Vetor B: "))
  B.append(V_B)

for z in range(0, 10):
  C.append(A[z])
  C.append(B[z])

print(f"Os elementos do Vetor C compoem {C}")
