'''
Faça um programa que peça dois números, base e expoente, 
calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem. 
'''
base = int(input("Insira a base: "))
exp = int(input("Insira o expoente: "))
pot = 1

for i in range(1, exp + 1):
  pot *= base

print(f"{base} elevado a {exp} equivale a {pot}")
