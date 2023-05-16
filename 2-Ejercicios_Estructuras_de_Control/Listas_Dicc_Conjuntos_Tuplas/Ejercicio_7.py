#-Crear un diccionario con los nombres de tres ciudades y sus respectivas poblaciones. Agregar una cuarta ciudad al diccionario con su respectiva
#población. Mostrar el diccionario resultante.

ciudades = {
    'ciudad1': 'Resistencia', 'cant_pob1': 300000,
    'ciudad2': 'Barranqueras', 'cant_pob2': 250000,
    'ciudad3': 'Fontana', 'cant_pob3': 20000,
}

ciudades['ciudad4'] = input('Ingrese el nombre de la ciudad: ') 
ciudades['cant_pob4'] = int(input('Ingrese la poblacion: '))

for key, value in ciudades.items():
    print(key,':',value)