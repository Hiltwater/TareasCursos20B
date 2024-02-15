#Ejercicio 6, sección 1.2.7

#Dados los vectores: 

from sympy import *
init_printing(use_unicode=True)

a = Matrix([1,2,3])
b = Matrix([4,5,6])
c = Matrix([3,2,1])
d = Matrix([6,5,4])

#a) Encuentre: a + b + c + d , a + b − c − d , a − b + c − d , −a + b − c + d .

print()
suma1= a + b + c + d
print("La suma de los vectores de la forma: a + b + c + d")
print("Equivale a:")
print(suma1)
print()
suma2 = a + b - c -d
print("La suma de los vectores de la forma: a + b − c − d")
print("Equivale a:")
print(suma2)
print()
suma3 = a -b + c - d
print("La suma de los vectores de la forma: a − b + c − d")
print("Equivale a:")
print(suma3)
print()
suma4 = -a + b - c + d
print("La suma de los vectores de la forma: −a + b − c + d")
print("Equivale a:")
print(suma4)
print()
