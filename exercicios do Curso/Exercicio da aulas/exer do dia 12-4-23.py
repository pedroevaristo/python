# Considere a lista a seguir como a quantidade de itens vendidos por cada vendedor de uma loja.
# vendas = [100, 150, 1500, 2000, 120]
# Caso o vendedor tenha vendido mais de 1000 unidades, ele ganha um bônus de 15% sobre seu salário.
# Fazer um programa que informa quem conseguiu o bônus.

sells = [100, 150, 1500, 2000, 120]
sumOfEmployers = 0
for loop in range(len(sells)):
    if sells[loop] > 1000:
        sumOfEmployers += 1
        resultValuePorcent = sells[loop] * 15 / 100

print(f"just {sumOfEmployers} will receive the bonus")