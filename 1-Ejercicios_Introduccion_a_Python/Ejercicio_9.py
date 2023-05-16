#-Escribe un programa que solicite al usuario dos números y luego imprima la suma, la resta, la multiplicación y la división de los dos números.

num1 = int(input('Ingrese un numero: \n'))
num2 = int(input('Ingrese otro numero: \n'))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print('La suma es:', suma)
print('La resta es:', resta)
print('La multiplacion es:', multiplicacion)
print('La division es:', division)