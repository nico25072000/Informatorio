#-Crea un programa que pida al usuario una cantidad en dólares y la convierta a euros. Supón que el tipo de cambio es de 0.84 euros por dólar.

cambio = 0.84

cant_dol = int(input('Ingrese cantidad de dolares: '))

cant_euros = cant_dol * 0.84

print('La cantidad de euros es:',cant_euros)