# Uma locadora de veículos possui o dicionário abaixo em seu estoque.
# Neste dicionário, podemos encontrar o veículo e o valor do aluguel por dia.
#
# carros =
# {"Chevrolet Tracker": 120, "Chevrolet Onix": 90, "Hyundai HB20": 85,
# "Hyundai Tucson": 120, "Fiat Uno": 60, "Fiat Mobi": 70), "Fiat Pulse": 130}
#
# Faça um programa que um operador consiga verificar o estoque,
# retirar o veículo do estoque para locação informando: Veículo e tempo de locação
# e devolver o valor total da locação e,
# também, o operador deve conseguir inserir o veículo de volta ao estoque.

option = 0
storeInforCar = [5]
# normalCars = {"Chevrolet Tracker": 120,
# "Chevrolet Onix": 90,
# "Hyundai HB20": 85,
# "Hyundai Tucson": 120,
# "Fiat Uno": 60,
# "Fiat Mobi": 70, "Fiat Pulse": 130}

sportCars = {"Camaro Chevrolet SS": 4,
"Mustang GT": 3,
"BMW M2 CS TURBO": 5,
"Audi RS Avant TFSI": 0,
"Honda Civic Touring": 3,
}

valueOfCars ={"Camaro Chevrolet SS": 3500,
"Mustang GT": 7500,
"BMW M2 CS TURBO": 5890,
"Audi RS Avant TFSI": 6000,
"Honda Civic Touring": 4000,
}

while option != 'l':
    print("\nDo you like to drive sport car(1)?\n Or normal car?(2)\n Or Do you want to leave the program (l)?")
    option = input()
    if option == '1':
        for loop in sportCars.items():
            print(f"{loop[0]}. quantity: {loop[1]}")

        print(f"choice one of after copy and paste name:")
        carName = input()
        if carName in sportCars:

            if loop[1] > 0:
                print("This car is available at 18:50 p.m ")
            #Colocar o valor do carro escolhido
            # retirar o veículo do estoque para locação informando: Veículo e tempo de locação
            # e devolver o valor total da locação e,
            # também, o operador deve conseguir inserir o veículo de volta ao estoque.
            else:
                print("This car is unavailable")
                break
        else:
            print("This car doesn't exist in our system")