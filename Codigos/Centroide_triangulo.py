#Ejercicio 3, sección 1.1.6

'''
Los vertices de un triángulo ABC tienen como vectores posición 
a, b y c, respectivamente y relativos a un origen común O. 
Demuestre que el vector posición g del centróide G del triángulo
viene dado por: 

g = (1/3)(a + b + c)
'''

import time

print("Este programa halla el vector posición del centroide de un triangulo a partir de los vectores posición de sus vertices.")
print()
time.sleep(1)

A = [] #Vector vertice a
B = [] #Vector vertice b
C = [] #Vector vertice c
D = [] #Sumatoria de vectores a,b,c
G = [] #Vector centroide

n = 3 #Dimensión del espacio

print("Dijite las coordenadas de los vectores.")
print()
time.sleep(1)

for i in range (1,n+1,1):
    a = int(input(f"Dijite la coordenada número {i} del primer vector: "))
    A.append(a) 

print()
for i in range (1,n+1,1):
    b = int(input(f"Dijite la coordenada número {i} del segundo vector: "))
    B.append(b)

print()
for i in range (1,n+1,1):
    c = int(input(f"Dijite la coordenada número {i} del tercer vector: "))
    C.append(c)

print()
print(f"Los vectores posición de los vertices del triángulo dijitados son: {A}, {B}, {C}.")

for i in range(len(A)): #Se suman los tres vectores y se dividen en 3
    a1 = A[i]
    b1 = B[i]
    c1 = C[i]
    suma = a1 + b1 + c1
    D.append(suma)

for i in range(len(D)):
    g1 = D[i]
    g = g1/3 
    G.append(g)

print()
print(f"El vector posición del centroide del triangulo es: {G}")    