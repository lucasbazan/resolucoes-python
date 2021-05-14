#Altere o programa anterior para mostrar no final a soma dos números. 
numeros = []

n1 = int(input("Insira o valor 1: "))
n2 = int(input("Insira o valor 2: "))

for i in range(n1 + 1, n2):
  numeros.append(i)

print(f"A soma do intervalo dos valores {n1} e {n2} equivale a {sum(numeros)}")
