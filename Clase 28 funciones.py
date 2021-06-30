# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 19:08:23 2021

@author: Usuario
"""

"""
FUNCIONES

bloques de codigos con una funcion definida
funcion es una variable con parentesis
    ej. input()
    lo que va entre parentesis son las variables

las funciones se invocan con def:
    ej def message():
      
"""

"""
print ("Ingrese un valor: ")
a=input()
print ("Ingrese un valor: ")
b=input()
print ("Ingrese un valor: ")
c=input()
print(a,b,c)

def mensaje():
    print("por favor ingrese un # \n")
    
print("inicio")
mensaje()
a=input()
mensaje()
b=input()
mensaje()
c=input()
print(a,b,c)
"""

def hola(nombre):
    print("hola:", nombre)

hola("Ana")
#funcion con un parametro

def hola2(nombre1,nombre2):
    print("hola:", nombre1)
    print("hola:", nombre2)
hola2("Ana","Pancho")
#funcion con 2 parametros

"""
def direccion(calle, codigopostal, ciudad):
    print("su ciudad es: \nCiudad :", ciudad)
    print("La calles es: \nCalle :",calle)
    print("Y su codigo postal es: \t",codigopostal)

print("Ingrese los siguientes datos: ")
cl=input("ingrese la calle: ")
cu=input("ingrese la ciudad: ")
cp=input("ingrese la c. postal: ")

direccion(cl,cp,cu)
"""
def resta(a,b):
    print("El resultado de la resta es: ", a-b, "\n")
    
resta(5,2)
resta(2,5)
resta(a=2,b=5)
resta(b=3,a=15)
resta(3,b=15)

def mult(a,b):
    #print(a*b)
    return(a*b)
#return me devuelve el valor, aunque no necesariamente lo imprime

mult(5,5)

def mult2(a,b):
    #print(a*b)
    return(a*b,a-b)
#return me devuelve el valor, aunque no necesariamente lo imprime

print(mult2(5,5),mult2(5,6))

def funlist(lista):
    for i in lista:
        print("hola ",i)

lista_nombre=["juan", "paco","pedro"]

funlist(lista_nombre)
# devuelve el valor de una lista

def crealista (n):
    lista1=[]
    for i in range(n):
        lista1.append(i)
    return lista1
print(crealista(10))
# devuelve el valor de la lista

def sumatoria(*arg):
    sum=0
    for i in arg:
        sum += i
    print("la suma es: ",sum)
    
sumatoria(3,5,9,10)
# el *arg hace que sea dinamica la entrada de datos

