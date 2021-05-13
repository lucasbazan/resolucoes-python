'''
Altere o programa anterior permitindo ao usuário informar as populações e 
as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.  
'''
a = int(input("Insira a populacao A: "))
cresc_a = float(input("Insira a taxa de crescimento em porcentagem da populacao A: "))
b = int(input("Insira a populacao B: "))
cresc_b = float(input("Insira a taxa de crescimento em porcentagem da populacao B: "))
anos = 0

while a < b:
  a += (cresc_a * a) / 100
  b += (cresc_b * b) / 100
  anos += 1
else:
  print(f"Seriam necessarios {anos} anos para a populacao A se igualar ou ultrapassar a B")
  print(f"Populacao A => {int(a)} habitantes")
  print(f"Populacao B => {int(b)} habitantes")
