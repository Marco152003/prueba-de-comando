# Hacer un programa para calcular el pago de una compra con el criterio de pago con descuento correspondiente.
compra=int(input("Ingrese el monto de la compra "))
if compra < 800:
   print("El pago de la compra es ",compra)
elif 800 <= compra <= 1500:
    compra -= (compra*0.10)
    print("El pago de la compra con su respectivo descuento es ",compra)
elif 1500<compra<=5000:
    compra -= (compra*0.15)
    print("El pago de la compra con su respectivo descuento es ",compra)
