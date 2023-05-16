#-Escribe un programa que solicite al usuario su peso y su altura, y luego calcule e imprima su índice de masa corporal (IMC).
#La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).

peso = float(input('Ingrese su peso: '))
altura = float(input('Ingrese su altura: '))

imc = peso / (altura**2)

print('Su indice de masa es:',imc)