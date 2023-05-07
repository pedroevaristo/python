import math

weight = float(input('digite seu peso: '))#fazer uma verificação de casa depois da decimal

gender = (input('digite seu sexo:'))
while gender != 'm' or gender != 'f' or gender != 'w':
    print('Digite novamente, que não seja em numero inteiro')
    gender = (input('digite seu sexo:'))
    if gender == 'm' or gender == 'f' or gender == 'w':
        break


if gender == 'm':

    height = float(input('digite sua altura: '))

    weightIdeal = (72.7 * height) - 50

    totalIMC = weight / math.pow(height, 2)

if gender == 'w' or gender == 'f':

    height = float(input('digite sua altura: '))

    weightIdeal = (62.1 * height) - 44.7

    totalIMC = weight / math.pow(height, 2)


differenceBetweenWeights = weightIdeal - weight

if totalIMC < 18.5:
    print(f'Seu IMC: {totalIMC:.2f}')
    print('Vá ao profissional da saúde mais próximo,'
          ' pode lhe custar maior dificuldade na sua vida\n')


if totalIMC >= 18.5 and totalIMC <= 24.9:
    print(f'Seu IMC: {totalIMC:.2f}')
    print('Parabéns por manter até aqui, agora a meta é ficar na maiorira das vezes constante nesse nível\n')

if totalIMC >= 25 and totalIMC <= 29.9:

   print(f'Sobrepeso: {totalIMC:.2f} IMC')

   print('Não sei o motivo de você estar assim,'
          ' mas se quiser mudança na sua vida vai ser uma longa jornada,'
          ' mas terá seus frutos recolhidos merecido\n')


print(f'Your weight goal: {abs(weightIdeal):.2f} KG')

print(f'This is difference between your actual weight and your goal: {abs(differenceBetweenWeights):.2f}')