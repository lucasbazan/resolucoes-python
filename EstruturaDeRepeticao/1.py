'''
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e 
continue pedindo até que o usuário informe um valor válido. 
'''
while True:
  nota = float(input("Insira uma nota (0-10): "))
  if nota >= 0 and nota <= 10:
    print("Nota registrada com sucesso!")
    break
  else:
    print("Valor invalido!")
