#Hacer un programa simple que calcule los números divisibles entre 4 en el intervalo (3,10)
print("Se coloco un rango de numeros del 3 al 10 , y solo se considerará los numeros que sean divisibles entre 4:")
for i in range (3,10):
    if i % 4 == 0:
        print("-",i)