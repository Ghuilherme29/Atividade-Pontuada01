import os
os.system('cls')


print('''
  Bem-vindo a loja de CDs!
  Temos as seguintes opções de cores para os CDs:
          
    |   cor    |   preço 
    |  Verde   |  R$ 10,00 
    |  Azul    |  R$ 20,00
    |  Amarelo |  R$ 30,00
    |  Vermelho|  R$ 40,00 \n''')

cor = input('Escolha a cor dos CDs desejada:').upper()

  
match cor:
    case "VERDE":
        print('Você escolheu a cor (verde:), o preço é R$ 10,00')
    case "AZUL":
        print('Você escolheu a cor azul, o preço é R$ 20,00')
    case "AMARELO":
        print('Você escolheu a cor amarelo, o preço é R$ 30,00')
    case "VERMELHO":
        print('Você escolheu a cor vermelho, o preço é R$ 40,00')
    case _:
        print('Opção inválida, tente novamente!')
