# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 13:06:38 2021

@author: Usuario
"""

Ecuador={"Pichincha":"Quito","Imbabura":"Ibarra","Guayas":"Guayaquil"}

print("Inserte la provincia")
x=input()
print(Ecuador[x])

password = input("Ingrese la contraseña: ")

if(password == "miClave"):
    print("Contraseña correcta. Te damos la bienvenida.")
else:
    print("Contraseña incorrecta.")

"""
ingreso=["x1","x2","x3"]
print("ingrese el nombre del estudiante 1")
print("ingrese el nombre del estudiante 2")
print("ingrese el nombre del estudiante 3")
x1=input()
x2=input()
x3=input()
print("El estudiante 1 es", x1)
print("El estudiante 2 es", x2)
print("El estudiante 3 es", x3)

print("\n","ingrese cualquier letra para salir")
x=input()
"""

"""
print("pn","\n"*2,"\t"*6,"kk")
print("pn","\t"*6,"\n"*2,"kk")
"""