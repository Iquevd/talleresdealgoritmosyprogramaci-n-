"""
Entradas
Numero 1 --> int --> a
Numero 2 --> int --> b
Salidas
Division --> float --> d
Cociente --> float --> c
Resto --> int --> r
"""
#Entradas y Salidas
a=int(input("Digite el primer número (Dividendo): "))
b=int(input("Digite el Segundo número (Divisor): "))
#Caja negra
d=int(a/b)
c=0
for i in range(d):
    print(f"{a}-{b}={a-b}")
    a=a-b
    c=c+1
print(f"El resto de la division es: {a} y el cociente es: {c}")