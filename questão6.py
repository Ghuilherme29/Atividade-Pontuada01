import os
os.system

nota1 = float(input("Digite sua nota1:"))
nota2 = float(input("Digite sua nota2:"))


soma = nota1 + nota2
media = soma / 2

if media >= 6:
    print(f"Aluno aprovado com média {media}.")


if media <= 5.9 and media >= 4.1:
    print(f"Aluno em recuperação com média {media}.")
else:
    print(f"Aluno reprovado com média {media}.")       