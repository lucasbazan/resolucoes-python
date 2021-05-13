'''
Faça um programa que leia um nome de usuário e a sua senha e 
não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.  
'''
while True:
  usuario = input("Insira o nome de usuario: ")
  senha = input("Insira uma senha: ")
  if usuario == senha:
    print("O nome de usuario nao pode ser igual a senha!")
  else:
    print("Usuario cadastrado com sucesso!")
    break
