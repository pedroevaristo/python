
print('How many oranges would like to have ?')
quantityOrange = int(input())

if quantityOrange > 12:
    total = float(quantityOrange * 0.25)
    print(f'the price total is: {total:.2f} with {quantityOrange} ')
else:
    total = float(quantityOrange * 0.30)
    print(f'the price total is: {total:.2f} with {quantityOrange} ')


