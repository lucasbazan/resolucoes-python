'''
Tendo como dado de entrada a altura (h) de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, 
utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7 
'''
def calcular_peso_m(h):
  peso = (72.7 * h) - 58
  print(f"Seu peso ideal equivale a {peso:.1f}kg")

def calcular_peso_f(h):
  peso = (62.1 * h) - 44.7
  print(f"Seu peso ideal equivale a {peso:.1f}kg")

sexo = input("Insira o seu sexo [m / f]: ")
altura = float(input("Insira sua altura em metro: "))

if sexo == "m" or sexo == "M":
  calcular_peso_m(altura)
elif sexo == "f" or sexo == "F":
  calcular_peso_f(altura)
else:
  print("Sexo invalido!")
