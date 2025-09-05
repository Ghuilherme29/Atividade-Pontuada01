import os
os.system("cls")

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))


soma_ab = A + B


if soma_ab < C:
    print(f"A soma de A + B ({soma_ab}) é menor que C ({C}).")
else:
    print(f"A soma de A + B ({soma_ab}) é maior que C ({C}).")
