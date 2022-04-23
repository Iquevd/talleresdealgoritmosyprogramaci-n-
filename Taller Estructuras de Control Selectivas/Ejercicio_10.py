"""
Entradas
Sueldo bruto --> float --> B
Salidas
Categoria --> int --> C
Sueldo neto --> float --> N
"""
# Entradas
B=int(input("Digite el salario bruto: "))
# Caja Negra
if(B>5000000):
    N=B+B*0.10
    C=1
elif(B>4300000 and B<=5000000):
    N=B+B*0.15
    C=2
elif(B>3600000 and B<=4300000):
    N=B+B*0.20
    C=3
elif(B>2000000 and B<=3600000):
    N=B+B*0.40
    C=4
elif(B>900000 and B<=2000000):
    N=B+B*0.60
    C=5
else:
    N="No existe ese sueldo"
    C="No existe una categoria con ese sueldo"
#Salidas
print(f"Su salario neto corresponde a la categoría {C}, y es de: ${N} COP")