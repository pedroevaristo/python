segment_1 = int(input())
segment_2 = int(input())
segment_3 = int(input())
calculation = 0
#tenho que separar o maior numero do resto para que no fim, a soma seja maior ou igual ao ultimo numero

#tenho duvida nessa questão na parte de elif, pois não funciona. Parece que ele passa direto da condição
if segment_1 < segment_2 and segment_1 < segment_3:
    print('o primeiro numero é o menor dos três')

elif segment_2 > segment_1 and segment_2 > segment_3:
    print('o segundo numero é maior que o resto')
    calculation = segment_3

elif segment_3 > segment_2 and segment_3 > segment_1:
    print('o terceiro numero é o maior que o resto')
    calculation = segment_2

totalCalculation = segment_1 + calculation

print('A soma dos dois menores numeros:')
print(f'{segment_1} + {calculation} = {totalCalculation}')
print(f'verificação: {totalCalculation} > {calculation}')

if totalCalculation > calculation:
    print('Conclusão: estes segmentos formam um triângulo')
else:
    print('Conclusão: estes segmentos não formam um triângulo')


print(segment_1)
print(segment_2)
print(segment_3)


# voltar para fazer ordenação de numeros
#
# if segment_1 < segment_2 and segment_3:
#
#     if segment_2 > segment_3:
#         aux = segment_2
#         segment_2 = segment_3
#         segment_3 = aux
#
#
# elif segment_2 > segment_1 and segment_3:
#
#     if segment_2 > segment_3:
#
#         aux = segment_2
#         segment_2 = segment_3
#         segment_3 = aux
#
#     elif segment_1 > segment_2:
#         aux = segment_1
#         segment_1 = segment_2
#         segment_2 = aux
#
#
# elif segment_3 > segment_2 and segment_1:
#
#     if segment_1 > segment_2:
#         aux = segment_1
#         segment_1 = segment_2
#         segment_2 = aux
