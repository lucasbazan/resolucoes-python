'''
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o 
fatorial várias vezes e limitando o fatorial a 
números inteiros positivos e menores que 16. 
'''
def fatorial(n):
  _n = n
  i = n
  while i > 1:
    i -= 1
    n = n * i
  print(f"{_n}!={n}")

while True:
  f = int(input("Insira um valor positivo e menor que 16: "))
  if f < 16 and f > 0:
    fatorial(f)
  else:
    print("Valor invalido!")
