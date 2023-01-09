#Hacer un programa que calcule el factorial de un número entero
print("Este codigo esta programado a arrojar el factorial de un nummero entero.")
numero = int(input("Digite el numero factorial para convertirlo en entero -> "))
fact = 1
for i in range(1,numero+1):
    fact = fact * i
print("El resultado es:...",fact)