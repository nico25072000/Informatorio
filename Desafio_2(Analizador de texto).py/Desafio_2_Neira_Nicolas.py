print('\nPrograma para analizar textos\n')
texto = input('Ingrese un texto, puede ser un articulo o frase: ').lower()
print('\nAhora le voy a pedir que ingrese 3 letras a eleccion\n')
letra1 = input('Ingrese primer letra: ').lower()
letra2 = input('Ingrese segunda letra: ').lower()
letra3 = input('Ingrese tercer letra: ').lower()

lista_letra = [letra1, letra2, letra3]
lista_texto = texto.split()
lista_letras = list(texto)
cant = 0
cant_pal = 0

for i in texto:
    if (i in lista_letra):
        cant = cant + 1

for i in lista_texto:
    cant_pal = cant_pal + 1
    
    if (i == 'python'):
        boolean = True
    else:
        boolean = False

for i in reversed(lista_texto):
    print(i)

if boolean:
    print('Aparece la palabra python en el texto')
else:
    print('No aparece la palabra python en el texto')

if lista_letras[-1] == '.':
    ult_letra = lista_letras[-2]
else:
    ult_letra = lista_letras[-1]

print('La cantidad de veces que aparecen las letras son:',cant)
print('La cantidad de palabras que hay en el texto son:',cant_pal)
print('La primer letra es:',lista_letras[0],'y la ultima letra es:',ult_letra)