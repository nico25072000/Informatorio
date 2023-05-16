#-Escribir un programa que pida al usuario un número entero y muestre por pantalla si es múltiplo de 2 y de 3 a la vez.

num = int(input('Ingrese un numero entero: '))

if (num % 2 == 0 and num % 3 == 0):
    print('Es multiplo de 2 y de 3')
else:
    print('No es multiplo de 2 y de 3')