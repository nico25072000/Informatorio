

def buscar_palabra(lista, objetivo):
   variable = ''
   boolean = bool
   for palabra in lista:
      if palabra == objetivo:
         boolean = True 
         variable = objetivo
   return False


if buscar_palabra(['Hola', 'Mundo', 'Info', '2023'], 'Info') == True:
   print(f'Se encontró la palabra  en la lista.')
else:
   print('No se encontro')