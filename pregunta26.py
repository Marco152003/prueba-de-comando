#Hacer un programa que procese el monto de las compras de un cliente, variando el número de montos hasta que el cajero coloque de monto=0
total=0
monto=float(input("Ingrese el monto de una venta -> "))
while monto!=0:
    if monto<0:
       print("Monto no válido")
    else:
        total+=monto
        monto=float(input("Monto de una venta: $"))
if monto>1000:
    total-=total*0.1
print("Monto total a pagar es ",total)