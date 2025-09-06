import os
os.system("cls")

operacao = int(input("Escolha a operação (1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão): "))
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

match operacao:
    case 1:
        resultado = a + b
        print(f"A soma de {a} + {b} é: {resultado}.")
    case 2:
        resultado = a - b
        print(f"A subtração de {a} - {b} é: {resultado}.")
    case 3:
        resultado = a * b
        print(f"A multiplicação de {a} * {b} é: {resultado}.")
    case 4:
        if b != 0:
            resultado = a / b
            print(f"A divisão de {a} / {b} é: {resultado}.")
       
    