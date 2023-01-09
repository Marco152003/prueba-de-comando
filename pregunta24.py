#Hacer un programa que calcule la suma de todos los n numeros enteros y la suma de sus numeros pares
print("Calcular la suma de todos los n numeros enteros y la suma de sus números pares.")
cantidad = int(input("Ingrese la cantidad de datos -> "))
suma = 0
par = 0
for i in range(1, cantidad+1):
    num = int(input("Digite el numero:.."))
    suma = suma + num
    if num % 2 == 0:
     par = par + num
print("La suma de todos los numeros es:...",suma)
print("La suma de los numeros pares es:...",par)