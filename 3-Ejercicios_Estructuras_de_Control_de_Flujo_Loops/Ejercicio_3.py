#Escribe un programa que pida al usuario un número y luego imprima la tabla de multiplicar correspondiente a ese número del 1 al 10.

num = int(input('Ingrese un numero: '))
i = 0

for i in range(11):
    if (i != 0):    
        result = i * num
        print('\n',num,'x',i,'=',result)