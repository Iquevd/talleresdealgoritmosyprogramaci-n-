"""
Entradas
Sueldo bruto --> float --> B
Salidas
Sueldo neto --> float --> N
"""
#Entradas
B=float(input("Digite el salario bruto: "))
#Caja negra
if(B<900000):
    N=(B*0.15)+B
else:
    N=(B*0.12)+B
#Salidas
print(f"El salio neto es de: ${N} COP")