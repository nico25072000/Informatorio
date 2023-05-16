#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es positivo, negativo o cero.

num = int(input('Ingrese un numero entero: '))

if (num > 0):
    print('Es positivo')
elif (num < 0):
    print('Es negativo')
else:
    print('Es cero')