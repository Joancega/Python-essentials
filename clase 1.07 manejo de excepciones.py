# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 19:14:18 2021

@author: Usuario
"""
"""
try:
    print("inicio")
    x=1/0
    print('proceso')
except:
    print("te jalaste")
print("fin")
"""
#maneja distintas excepciones

"""
try:
    x=int(input("Enter a number: "))
    y=1/x
    print(y)
except ZeroDivisionError:
     print("you cannot divide by zero")
except ValueError:
    print("you must enter an integer value")
except:
    print("something went wrong")

print("fin")
"""
#se pueden dividir distintas excepciones

"""
try:
    y=1/0
except ZeroDivisionError:
    print("Zero division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END.")
"""
#existen jerarquias de errores 
""" 
def readint(prompt, min,max):
    while (True):
        try:
            print("Ingrese un valor entre",min, "y",max,": ")
            x=int(input(prompt))
            assert min < x and max > x 
            return x
        except ValueError:
            print("Error en el ingreso")
        except:
            print("el valor no esta en el rango definido")
v = readint("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)
"""
#ejercicio realizado en clase

"""
try:
    import math
    import equisde
except:
    print("el modulo no existe")
"""
#me sirve para evaluar tambien si existen modulos
