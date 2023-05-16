nombre_usuario = input('Ingrese un nombre de usuario: ')
contrasena = input('Ingrese una contraseña: ')

# print(f'El usuario es: {nombre_usuario} y la contraseña es: {contrasena}')

print('Ya podés ingresar a la plataforma con tu usuario y contraseña.')

nombre_usuario2 = input('Ingrese su nombre de usuario: ')
contrasena2 = input('Ingrese su contraseña: ')
booleano = True

while booleano:
 if nombre_usuario2 == nombre_usuario:
   if contrasena2 == contrasena:
      print('Usted ingresó correctamente.')
      booleano = False 
   else:
      print('La contraseña ingresada no es correcta. Vuelva a ingresar.')
      contrasena2 = input('Ingrese su contraseña: ')
else:
    print('El usuario ingresado es incorrecto. Vuelva a ingresar.')
    nombre_usuario2 = input('Ingrese su nombre de usuario: ')