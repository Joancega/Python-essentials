# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 18:55:46 2021

@author: Usuario
"""

str1= "Ikna"
str2= "es"
str3= "guapo"
space=" "
numb= 69
#numb es intiger pero la hago string con str()
fakepi=22/7

print("\t",str1+space+str2+space+str3)
#"\t" sirve para tabular

print(str1,str2,str3,"\n"*(2))
#"\n" es un salto de linea y *2 me permite duplicarlo

print(str1,str2,str3,str(numb))
 #dice la verdad
print(str1,"\t"*2,str2,str3)
 
print(type(numb))

print(fakepi)
print("{:.2f}".format(fakepi))
 

