'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, 
o maior valor e a soma dos valores. 
'''
valores = []
qnt = int(input("Quantos valores voce quer inserir? "))

for i in range(1, qnt + 1):
  v = int(input(f"Insira o valor {i}: "))
  valores.append(v)

print("O menor valor equivale a", min(valores))
print("O maior valor equivale a", max(valores))
print("A soma dos valores equivale a", sum(valores))
