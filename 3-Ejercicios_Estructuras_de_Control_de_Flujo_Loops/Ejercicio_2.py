#-Escribe un programa que pida al usuario un número y calcule la suma de todos los números naturales del 1 hasta ese número.

num = int(input('Ingrese un numero: '))
cont = 0
suma = 0

while cont <= num:
    suma = suma + cont
    cont = cont + 1

print(suma)