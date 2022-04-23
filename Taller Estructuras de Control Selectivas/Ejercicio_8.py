"""
Entradas
Datos --> int --> P,Q
Salidas
Expresión --> str --> E
"""
#Entradas
P,Q=input("Ingrese los valores P,Q: ").split(",")
P=int(P)
Q=int(Q)
#Caja negra y Salidas
E=P**3+Q**4-2*P**2
if(E>680):
    print(f"{P} y {Q} satisfacen la expresión")
else:
    print(f"{P} y {Q} no satisfacen la expresión")