#-Escribe un programa que imprima los números pares del 1 al 100.

i = 0

for i in range(100):
    if (i % 2 == 0 and i != 0):
        print('\n',i)