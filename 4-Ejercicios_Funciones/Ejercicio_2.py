#Crea una función llamada saludo que tome el nombre de una persona como parámetro e imprima un saludo personalizado.

def saludo(nom):
    x = input('Escriba lo que quieras decir a',nom,':')
    return x

nombre = input('Ingrese su nombre: ')
print(saludo(nombre))