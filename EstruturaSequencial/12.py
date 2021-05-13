'''
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: (72.7*altura) - 58
'''
def calcular_peso(h):
  peso = (72.7 * h) - 58
  print(f"Seu peso ideal equivale a {peso:.1f}kg")

altura = float(input("Insira sua altura em metro: "))

calcular_peso(altura)
