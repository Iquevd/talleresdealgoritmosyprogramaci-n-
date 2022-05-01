"""
Entradas
Cantidad de estudiantes --> int --> c
Salidas
Altura mayor de todas --> float --> a
"""
#Entradas
c=int(input("Digita la cantidad de estudiantes: "))
a=0
for i in range(1,c+1):
    altura=float(input("Digite  la altura: "))
    #Caja negra
    if(a<=altura):
        a=altura
        #Salidas
print(a)