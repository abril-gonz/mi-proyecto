
#1

def multiplicador_hasta(num):
    valores= []
    for nums in range(num+1):
        nums *= 2
        valores.append(nums)
    return valores


print(multiplicador_hasta(5))

#2

ej= [3,2]

def operations(ej):
    suma= sum(ej)
    print(suma)
    resta= ej[0]-ej[1]
    return resta


print(operations(ej))

#3

lista= [9,2]

def sum_len(lista):
    op= sum(lista) - len(lista)
    return op

print(sum_len(lista))


#4

lista= [1, 3, 5, 7]

def new(lista):
    lis1= []
    for num in lista:
        lis1.append(num*2)
    print(len(lis1))
    if len(lista) < 2:
        lis2= []
        return lis2
    else:
       return lis1
    
print(new(lista))


#5

def value_len (value, long):
    lista= []
    mul= value * long
    while len(lista) < long:
        lista.append(mul)
    return lista

print(value_len(5, 2))

