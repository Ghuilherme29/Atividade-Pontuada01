import os
os.system

Morango_kg = float(input("Digite o peso de morango (em kg): "))
maca_kg = float(input("Digite o peso de maçã (em kg): "))

if Morango_kg <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

if maca_kg <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

total_morango = Morango_kg * preco_morango
total_maca = maca_kg * preco_maca
total_kg = Morango_kg + maca_kg
total_compra = total_morango + total_maca

if total_kg > 10 or total_compra > 15:
    total_compra *= 0.1

print(f"O total da compra é: R$ {total_compra:.2f}")  