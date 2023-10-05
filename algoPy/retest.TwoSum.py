from typing import List

def twoSum(nums: List[int], target:int) -> List[int]:
  #print(f"Entrou {nums} | {target}")
    sumof = 0
    sequences = []

    for x in range(0,len(nums)):
        for y in range(x + 1,len(nums)):
            sumof = int(nums[x]) + int(nums[y])
            if x != y  and sumof == target:
                print(f"Entrou {x} | {y}")






nums = []
whilLoop = 0
target = 6
while True:
    number = input("Digite os valores, digite qualquer letra para sair: ")
    if number.isalpha():
        break
    try:
        nums.append(number)
    except ValueError:
        print("Deu erro ao captar o valor")
    
twoSum(nums, target)
