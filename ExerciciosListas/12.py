'''
Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais de 13 anos 
possuem altura inferior à média de altura desses alunos. 
'''
idades = []
alturas = []
anos13 = []
alt_inf = []

for i in range(1, 31):
  idade = int(input(f"Insira a idade do aluno {i}: "))
  idades.append(idade)
  
  if idade > 13:
    anos13.append(idade)

  altura = float(input(f"Insira a altura do aluno {i}: "))
  alturas.append(altura)

media = sum(alturas) / len(alturas)

for a in alturas:
  if a < media:
    alt_inf.append(a)
  else:
    pass

print(f"Possuem {len(alt_inf)} aluno(s) de 13 anos com altura menor do que a media")
