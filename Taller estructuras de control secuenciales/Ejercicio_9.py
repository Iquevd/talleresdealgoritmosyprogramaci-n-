#Entradas
horas_t=int(input("Ingrese las horas trabajadas: "))
horas_p=float(input("Ingrese el precio por hora: "))
#Caja negra
sueldo_bruto=horas_t*horas_p
descuento_fijo=sueldo_bruto*0.20
salario_neto=sueldo_bruto-descuento_fijo
#Salidas
print(f"El descuento fijo es: {descuento_fijo} y el salario neto es: {salario_neto}")