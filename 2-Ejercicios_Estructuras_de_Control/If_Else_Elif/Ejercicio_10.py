#Escribir un programa que pida al usuario una letra y muestre por pantalla si es una vocal o una consonante.

vocales = 'aeiouAEIOU'
letra = input('Ingrese una letra: ')


if (letra in vocales):
    print('Es una vocal')
else:
    print('Es una consonante')