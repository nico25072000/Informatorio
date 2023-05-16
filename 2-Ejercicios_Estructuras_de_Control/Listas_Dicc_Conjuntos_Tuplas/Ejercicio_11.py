#-Crear una lista con los nombres de tres animales y agregar una cuarta animal al principio de la lista. Mostrar la lista resultante.

nombres = ['Leon', 'Elefante', 'Jirafa']

nombres.insert(0, input('Ingrese otro animal: '))

print(nombres)