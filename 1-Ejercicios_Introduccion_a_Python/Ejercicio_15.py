#Escribe un programa que solicite al usuario una temperatura en grados Celsius y luego imprima la temperatura equivalente en grados Fahrenheit.
#La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32.

temp = int(input('Ingrese temperatura en grados Celsius: '))

f = (temp*1.8) + 32

print('La temperatura en grados Fahrenheit es', f)