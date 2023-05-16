#Trabajas en una empresa X donde sus vendedores cobran comisiones del 6% de
#sus ventas totales y el departamento comercial te solicita que ayudes a los
#vendedores a calcular sus comisiones creando un programa que les pregunte su nombre y cuánto han vendido en éste mes.
#Tu programa le va a responder con una frase que incluya su nombre y el monto que le corresponde por las comisiones.

comision = 0.06

nombre = input('Ingrese su nombre: ')
vendidos = int(input('Cuanto vendio en este mes? '))

monto = vendidos * comision

print('\nEL vendedor',nombre,'tiene un monto de',monto,'por las comisiones')