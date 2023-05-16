#Crea un programa que pida al usuario el radio de un círculo y calcule su área. La fórmula A = pi * r^2. Luego, muestra en pantalla el resultado.
#Supongamos que pi = 3.1416

pi = 3.1416

print('Programa para calcular el area de un circulo\n')
radio = int(input('Ingrese radio: '))

a = pi * radio**2

print('El area es:',a)