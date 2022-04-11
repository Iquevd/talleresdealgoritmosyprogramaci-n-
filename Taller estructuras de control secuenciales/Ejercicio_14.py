#Entradas
lectura1=int(input("Ingrese la lectura anterior de kilovatio: "))
lectura2=int(input("Ingrese la lectura actual de kilovatio: "))
lectura3=int(input("Ingrese el costo por kilovatio: "))
#Caja negra
monto=abs(lectura2-lectura1)*lectura3
#Salidas
print("El monto total a pagar en un mes de luz es:",monto)