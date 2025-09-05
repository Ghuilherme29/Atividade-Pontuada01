import os
os.system

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo:")
Estado_Civil = input("Digite seu estado civil:")

if sexo == "F" and Estado_Civil == "CASADA":
    print(f"{nome} é casada.")
else:
    print(f"{nome} não é casada.")
