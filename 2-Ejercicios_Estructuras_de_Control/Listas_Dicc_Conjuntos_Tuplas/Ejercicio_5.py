#Crear un set/conjunto con los números del 1 al 10 y mostrar el número más grande en el conjunto.

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
num = 0

for elemento in numeros:
    if (elemento > num):
        num = elemento

print('El numero mas grande es:',num)