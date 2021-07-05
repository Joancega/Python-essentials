# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 18:30:46 2021

@author: Usuario
"""

def fibonacci(n):
    a,b=0,1
    for i in range(0,n,1):
        print(a,end=" ")
        a,b=b,a+b
        """
        c=a+b
        a=b
        b=c
        """
    print()

valor=int(input("Ingrese cuantos numeros desea: "))
fibonacci(valor)