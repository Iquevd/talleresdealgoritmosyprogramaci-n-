#Entradas
precio1=int(input("Ingrese el precio final de un producto: "))
precio2=int(input("Ingrese el precio de venta al publico del producto: "))
#Caja negra
diferencia=(precio2-precio1)
descuento=(diferencia/precio2)*100
#Salidas
print("El porcentaje de descuento es:",descuento)