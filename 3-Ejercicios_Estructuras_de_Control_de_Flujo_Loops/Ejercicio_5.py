#-Escribe un programa que imprima la suma de todos los números pares del 1 al 100.

i = 0
suma = 0

for i in range(100):
    if (i % 2 == 0 and i != 0):
        suma = suma + i

print(suma)