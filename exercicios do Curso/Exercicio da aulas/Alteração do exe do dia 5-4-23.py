#coolab so raodava na versão 3.9

print("The month's goal is 50.000.")
loop = 0

totalValueSell = 0

while True:
    valueSeller = int(input("Type your sells during of the month: "))

    totalValueSell += valueSeller
    loop += 1
    if loop == 5:  # com 5 funcionarios o minimo é fazer 333 vendas por dia
        break

if totalValueSell < 49500:
    print(
        f"Unfortunately, we don't get the goal this month. The difference is {totalValueSell - 49500}. Nobody going to receive the bonus")

elif totalValueSell == 49500:
    print(
        f"We just a little bit to reach.The difference is {totalValueSell - 49500}. Only the winners will get the prize of 5 %")

    totalWithPercent = totalValueSell * 5 / 100

    print(f"Value total with percent: {totalWithPercent}")

elif totalValueSell == 50000:

    print(
        f"We achieve our objetive this month. The difference is {totalValueSell - 50000}. Only the winners will get the prize of 10 %")

    totalWithPercent = totalValueSell * 10 / 100

    print(f"Value total with percent:  {totalWithPercent}")

elif totalValueSell >= 50500:

    print(
        f"We exceed our goal this month. Congrats!The difference is {totalValueSell - 50500}. Only the winners will get the prize of 15 %")

    totalWithPercent = totalValueSell * 15 / 100

    print(f"Value total with percent: {totalWithPercent}")
