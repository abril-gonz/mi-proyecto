
#1 _________________________________________________________________________________________
matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

matriz[1] [0]= 6
cantantes[0] ['nombre']= 'Enrique Martin Morales'
ciudades['México'] [2]= 'Monterrey'
coordenadas[0] ['latitud']= 9.9355431

print(matriz)
print(cantantes)
print(ciudades)
print(coordenadas)

#2 _________________________________________________________________________________________
## funcion con print -----------------------------------------------------
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario(d):
    for i in d:                        ##recorre los diccionarios
        listado= []                    #lista de pares por cada clave
        for k,v in i.items():          ##recorre las keys y values de cada diccionario
            pares=f'{k}- {v}'          #k-v ordenado
            listado.append(pares)      #agrega los k-v a la lista x clave
        print(', '.join(listado))      #imprime la lista separada por ","
                  
    
iterarDiccionario(cantantes)
'''
## funcion con return -----------------------------------------------------
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario(d):
    listado= []
    for i in d:                     ##recorre los diccionarios
        nyp=[]                      #guarda k-v ordenados
        for k,v in i.items():       ##recorre las keys y values de cada diccionario
            pares=f'{k}- {v}'       #k-v ordenado
            nyp.append(pares)       #agrega k-v a una lista                     
        z= ', '.join(nyp)           #separa los pares con ','
        listado.append(z)           #agrega los pares separados    
    return '\n'.join(listado)       #devuelve los pares uno abajo del otro

print(iterarDiccionario(cantantes))


'''
#3 _________________________________________________________________________________________
## funcion con print -----------------------------------------------------
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario2(c,l):
    contenido=[]                    #lista principal
    for i in l:                     ##recorre los diccionarios de la lista             
        contenido.append(i[c])      #agrega los values segun la clave a la lista
    for y in contenido:             ##recorre la lista principal
        print(y)                    #imprime valores por cada clave
    
iterarDiccionario2("pais", cantantes)
'''
##funcion con return -----------------------------------------------------
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario2(c,l):
    contenido=[]                    #lista principal
    for i in l:                     ##recorre los diccionarios de la lista
        info=[]                     #lista de valores x clave
        valores= i[c]               #guarda los values de cada diccionario
        info.append(valores)        #agrega los values a la lista de valores x clave
        x= " ".join(info)           #guarda los values separados
        contenido.append(x)         #agrega a la lista principal            
    return '\n'.join(contenido)     #devuelve valores por cada clave, uno abajo del otro

print(iterarDiccionario2("nombre", cantantes))
'''
#4 _________________________________________________________________________________________
## funcion con print -----------------------------------------------------
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(d):
    for c in d:                                         #recorre las claves del diccionario
        print((f'{len(d[c])} {c.upper()}'))             #imprime cantidad de valores en la lista junto con la clave en mayuscula
        for x in d[c]:                                  #recorre los valores de la lista x cada clave
            print(f'-{x}')                              #imprime cada valor de la lista x cada clave

imprimirInformacion(costa_rica)
'''
## funcion con return -----------------------------------------------------
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(d):
    listado= []                                                #listado principal
    for c in d:                                                #recorre las claves del diccionario
        categ = f'{len(d[c])} {c.upper()}'                     #titulo(cantidad de valores en la lista con la clave en mayusculas)
        listado.append(categ)                                  #agrega las categorias al listado
        for i in d[c]:                                         #recorre los valores de la lista, por cada clave
            listado.append(f'-{i}')                            #agrega los valores al listado, segun la clave
    return '\n'.join(listado)                                  #devuelve la lista separando cada elemento


print(imprimirInformacion(costa_rica))
'''