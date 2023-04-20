# Faça um programa de verificação de login e senha.
# O usuário pode errar a senha até 3 vezes antes do programa terminar informando que o acesso foi bloqueado.

senha = ['15-e']
verifyBlock = 1
login = input('Digite seu login:')
password = input('Digite a senha: ')

while True:
    if password != senha[0]:
        input(f'Tem {verifyBlock} de 3 chances para não ser bloqueado.\nPor favor digite novamente:')
        verifyBlock += 1
        if verifyBlock == 3:
            print('Conta bloqueado, crie uma nova senha')
            exit()
    else:
        print('Está logado na conta. Entrando ...')
        break
