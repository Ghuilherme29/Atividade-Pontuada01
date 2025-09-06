import os
os.system

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

if a == b:
    print(f"O valor de a ({a}) é igual ao valor de b ({b}).")
    c = a + b
    print(f"A soma de a + b é: {c}.")
else:
    print(f"O valor de a ({a}) é diferente do valor de b ({b}).")
    c = a * b
    print(f"A multiplicação de a * b é: {c}.")