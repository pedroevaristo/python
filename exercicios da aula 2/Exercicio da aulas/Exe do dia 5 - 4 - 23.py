# baseando na seguinte logica com 10 funcionários cada um com seu objetivo individual
#sabendo que, precisa ser um valor de quatro digitos de venda
print("The month's goal is 50.000.")
loop = 0

totalValueSell = 0

while True:
    valueSeller = int(input("Type your quantify sells during of the month: "))

    totalValueSell += valueSeller
    loop += 1
    if loop == 5:#com 5 funcionarios o minimo é fazer 333 vendas por dia
        break




match totalValueSell:
    case totalValueSell if totalValueSell < 49500 :

        print(f"Unfortunately, we don't get the goal this month. The difference is {totalValueSell - 49500}. Nobody going to receive the bonus")

    case totalValueSell if totalValueSell == 49500:

        print(f"We just a little bit to reach.The difference is {totalValueSell - 49500}. Only the winners will get the prize of 5 %")
        totalWithPercent = totalValueSell * 5/ 100
        print(f"Value total with percent: {totalWithPercent}")

    case totalValueSell if totalValueSell == 50000:

        print(f"We achieve our objetive this month. The difference is {totalValueSell - 50000}. Only the winners will get the prize of 10 %")
        totalWithPercent = totalValueSell * 10 / 100
        print(f"Value total with percent:  {totalWithPercent}")

    case totalValueSell if totalValueSell >= 50500:

        print(f"We exceed our goal this month. Congrats!The difference is {totalValueSell - 50500}. Only the winners will get the prize of 15 %")
        totalWithPercent = totalValueSell * 15 / 100
        print(f"Value total with percent: {totalWithPercent}")
