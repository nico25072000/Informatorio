#Escribe un programa que pida al usuario una palabra y determine si es un palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a
#izquierda).

palabra = input('Ingrese una palabra: ')
pal_reves = palabra[::-1]

if (palabra == pal_reves):
    print('Es un palindromo')
else:
    print('No es un palindromo')