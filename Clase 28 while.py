# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:20:45 2021

@author: Usuario
"""

contar=input("Ingrese el # al que debo contar: ")
contar=int(contar)
if contar>=0:
    contador=1
else:
    contador=-1
"""
while contador <= contar:
    print(contador)
    contador +=1 
    print("Dentro de while")
print("fuera de while")
"""
#me permite contar

"""
if contador==1:
    while True:
        print(contador)
        contador +=1
        if contador>contar:
            break
else:
    while True:
        print(contador)
        contador -=1
        if contador<contar:
            break
"""
# Me permite contar a numeros positivos y negativos


"""
while True:
    x= input("Enter a number to count to:")
    if x=="q" or x=="quit":
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y +=1
        if y>x:
            break
 """
# Cuenta pero me permite salir escribiendo q  

