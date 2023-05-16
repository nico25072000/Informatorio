#-Escribir un programa que pida al usuario dos números y muestre por pantalla la suma de ellos solo si ambos son pares.

n1 = int(input('ingrese primer numero: '))
n2 = int(input('ingrese segundo numero: '))

if (n1 % 2 == 0 and n2 % 2 == 0):
    print('La suma de los dos es:',n1+n2)
else:
    print('Son impares')