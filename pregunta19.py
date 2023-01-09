#Hacer un programa que haga la tabla de multiplicación de cualquier número entero
tabla=int(input("Ingresa la tabla de multiplicar -> "))
for i in range (1,11):
    resultado = tabla*i
    print(tabla, "* ",i, "= ",resultado)