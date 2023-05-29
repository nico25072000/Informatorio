inmuebles = []

def agregar(lista):
    booleano = True
    while booleano:
        año = int(input('Ingrese el año: '))
        metros = int(input('Ingrese los metros: '))
        habit = int(input('Cuantas habitaciones tiene? '))
        garaje = bool(input('Tiene garaje? '))
        zona = input('En que zona esta? ')
        estado = input('Cual es su estado? \n')
        op = input('Quiere agregar otro inmobilario? si/no ').lower
        if (op == 'si'):
            booleano = True
        else:
            booleano = False

def editar(lista):
    booleano = True
    while booleano:
        año = int(input('Ingrese el año: '))
        metros = int(input('Ingrese los metros: '))
        habit = int(input('Cuantas habitaciones tiene? '))
        garaje = bool(input('Tiene garaje? '))
        zona = input('En que zona esta? ')
        estado = input('Cual es su estado? \n')
        op = input('Quiere agregar otro inmobilario? si/no ').lower
        if (op == 'si'):
            booleano = True
        else:
            booleano = False
