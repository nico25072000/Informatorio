#Crea un programa que pida al usuario dos números enteros y muestre en pantalla su cociente y su resto.

num1 = int(input('Ingrese un numero: \n'))
num2 = int(input('Ingrese otro numero: \n'))

cociente = num1 / num2
resto = num1 % num2

print('El cociente es:',cociente,'y el resto es:',resto)