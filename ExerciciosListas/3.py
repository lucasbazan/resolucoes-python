#Faça um Programa que leia 4 notas, mostre as notas e a média na tela. 
notas = []
x = 0

for i in range(1, 5):
  nota = float(input(f"Insira a nota {i}: "))
  notas.append(nota)
for n in notas:
  x += 1
  print(f"Nota {x}: {n}")
print(f"A media equivale a {sum(notas) / len(notas)}")
