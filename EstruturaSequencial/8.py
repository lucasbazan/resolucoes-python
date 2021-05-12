'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês. 
'''
def calcular_salario(ph, ht):
  salario = ph * ht
  print(f"Seu salario equivale a R${salario:.2f}")

por_hora = float(input("Insira quanto voce ganha por hora: "))
horas_trabalhadas = int(input("Insira quantas horas voce trabalhou: "))

calcular_salario(por_hora, horas_trabalhadas)
