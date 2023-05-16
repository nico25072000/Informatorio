#-Escribe un programa que solicite al usuario su fecha de nacimiento en formato dd/mm/aaaa y luego imprima su edad en años.
#Utiliza la función .split()

fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')
fecha = fecha.split('/')
nacimiento_usuario= int(fecha[2])
actual=2023
edad= actual - nacimiento_usuario
print("Su edad actual es:", edad)