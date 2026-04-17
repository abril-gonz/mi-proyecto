# numeros enteros del 0 al 100
for nums in range(0, 101):
    print(nums)

print("----------")
# multiplos de 2
for mul2 in range(2, 501, 2):
    print(mul2)

print("----------")
# contando vanilla ice
for num in range(1, 101):
    if (num / 10).is_integer():     # detecta int con .is_integer()
        print("ice ice")
    elif num % 5 == 0:               # detecta int con resto(%) = 0
        print("baby") 
    else:
        print(num)
print("----------")
# numero grande
bignum = 0

for i in range(2,500000,2):
    bignum += i

print(bignum)

print("----------")
# conteo hacia atras 3 en 3
print(list(range(2024,0,-3)))

print("----------")
# contador dinamico con multiplo
numInicial= 0
numFinal= 104
multiplo= 13

for contador in range(numInicial, numFinal+1):
    if contador % multiplo == 0:
        print(contador)



