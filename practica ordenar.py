# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 12:33:46 2021

@author: Usuario
"""


condicion="seguir"

while condicion == "seguir":
    
    entrada=[]
    #encera la lista
    
    limit = int(input("Cuantos valores desea ingresar?:"))
    # pone el numero de datos
    
    
    for i in range(0,limit,1 ): 
        value= float(input("ingrese un numero "))
        entrada.append(value) 
    # carga los valores de entrada
    
        
    for i in range(0,limit,1): 
        for j in range(0,limit-1,1):
            if entrada[j] > entrada[j+1]:
                entrada[j],entrada[j+1]=entrada[j+1],entrada[j]
    #ordenanamiento burbuja    
              
    print(entrada)
    # imprime la lista ordenada
    
    condicion=(input("desea seguir ordenando valores? responda con -seguir-: "))

