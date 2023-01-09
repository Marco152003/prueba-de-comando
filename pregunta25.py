#Calcular el menor número de N valores
cantidad=int(input("Ingrese la cantidad de valores -> "))
minimo=9999
for i in range (cantidad):
    número=int(input("Ingrese el número -> "))
    if número<minimo:
        minimo=número
print("El menor número es ",minimo)
