#Crear un diccionario con los nombres de tres frutas y sus respectivos precios y mostrar el diccionario completo.

tres_frutas = {
    'naranja': 800,
    'manzana': 300,
    'banana': 600,
}

for key, value in tres_frutas.items():
    print(key,':',value)