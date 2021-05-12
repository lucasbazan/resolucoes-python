'''
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
'''
def converter_f(f):
  c = 5 * ((f - 32) / 9)
  print(f"{f}F => {c:.1f}C")

F = float(input("Insira os graus Fahrenheit: "))

converter_f(F)
