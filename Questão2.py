import os
os.system

nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F): ").upper()
estado_civil = input("Digite o estado civil: ").upper()

tempo_casada = None
if sexo == "F" and estado_civil == "Casada":
    tempo_casada = input("Digite o tempo de casada (em anos): ")

print("\nDados do usuário:")
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado civil: {estado_civil}")
if tempo_casada:
    print(f"Tempo de casada: {tempo_casada} anos")