'''
Faça um Programa que pergunte quanto você ganha por hora e o 
número de horas trabalhadas no mês. Calcule e 
mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 
5% para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

    Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
def folha_pagamento(p_h, h_t):
  salario_bruto = p_h * h_t
  imposto_renda = salario_bruto * 0.11
  inss = salario_bruto * 0.08
  sindicato = salario_bruto * 0.05
  salario_liquido = salario_bruto - imposto_renda - inss - sindicato

  print(f"+ Salário Bruto : R${salario_bruto:.2f}")
  print(f"\t- IR (11%) : R${imposto_renda:.2f}")
  print(f"\t- INSS (8%) : R${inss:.2f}")
  print(f"\t- Sindicato (5%) : R${sindicato:.2f}")
  print(f"= Salário Liquido : R${salario_liquido:.2f}")

por_hora = float(input("Insira o ganho por hora: "))
horas_trabalhadas = float(input("Insira a quantidade de horas trabalhadas: "))

print("\n-:-: FOLHA DE PAGAMENTO :-:-")
folha_pagamento(por_hora, horas_trabalhadas)
