#-Escribe un programa que solicite al usuario un número decimal y luego imprima la parte entera y decimal por separado.

num = float(input('Ingrese un numero decimal: '))

entera = int(num)
decimal = num - int(num)

print('\nLa parte entera es:',entera,'y la decimal es:',decimal)