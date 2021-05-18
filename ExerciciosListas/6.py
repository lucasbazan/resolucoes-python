'''
Faça um Programa que peça as quatro notas de 10 alunos, 
calcule e armazene num vetor a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0. 
'''
medias = []
notas = []
maior = []

for i in range(1, 11):
  for x in range(1, 5):
    nota = float(input(f"Insira a nota {x} do aluno {i}: "))
    notas.append(nota)
    if len(notas) == 4:
      media = sum(notas) / len(notas)
      medias.append(media)
      notas.clear()
    else:
      pass

for m in medias:
  if m >= 7:
    maior.append(m)

print(f"Possuem {len(maior)} alunos com media maior ou igual a 7")
