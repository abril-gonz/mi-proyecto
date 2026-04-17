#0 lista de datos
ventas=[ 
    {'fecha': '03-09-2025', 'producto':'alfajores_maicena_6u', 'cantidad': 12, 'precio': 7000.0},
    {'fecha': '24-09-2025', 'producto':'alfajores_maicena_12u', 'cantidad': 15, 'precio': 12000.5},
    {'fecha': '18-11-2025', 'producto':'pastafrola', 'cantidad': 7, 'precio': 16000.2},
    {'fecha': '29-01-2026', 'producto':'lemmon_pie', 'cantidad': 8, 'precio': 19000.0},
    {'fecha': '05-02-2026', 'producto':'torta_personalizada_xkg', 'cantidad': 1, 'precio': 30000.0},
    {'fecha': '17-02-2026', 'producto':'pastafrola', 'cantidad': 8, 'precio': 16000.2},
    {'fecha': '19-02-2026', 'producto':'lemmon_pie', 'cantidad': 6, 'precio': 19000.0},
    {'fecha': '24-02-2026', 'producto':'tarta_ricota', 'cantidad': 2, 'precio': 19000.0},
    {'fecha': '14-02-2026', 'producto':'alfajores_maicena_12u', 'cantidad': 18, 'precio': 12000.5},
    {'fecha': '09-03-2026', 'producto':'lemmon_pie', 'cantidad': 5, 'precio': 19000.0},
    {'fecha': '12-03-2026', 'producto':'torta_personalizada_xkg', 'cantidad': 2, 'precio': 30000.0},
    {'fecha': '17-03-2026', 'producto':'alfajores_maicena_6u', 'cantidad': 19, 'precio': 7000.0}
    ]

productos_precios= [
    {'alfajores_maicena_6u': '7000.0'},
    {'alfajores_maicena_12u': '12000.5'},
    {'pastafrola': '16000.2'},
    {'tarta_ricota': '19000.0'},
    {'lemmon_pie': '19000.0'},
    {'torta_personalizada_xkg': '30000.0'}
]

# 2 Calculo de Ingresos Totales

def Ingresos_totales(l):
    ingresos=[]                                         #lista de ingresos por producto
    for i in ventas:                                    ##recorre los diccionarios
        ingresos.append(i['precio']*i['cantidad'])      #agrega cantidadxprecio por producto (se repite por diccionario)                                    
    return f'ingresos totales: {sum(ingresos)}'         #devuelve la suma de los ingresos por producto


print(f'\n{Ingresos_totales(ventas)}\n')


#3 Analisis del Producto Mas Vendido

ventas_por_producto= {

}

#bucle que agrega las claves y valores a ventas_por_producto

for i in ventas:                                                                #recorre los diccionarios en ventas                                                            
    if i['producto'] not in ventas_por_producto:                                #condicional if para agregar claves y valor a ventas_por_producto una vez
        ventas_por_producto.setdefault(i['producto'], i['cantidad'])            #por default agrega el nombre del producto y su cantidad como value
    else:                                                                       #condicion cuando se repiten las claves
        x= ventas_por_producto[i['producto']] + i['cantidad']                   #variable que guarda las sumas del valor en ventas_por_producto y el valor de cantidad en ventas ya repetido
        ventas_por_producto[i['producto']]= x                                   #define a x como nuevo valor cada vez que se sume una nueva cantidad

print(f'ventas por producto:\n {ventas_por_producto} \n')


#identificador producto mas vendido

producto_mas_vendido= {
    
}

max_valor= 0
clave_max= ''

for c, v in ventas_por_producto.items():                                                    ##recorre las claves y valores del diccionario de ventas por producto                                          
    if v > max_valor:                                                                       #condicional if para comparar el valor de cada producto(siendo el valor su cantidad de ventas totales) con una variable de valor inicial 0
        max_valor= v                                                                        #si el valor resulta mayor a la variable, toma el valor de v
        clave_max= c                                                                        #si el valor resulta mayor a la variable, la variable clave_max toma el valor c

producto_mas_vendido.setdefault(f'producto mas vendido: {clave_max}', {max_valor})  

print(f'{producto_mas_vendido} \n') 


#4 promedio de Precio por Producto

precios_por_producto= {

}

for i in ventas:                                                                                 #recorre los diccionarios en ventas
    ingreso_total = i['precio'] * i['cantidad']                                                  #por cada diccionario guarda el ingreso total  
    cantidad_total = i['cantidad']                                                               #por cada diccionario guarda la cantidad                                                                     
    if i['producto'] not in precios_por_producto:                                                #condicional if para agregar la clave (nombre del producto) una sola vez. tambien como clve agrega una tupla de dos elementos
        precios_por_producto[i['producto']]= (ingreso_total, cantidad_total)          
    else:                                                                                        #condicional else cuando los nombres de los productos se repiten
        ingreso_final, cantidad_final = precios_por_producto[i['producto']]                      #llama a los elementos de la tupla para transformarlos a variables
        ingreso_final= ingreso_final + ingreso_total                                             #reemplaza el valor cada vez que se repite el producto. Suma lo que habia en la tupla + el ingreso total guardado en el i repetido
        cantidad_final= cantidad_final + cantidad_total                                          #idem, con cantidad
        precios_por_producto[i['producto']]= (ingreso_final, cantidad_final)                     #va reemplazando la tupla anterior con otra con los valores actualizados

print(f'ingresos y cantidades por producto: \n {precios_por_producto} \n')


promedio= {

}

for x, (i, c) in precios_por_producto.items():                     ##recorre las claves y valores(elementos dentro de las tuplas) del diccionario precios por produto
    p= i / c                                                       #se calcula el promedio con el ingreso / cantidad de cada producto
    promedio[x]= p                                                 #se agrega la clave con el nombre del producto y con el promedio como valor

print(f'promedio por producto: \n {promedio} \n')


#5 Ventas por Dia

ingresos_por_dia= { 
    
}

for i in ventas:                                                                    ##recorre los diciconarios en ventas
    if i['fecha'] not in ingresos_por_dia:                                          
        ingresos_por_dia.setdefault(i['fecha'], i['precio']*i['cantidad'])          #por el condicional, agrega la fecha como clave y precioxcantidad como valor una vez por producto 
    else:
        x= ingresos_por_dia[i['fecha']] + i['precio']*i['cantidad']                 
        ingresos_por_dia[i['fecha']]= x                                             #por else, cuando la fecha se repite se suma el valor guardado en la fecha ya añadida y se le suma precioxcantidad de la repetida

print(f'ingresos por dia: \n {ingresos_por_dia} \n')


#6 Representacion de Datos

resumen_ventas= {
    
}

for x, (i, c) in precios_por_producto.items():              ##recorre las claves y valores(elementos dentro de las tuplas) del diccionario precios por produto                   
    resumen_ventas.setdefault(x,)                           #agrega los nombres del producto como clave
    resumen_ventas[x] =[                                    #agrega una lista como valor a cada producto, con su informacion correspondiente
        {'cantidad total': c},
        {'ingresos totales': i},
        {'precio promedio': i/c} 
    ]


print(f'resumen de ventas:\n {resumen_ventas}')
