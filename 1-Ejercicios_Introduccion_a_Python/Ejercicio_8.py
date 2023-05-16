#Crea un programa que pida al usuario el radio de un círculo y muestre su diámetro, su circunferencia y su área.
#Supón que pi es aproximadamente 3.14159.

pi = 3.14159

radio = int(input('Ingrese el radio: '))

diametro = radio*2
circunferencia = pi*diametro
area = pi * radio**2 

print('El diametro es:',diametro)
print('La circunferencia es:',circunferencia)
print('El area es:',area)