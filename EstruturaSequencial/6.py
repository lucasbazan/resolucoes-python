#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. 
from math import pi

def calcular_area(r):
  area = pi * (r ** 2)
  print(f"A area equivale a {area:.2f} metros")

raio = float(input("Insira o raio do circulo: "))

calcular_area(raio)
