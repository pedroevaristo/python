import random
value = random.randint(1,52)
# value = int(input())

print(f'valor digitado: {value}')

print('\n Qual é a sua escollhe: \n g - Gasolina \n a - Álcool')
choice = input()

if choice =='g':# gasolina
    value *= 5
    if value <= 20:
        totalDiscount = value * 4 / 100
        totalValue = value - totalDiscount

    elif value > 20:
        totalDiscount = value * 6 / 100
        totalValue = value - totalDiscount


if choice == 'a':
    value *= 4

    if value <= 20:
        totalDiscount = value * 3 / 100
        totalValue = value - totalDiscount

    elif value > 20:
        totalDiscount = value * 5 / 100
        totalValue = value - totalDiscount


print(f'valor total do combustivel: {totalValue}')#NameError: name 'totalValue' is not defined
