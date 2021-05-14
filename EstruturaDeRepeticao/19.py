#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000. 
valores = []
qnt = int(input("Quantos valores voce quer inserir? "))

for i in range(1, qnt + 1):
  v = int(input(f"Insira o valor {i}: "))
  if v >= 0 and v <= 1000:
    valores.append(v)
  else:
    print("Serao registrados somente valores entre 0 e 1000!")

print("O menor valor equivale a", min(valores))
print("O maior valor equivale a", max(valores))
print("A soma dos valores equivale a", sum(valores))
