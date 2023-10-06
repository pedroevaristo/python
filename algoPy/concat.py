nums = [1,2,1]

def concat(nums):
    return nums + nums

leng = len(nums)
ans = []

ans = concat(nums)

print(f"{ans}")
#concatenação é a duplicata seja conjuntos de caracteres ou numeros
#basicamente pego a lista como já em string usa o "+" e faz uniao da lista
#de novo