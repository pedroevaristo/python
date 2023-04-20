#fazer um dicionario
sumOfTheEmployers = 0
sells = {
    "1": 100,
    "2": 150,
    "3": 1500,
    "4": 2000,
    "5": 120,
}

for loop in sells.items():
   convertToInt = (int(loop[1]))
   if convertToInt >= 1000:
    sumOfTheEmployers += 1
    totalCalculate = convertToInt * 15 /100
    print(f'Empregado {loop[0]} vendas no mês: {convertToInt}')
    print(f'Com bonus de 15 por cento: {totalCalculate}\n')

print(f'Esses {sumOfTheEmployers} vão receber o bonus de 15 por cento por ter batido a meta')