# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 18:12:49 2021

@author: Usuario
"""

def isPrime(num):
    contador=True
    if num >2:
        contador=False
        for comparador in range(2,num-1,1):
            if num % comparador == 0:
                contador =True
    #esta zona es para otros numeros y si funciona
    return contador
            
value=int(input("Ingrese un numero ")) 
numero= isPrime(value) 

if numero== True:
    print("No es primo")
else:
    print("Es primo")
