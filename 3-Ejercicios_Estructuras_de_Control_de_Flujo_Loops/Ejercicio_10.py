#Escribe un programa que pida al usuario una cadena de texto y luego imprima la misma cadena pero con todas las vocales en mayúscula.

texto = input('Ingrese un texto: ')
lista_texto = list(texto)
vocales = {'aeiouAEIOU'}

for i in lista_texto:
    if (i in vocales):
        lista_texto[i] = lista_texto[i].upper()
        i = i + 1

texto = ''.join(lista_texto)
print(texto)