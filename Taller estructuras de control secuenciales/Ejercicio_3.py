#Entradas
venta1=float(input("Ingrese la primera venta: "))
venta2=float(input("Ingrese la segunda venta: "))
venta3=float(input("Ingrese la tercera venta: "))
sb=float(input("Ingrese el sueldo base: "))
#Caja negra
comision=(venta1+venta2+venta3)*0.10
sueldo_total=comision+sb
#Salidas
print(f"El sueldo base es: {sb}, la comision es: {comision} y el sueldo total es: {sueldo_total}")