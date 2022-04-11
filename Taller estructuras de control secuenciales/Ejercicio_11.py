#Entradas
nombre=str(input("Ingrese el nombre del trabajador: "))
horas_trabajadas=int(input("Ingrese las horas trabajadas: "))
pago_hora=float(input("Ingrese el pago por hora: "))
horas_extras=int(input("Ingrese las horas extras trabajadas: "))
total_hijos=int(input("Ingrese el total de los hijos: "))
#Caja negra
sb=pago_hora*horas_trabajadas#float
asignacion=(250000+173000*total_hijos+180000)#float
deduccion=sb*(0.05+0.02+0.07)#float
salario_descuentos=sb-deduccion
he_sin=pago_hora*horas_extras
he_con=he_sin*0.25+he_sin
sueldo_neto=asignacion+deduccion+he_con
#Salidas
print(f"Las asignaciones son: {asignacion}, las deducciones son: {deduccion} y el sueldo neto que recibira {nombre} en el mes de diciembre es de: {sueldo_neto} ")
