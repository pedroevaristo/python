#https://leetcode.com/problems/two-sum/
# nums =  [2,7,11,15], target = [9]
quantityReceive = input("Digite a quantidade de numeros que irá digitar: ")
targetReceive = input("Digite o valor da soma do numeros que vc quer:")

target = int(targetReceive)
quantity = int(quantityReceive)


list = []
stockList = []
sum = 0


for i in range(0, quantity):
    receiveValues = int(input(f"{i}: "))
    list.append(receiveValues)
    

# juntar as coisas dentro do while e for, e colocar em um loop só
for x in range(0, quantity):
    for y in range(x + 1, quantity):
        
        if(x != y and list[x] + list[y] == target):
            print(f"[{x} : {list[x]}, {y} : {list[y]}]")
            
            break
    
        





#    if sum == target: 
#        print(f"{stockList}")
#        break
#    while sum > target:
#        sum -= list[x]
        

#        print("Não foi encontrado o valor que seja igual ao target")

