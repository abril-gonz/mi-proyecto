numero1 = 70 #declaracion de variable. inicializar primitivo numeral int
numero2 = 3.14 #declaracion de variable. inicializar primitivo numeral float
booleano = False #declaracion de variable. inicializar primitivo boolean
cadena = 'Hola Mundo' #declaracion de variable. inicializar primitivo string
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate'] #declaracion de variable. inicializar list
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False} #declaracion de variable. inicializar diccionario
frutas = ('guayaba', 'fresa', 'papaya') #declaracion de variable. inicializar tupla
print(type(frutas)) #revision de type 
print(ingredientes_pastel[2]) #accesar valor a lista
ingredientes_pastel.append('Mantequilla') #agragar valor a lista
print(persona['nombre']) #accesar valor a diccionario
persona['nombre'] = 'Kevin' #cambiar valor en diccionario
persona['color_ojos'] = 'cafe' #agregar valor a diccionario
print(frutas[2]) #accesar valor a tupla

if numero1 > 45:                #condicional if: evalua si numero1 es mayor a 45
    print("Numero mayor")       #se ejecuta si la condicion es true
else:                           
    print("Numero menor")       #se ejecuta si la condicion es false

if len(cadena) < 5:             #condicional if: evalua que len() (revision de tamaño de un string) sea menor a 5
    print("Cadena corta")       #ejecuta en caso de true
elif len(cadena) > 15:          #condicion adicial: evalua un segundo caso posible
    print("Cadena larga")       #ejecuta si la segunda condicion es true
else:                           
    print("Cadena perfecta")    #se ejecuta si las condiciones anteriores son false

for x in range(8):              #bucle for que recorre numeros desde el 0 (por defecto) y con fin en 8 (sin incluir)
    print(x)                    #se ejecuta por cada numero recorrido
for x in range(2,8):            #bucle for que recorre numeros con inicio en 2 y fin en 8 (sin incluir)
    print(x)                    #se ejecuta por cada numero recorrido
for x in range(2,8,2):          #bucle for que recorre los numeros de 2 en 2 con inicio en 2, fin en 8(sin incluir) 
    print(x)                    #imprime cada numero recorrido de 2 en 2
x = 0                           #variable declarada con valor 0
while(x < 8):                   #bucle while: ejecuta un codigo mientras la condicion se cuemple (mientras x sea menor a 8)
    print(x)                    #imprime el valor de x
    x += 1                      #tambien le suma 1 al valor de x cada vez que se cumpla la condicion

ingredientes_pastel.pop()       #accede al ultimo valor en la lista y lo quita
ingredientes_pastel.pop(1)      #accesa al valor en la posicion 1 de la lista y lo quita

print(persona)                  #imprime el diccionario(claves y valores)
persona.pop('color_ojos')       #extrae el valor de la clave indicada junto con su clave si no se indica un nuevo valor
print(persona)                  #imprime el diccionario actualizado

for ingrediente in ingredientes_pastel:             #bucle for que recorre los elementos de la lista
    if ingrediente == 'Harina':                     #condicional(para cada elemento) que verifica si es igual al string harina
        continue                                    #se salta la condicion indicada en caso de true y reinicia el bucle
    print('Después de la primera sentencia')        #imprime el string para cada elemento que pase por el condicional anterior
    if ingrediente == 'Chocolate':                  #condicional if que compara la igualdad del elemento con el string chocolate
        break                                       #termina de forma definitiva el bucle en caso de true

def imprime_hola_10_veces():                        #definicion de funcion sin parametros
    for numero in range(10):                        #bucle for que recorre los numeros con fin en 10 (sin incluir)
        print('Hola')                               #imprime para cada numero

imprime_hola_10_veces()                             #llamada de la funcion (se ejecuta el bloque de codigo)

def imprime_hola_n_veces(n):                        #definicion de funcion con parametro n
    for numero in range(n):                         #bucle for que recorre numeros con fin en n
        print('Hola')                               #imprime para cada numero

imprime_hola_n_veces(5)                             #llamada a funcion con argumento 5

def imprime_hola_n_o_diez_veces(n = 10):            #definicion de funcion con parametro n = 10 (valor por default)
    for numero in range(n):                         #recorre los numeros hasta n
        print('Hola')                               #imprime para todos los numeros

imprime_hola_n_o_diez_veces()                       #llamado a la funcion sin argumento (se ejecuta porque la funcion tiene un argumento por default)
imprime_hola_n_o_diez_veces(5)                      #llamado a la funcion con argumento 5(5 reemplaza el argumento por default)


"""
Sección BONUS
"""

# print(numero3)                            #NameError: name <variable name> is not defined
# numero3 = 86                              
# frutas[0] = 'naranja'                     #TypeError: 'tuple' object does not support item assignment
# print(persona['hobbies'])                 #NameError: name <variable name> is not defined
# print(ingredientes_pastel[11])            #IndexError: list index out of range
#   print(booleano)                         #IndentationError: unexpected indent
# frutas.append('manzana')                  #AttributeError: 'tuple' object has no attribute 'append'
# frutas.pop(1)                             #AttributeError: 'tuple' object has no attribute 'pop'