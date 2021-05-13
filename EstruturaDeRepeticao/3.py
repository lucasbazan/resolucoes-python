'''
Faça um programa que leia e valide as seguintes informações:

    a. Nome: maior que 3 caracteres;
    b. Idade: entre 0 e 150;
    c. Salário: maior que zero;
    d. Sexo: 'f' ou 'm';
    e. Estado Civil: 's', 'c', 'v', 'd'; 
'''
while True:
  a = input("Insira o nome: ")  
  b = int(input("Insira a idade: "))
  c = float(input("Insira seu salario: "))
  d = input("Insira seu sexo [f / m]: ")
  e = input("Estado Civil [s, c, v, d]: ")

  if b < 0 or b > 150 or c <= 0 or d != "f" and d != "m" or e != "s" and e != "c" and e != "v" and e != "d":
    print("Algum dado inserido esta invalido!")
  else:
    print("Cadastro efetuado com sucesso!")
