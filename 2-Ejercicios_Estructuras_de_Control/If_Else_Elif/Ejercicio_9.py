#Escribir un programa que pida al usuario tres números y muestre por pantalla el mayor de ellos.

n1 = float(input('ingrese primer numero: '))
n2 = float(input('ingrese segundo numero: '))
n3 = float(input('ingrese tercer numero: '))

if (n1 > n2 and n1 > n3):
    print('El numero mayor es:',n1)
elif (n2 > n1 and n2 > n3):
    print('El numero mayor es:',n2)
else:
    print('El numero mayor es:',n3)