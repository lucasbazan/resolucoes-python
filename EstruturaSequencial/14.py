'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador 
para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o 
estabelecido pelo regulamento de pesca do estado de São Paulo 
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a 
variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite 
e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.
'''
def calcular_excesso(p_p):
  multa = p_p * 4
  print(f"Voce tera que pagar uma multa de R${multa:.2f}\nPois o peso {p_p}kg excedeu o limite de 50kg")

peso_peixe = float(input("Insira o peso do(s) peixe(s) em kilogramas: "))

if peso_peixe > 50:
  calcular_excesso(peso_peixe)
else:
  print(f"Nao precisara pagar multa\nPois o peso de {peso_peixe}kg nao excedeu o limite de 50kg")
