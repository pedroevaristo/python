segment_1 = int(input())
segment_2 = int(input())
segment_3 = int(input())

maior = 0
resultCalculation = 0

if segment_1 > segment_2 and segment_1 > segment_3:
    maior = segment_1
    resultCalculation = segment_2 + segment_3

elif segment_2 > segment_1 and segment_2 > segment_3:
    maior = segment_2
    resultCalculation = segment_1 + segment_3

elif segment_3 > segment_1 and segment_3 > segment_2:
    maior = segment_3
    resultCalculation = segment_1 + segment_2

if maior > resultCalculation:
    print('É triangulo')
else:
    print('Não é triangulo')
