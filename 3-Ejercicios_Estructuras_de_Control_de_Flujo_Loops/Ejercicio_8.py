#Escribe un programa que pida al usuario una cadena de texto y luego imprima el número de palabras que contiene.

texto = input('Ingrese un texto: ')
lista_texto = texto.split()
cont = 0

for i in lista_texto:
    cont = cont + 1

print('Contiene',cont,'palabras')