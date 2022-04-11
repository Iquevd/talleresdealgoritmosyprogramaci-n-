#Entradas
x=int(input("Cantidad de préstamo de Bolívares: "))
y=int(input("Cantidad de intereses en 4 años: "))
#Caja negra
razon=(y*100)/(x*4)
porcentaje=razon/4
#Salidas
print("El porcentaje anual cobrado por el prestamo durante los 4 años es de:",porcentaje)