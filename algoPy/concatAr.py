#https://leetcode.com/problems/concatenation-of-array/
#nums
#n
#ans
condition = True
whileLoop = 0
nums = []
print("Digite os valores e para terminar digite s(sair)")
while condition:
    values = input()

    if values == "s":
        
        condition = False
        break
    nums.append(values)
    whileLoop +=1

n = len(nums)
ans = []
for i in range(2*n):
    ans.append(nums[i%n])# isso aqui é o resto da divisão não 
# não é a parte do quociente

print(ans)
#ans = nums.copy()

#if ans == nums:
    #nums = ans
#    print(f"Junção dos nums e ans {nums} {ans}")
