"""
El sueldo de los vendedores -->  float --> S
Las ventas del departamento 1 -->  float --> V1
Las ventas del departamento 2 -->  float --> V2
Las ventas del departamento 3 -->  float --> V3
Salidas
El sueldo de los vendedores del departamento 1 --> float --> S1
El sueldo de los vendedores del departamento 2 --> float --> S2
El sueldo de los vendedores del departamento 3 --> float --> S3
"""
#Entradas
S=float(input(f"Ingrese el sueldo bruto de los vendedores: "))
V1=float(input(f"Ingrese el total de ventas del departamento 1: "))
V2=float(input(f"Ingrese el total de ventas del departamento 2: "))
V3=float(input(f"Ingrese el total de ventas del departamento 3: "))
#Caja negra
total=(V1+V2+V3)*0.33
if(V1>total):
    S1=S+S*0.20
else:
    S1=S
if(V2>total):
    S2=S+S*0.20 
else:
    S2=S    
if(V3>total):
    S3=S+S*0.20
else:
    S3=S
#Salidas
print(f"El sueldo neto de los vendedores del departamento 1 será de: ${S1}")
print(f"El sueldo neto de los vendedores del departamento 2 será de: ${S2}")
print(f"El sueldo neto de los vendedores del departamento 3 será de: ${S3}")