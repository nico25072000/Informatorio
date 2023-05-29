import random

nombre_usuario = input('\nIngrese nombre de usuario: ')

print(f'\nHola! {nombre_usuario}, el juego a jugar es: tenes que adivinar el numero\n')
print('El numero adivinar esta entre 1 y 100, y tenes 8 intentos para poder adivinarlo\n')

aleatorio = random.randint(1, 100)
#print(aleatorio)
x = input('Ingrese un numero: ')
intentos = 8


while intentos > 0:

    valido = False
    while valido == False:
        if x.isdigit() == True:
            num = int(x)
            valido = True
        else:
            print('El numero que ingreso no es un numero. Por favor ingrese de vuelta\n')
            x = input('Ingrese de vuelta el numero: ')
            valido = False

    if num < aleatorio:
        print('\nEl numero que hay que adivinar es mayor')
        intentos = intentos - 1
        if intentos == 0:
            print('Se agotaron los intentos. El numero a adivinar era el',aleatorio)
            break
        else:
            print('Te quedan',intentos,'intentos\n')
            x = input('Ingrese otro numero: ')
    elif num > aleatorio:
        print('\nEl numero que hay que adivinar es menor')
        intentos = intentos - 1
        if intentos == 0:
            print('Se agotaron los intentos. El numero a adivinar era el',aleatorio)
            break
        else:
            print('Te quedan',intentos,'intentos\n')
            x = input('Ingrese otro numero: ')
    else:
        print('HAS GANADO!. En el intento:',intentos)
        break