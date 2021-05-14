'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo. 
Numero seguinte = soma dos dois numeros anteriores
'''
fibonacci = [1,1]

n = int(input("Insira um numero: "))

while len(fibonacci) < n:
  fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(f"O numero Fibonacci de {n} equivale a {fibonacci[-1]}\nSerie Fibonacci => {fibonacci}")
