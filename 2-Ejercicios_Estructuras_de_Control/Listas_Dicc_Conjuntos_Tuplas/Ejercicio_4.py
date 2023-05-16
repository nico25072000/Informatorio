#Crear un diccionario con los nombres de tres personas y sus respectivas edades. Mostrar la edad de la tercera persona en el diccionario.

personas = {
    'nombre1': input('Ingrese tu nombre: '), 'edad1': int(input('Ingrese su edad: ')),
    'nombre2': input('Ingrese tu nombre: '), 'edad2': int(input('Ingrese su edad: ')),
    'nombre3': input('Ingrese tu nombre: '), 'edad3': int(input('Ingrese su edad: ')),
}

print('La edad de la tercera persona es:', personas['edad3'])