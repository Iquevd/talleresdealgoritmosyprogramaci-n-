"""
Entradas
Consume licor --> int --> L
Licor preferido --> int--> P
Edad --> int --> E
Sexo--> str --> S
Continuar --> str --> C
Salidas
Personas encuestadas que consumen licor --> str --> A
Mujeres menores de edad --> int --> B
Hombres que no consumen aguardiente entre 20 y 25 años --> int --> C
Promedio de edad de las personas que consumen cerveza --> float --> D
Porcentaje de quienes consumen whisky --> float --> F
"""
A=0
B=0
C=0
D=[]
W=[]#Whisky
G=0
T=[]#Total
#Entradas y Caja negra
while True:
    L=int(input("¿Consume licor?\nDigite 0-Si y 1-No "))  
    if (L==0):
        A=A+1
        P=int(input("Licor preferido:\nDigite 1-Aguardiante, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky o 6-Otro ")) 
        E=int(input("Edad: "))  
        if (P==3):
            D.append(E)
        elif (P==5):
            W.append(P)
        S=int(input("Sexo:\nDigite 0-Mujer y 1-Hombre "))  
        if (S==1 and P!=1 and E>=20 and E<=25):
            C+=1
    elif (L==1): 
        P=0
        E=int(input("Edad: ")) 
        S=int(input("Sexo:\nDigite 0-Mujer y 1-Hombre "))  
        if (S==1 and E>=20 and E<=25):
            C+=1  
    T.append(L)
    if (E<18 and S==0):
        B=B+1 
    C=int(input("¿Desea continuar con la investigacion?\nDigite 0-Si y 1-No "))  
    if (C==1):
        break
for x in range(len(W)):
    if W[x]==5: 
            G+=1
F=(G*100)/len(T)
#salidas
print(f"Las personas encuestadas que consumen licor son: {A}")
print(f"Las mujeres menores de edad son: {B}")  
print(f"Los hombres que no consumen aguardiente y tienen entre 20 y 25 años son: {C}")
if (D):
    print(sum(D)/len(D),"es el promedio de edad de quienes consumen cerveza.")
else:
    print("no hay promedio de edad de quienes consumen cerveza, es 0.")
print(f"Consumen whisky en relación con el total encuestados el: {F}%") 