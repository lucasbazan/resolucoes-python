'''
Faça um Programa que leia um vetor de 10 caracteres, 
e diga quantas consoantes foram lidas. Imprima as consoantes. 
'''
conso = []
vetor = input("Insira um vetor: ")

for v in vetor:
  if v != "A" and v != "a" and v != "E" and v != "e" and v != "I" and v != "i" and v != "O" and v != "o" and v != "U" and v != "u":
    conso.append(v)

print(f"A palavra {vetor} possui {len(conso)} consoantes")
print(f"Consoantes da palavra {vetor}: {conso}")
