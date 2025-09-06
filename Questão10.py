import os
os.system("cls")


litros = float(input("Digite o número de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()

if tipo == "A":
    preco_litro = 3.79
    if litros <= 25:
        desconto = 0.10
    else:
        desconto = 0.20
elif tipo == "G":
    preco_litro = 6.59
    if litros <= 25:
        desconto = 0.15
    else:
        desconto = 0.30
else:
    print("Tipo de combustível inválido.")
    

valor_bruto = litros * preco_litro
valor_bruto = litros * preco_litro
valor_desconto = valor_bruto * desconto
valor_final = valor_bruto - valor_desconto

print(f"Valor a pagar: R$ {valor_final:.2f}")