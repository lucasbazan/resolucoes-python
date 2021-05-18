'''
Faça um programa que peça um número inteiro e determine se ele é 
ou não um número primo. Um número primo é aquele que é 
divisível somente por ele mesmo e por 1. 
'''
n = int(input("Verificar numeros primos ate: "))
m = 0

for i in range(2, n):
    if n % i == 0:
        print("Multiplo de", i)
        m += 1

if m == 0:
    print(f"{n} equivale a um primo")
else:
    print(f"Tem {m} multiplos acima de 2 e abaixo de {n}")
