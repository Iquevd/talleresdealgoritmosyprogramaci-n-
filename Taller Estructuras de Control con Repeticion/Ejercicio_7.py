"""
Entradas
Multiplicador --> int --> m
XP --> int --> x
Salidas
Resultado de XP --> int --> r
"""
while True:
#Entradas
    datos=input()
    x,m=datos.split(" ")
    x=int(x)
    m=int(m)
    #Codicion de cierre
    if(x==0 and m==0):
        break
    #Caja negra
    r=x*m
    #Salidas
    print(r)