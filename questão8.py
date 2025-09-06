import os
os.system


precos = {
    'VERDE': 10.00,
    'AZUL': 20.00,
    'AMARELO': 30.00,
    'VERMELHO': 40.00
}

cor = input("Digite a cor dos CDs (VERDE, AZUL, AMARELO, VERMELHO): ").upper()


if cor in precos:
    preco_selecionado = precos[cor]
    print(f"O preço do CD da cor {cor} é: R$ {preco_selecionado:.2f}")
else:
   
    print("Cor inválida. Por favor, escolha entre VERDE, AZUL, AMARELO ou VERMELHO.")