#-Escribir un programa que pida al usuario un carácter y muestre por pantalla si es una letra mayúscula, una letra minúscula, un número o un carácter especial.

mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
minusculas = 'abcdefghijklmnopqrstuvwxyz'
numero = '0123456789'

caract = str(input('Ingrese un caracter: '))

if (caract in mayusculas):
   print('Es una letra mayuscula')
elif (caract in minusculas):
   print('Es una letra minuscula')
elif (caract in numero):
   print('Es un numero')
else:
   print('Es un caracter especial')
