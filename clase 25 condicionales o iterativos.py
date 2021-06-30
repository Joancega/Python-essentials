# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 19:24:23 2021

@author: Usuario
"""

#Condicional if
nativeVlan=100
dataVlan=100

if nativeVlan==dataVlan:
    print("The native VLAN are the same")
#if es un condicional o iterativo simple
else:
    print("equis de")
#si le agrego un else es un condicional o iterativo doble

acl=int(input("ingrese el # de ACL: "))
if acl>=1 and acl <=99:
    print("La ACL es estandar")
elif acl>=100 and acl <=199:
    print("La ACl es extendida")
else:
    print("El # ingresado no es de ACl")
  
    
print("\n")   
 #ciclo repetitivo for

lista=["r1","r2","r3","s1","s2","s3","ap1","ap2","ap3"]

print(len(lista))
print("antes de for")


for i in lista:
    print(i)
    print("dentro de for")
# for recorre el vector sin necesidad de una condicion

print("fuera de for")
print("\n")

for i in lista:
    if "r" in i:
        print(i)
print("\n")
#imprime solo los valores r de la lista

listaR=[]
listaS=[]
listaAP=[]

for i in lista:
    if "r"in i:
        listaR.append(i)
        print(listaR) 
print("\n")        
for i in lista:
    if "s"in i:
        listaS.append(i)
        print(listaS)   
print("\n") 
for i in lista:
    if "ap"in i:
        listaAP.append(i)
        print(listaAP) 
print("\n")
#llena una lista con los valores de otra

for i in range(0,3,1):
    print(lista[i]) 
#devuelve los valores de acuerdo a la posicion

