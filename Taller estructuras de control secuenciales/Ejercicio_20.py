#Entradas
precio=int(input("Ingrese el precio de la compra: "))
recargo=float(input("Ingrese el interes de la compra por cada cuota: "))
#Caja negra
cuota_n=precio/12
cuota_r=(cuota_n*recargo)/100+cuota_n
cuota_i=(cuota_r-cuota_n)*100/cuota_n
#Salidas
print("El cobro en porcentaje por los intereses del computador es:",cuota_i)
print("La cuota a pagar en conjunto al recargo mensual es:",cuota_r)