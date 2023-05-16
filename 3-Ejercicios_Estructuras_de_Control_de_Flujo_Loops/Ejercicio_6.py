#-Escribe un programa que pida al usuario una palabra y luego imprima la misma palabra pero con las letras en orden inverso.

palabra = input('Ingrese una palabra: ')
lista_pal = list(palabra)

for i in reversed(lista_pal):
    print(i)