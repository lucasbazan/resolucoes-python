#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. 
def converter_c(c):
  f = (c * 9 / 5) + 32
  print(f"{c}C => {f:.1f}F")

C = float(input("Insira os graus Celsius: "))

converter_c(C)
