#Escribe un programa que solicite al usuario su información personal, incluyendo
#su nombre completo, edad, estatura, peso, dirección y número de teléfono.
#A continuación, el programa deberá imprimir un mensaje con los datos
#ingresados por el usuario en el siguiente formato:
#La información ingresada es la siguiente:
#Nombre completo: [nombre completo]
#Edad: [edad]
#Estatura: [estatura] cm
#Peso: [peso] kg
#Dirección: [dirección]
#Número de teléfono: [número de teléfono]


nombre_comp = input('Ingrese su nombre completo: ')
edad = input('Ingrese su edad: ')
estatura = input('Ingrese su estatura: ')
peso = input('Ingrese su peso: ')
direccion = input('Ingrese su direccion: ')
num_telef = input('Ingrese su numero de telefono: ')

print('\nNombre completo:',nombre_comp,'\nEdad:',edad,'\nEstatura:',estatura,'cm','\nPeso:',peso,'kg','\nDireccion:',direccion,'\nNumero de telefono:',num_telef)