import os
os.system("cls")

renda = float(input("Digite sua renda mensal: R$ "))
valor_emprestimo = float(input("Digite o valor do empréstimo solicitado: "))
num_prestacoes = int(input("Digite o número de prestações desejado: "))

prestacao = valor_emprestimo / num_prestacoes

if valor_emprestimo <= renda * 10 and prestacao <= renda * 0.3:
    print("Empréstimo pode ser concedido.")
else:
    print("Empréstimo NÃO pode ser concedido.")