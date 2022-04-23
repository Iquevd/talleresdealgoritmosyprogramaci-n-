"""
Entradas
Datos --> int --> A,B,C,D
Salidas
Resultado --> expresión 1: int -y expresión 2: float --> R
"""
# Entradas
A,B,C,D=input(f"Digite los números A,B,C,D: ").split(",")
A=int(A)
B=int(B)
C=int(C)
D=int(D)
# Caja Negra
if(D==0):
    R=(A-C)**2
elif(D>0):
    R=((A-B)**3)/D
# Salidas
print(f"El resultado es: {R}")