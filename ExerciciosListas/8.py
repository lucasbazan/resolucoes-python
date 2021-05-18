'''
Faça um Programa que peça a idade e a altura de 5 pessoas, 
armazene cada informação no seu respectivo vetor. Imprima a idade e a 
altura na ordem inversa a ordem lida. 
'''
idades = []
alturas = []

for i in range(1, 6):
  idade = int(input(f"Insira a idade da pessoa {i}: "))
  idades.append(idade)
  altura = float(input(f"Insira a altura da pessoa {i}: "))
  alturas.append(altura)

print("--- ORDEM INVERSA ---")
print("Idades =>", idades[::-1])
print("Alturas =>", alturas[::-1])

print("\n--- ORDEM LIDA ---")
print("Idades =>", idades)
print("Alturas =>", alturas)
