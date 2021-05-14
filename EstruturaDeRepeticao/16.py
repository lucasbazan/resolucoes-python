'''
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500. 
'''
fibonacci = [1,1]

while True:
  n = int(input("Insira um numero: "))
  if n > 500:
    break
  else:
    print("Insira um numero maior que 500!")

while len(fibonacci) < n:
  fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(f"O numero Fibonacci de {n} equivale a {fibonacci[-1]}\nSerie Fibonacci => {fibonacci}")
