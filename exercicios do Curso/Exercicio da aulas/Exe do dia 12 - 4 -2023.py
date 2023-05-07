# Faça um programa que peça verifica se o usuário digitou um número inteiro.
# Caso tenha digitado, mostrar o número na tela.
# Caso não tenha digitado, pedir para o usuário digitar novamente.

while True:
    verifyInput = input()
    if verifyInput.isdigit():
        print('É um numero')
        break
    else:
        print('Não é um numero')
        break