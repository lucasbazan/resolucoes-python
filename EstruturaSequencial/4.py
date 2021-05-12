#Faça um Programa que peça as 4 notas bimestrais e mostre a média. 
notas = []

for i in range (1, 5):
  nota = float(input(f"Insira a nota do bimestre {i}: "))
  notas.append(nota)

media = (notas[0] + notas[1] + notas[2] + notas[3]) / 4
print(f"A media equivale a {media:.1f}")
