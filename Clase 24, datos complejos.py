# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 19:43:12 2021

@author: Usuario
"""

"""
tupla: Es una variable que permite almacenar 
datos inmutables.Es como un vector.
    tupla=(x0,...,xn)
    print(tupla[i]) da como resultado xi
    
lista: la lista es lo mismo pero los datos 
son modificables
    lista[x0,...xn]
    lista[i]=x, cambia el valor de la 
    posicion i por x.
    
diccionario: Es una lista pero su posicion se
define con una clave
    diccionario={clave0:x0,...,clave n:xn}
    print(diccionario[clavei]) da como resultado xi

"""

lista1=["Ikna",69,4.20,True]
#para ver las variables hay que dar click en el valor de size

print(type(lista1))

print(len(lista1))
#imprime la longitud de la lista

tupla1=("Ikna",69,4.20,True)

print(tupla1[0:3])
#imprime los valores del 0 al 3

print(tupla1[:3])
#imprime la izquierda 

print(tupla1[2:])
#imprime solo la derecha y la posicion

print(tupla1[-1])
#devuelve el valor 1 del otro lado del cero


#permite cambiar el tipo de dato en la celda
lista1[3]=False

del lista1[2]
#borra el valor de la celda2
print(len(lista1),"\n"*2)
#del no funciona con la tupla

dict1={"R1":"10.10.01","R2":"10.10.02",
       5.0:"1727035717","Juan":666}
print(dict1["R1"])

dict2={"R1":"10.10.01","R1":"10.10.02",
       5:"1727035717","Juan":666}
print(dict2["R1"])
#si pongo la misma clave su valor se cambia por el ultimo

print(dict1)
#si no pongo la posicion se imprime todo

print(5 in dict1)
#me comprueba si la clave existe en el diccionario

dict1["R3"]="XD"
# Es posible añadir claves y posiciones

