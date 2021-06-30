# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:10:41 2021

@author: Usuario
"""

data={"r1":"a1","r2":"a2","r3":"a3"}
condition="Nachito"


while condition=="Nachito":
    entry=input("Ingrese la caracteristica de Igna que desea consultar")
    print(data[entry])
    condition=input("Si desea consultar otra caracteristica escriba: Nachito ")
    