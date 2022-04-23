"""
Edad --> int --> E
Sexo --> str --> S
Nivel de hemoglobina --> float --> N
Salidas
Resultados de anemia --> str --> R
"""
# Entradas
E=int(input("Ingrese la edad en meses: "))
N=float(input("Digite el nivel de hemoglobina en g%: "))
if(E>180):
    S=str(input("¿Cuál es su sexo? (Hombre:1 o Mujer:2) "))
else:
    S=0
S=int(S)
#Caja negra
if(E>=0 and E<=1):
    if(N>=13 and N<=26):
        R="Negativo"
    elif(N<13):
        R="Positivo"
    else:
        (N>26)
        R="Error"
elif(E>1 and E<=6):
    if(N>=10 and N<=18):
        R="Negativo"
    elif(N<10):
        R="Positivo"
    else:
        (N>18)
        R="Error"
elif(E>6 and E<=12):
    if(N>=11 and N<=15):
        R="Negativo"
    elif(N<11):
        R="Positivo"
    else:
        (N>15)
        R_="Error"
elif(E>12 and E<=60):
    if(N>=11.5 and N<=15):
        R="Negativo"
    elif(N<11.5):
        R="Positivo"
    else:
        (N>15)
        R="Error"
elif(E>60 and E<=120):
    if(N>=12.6 and N<=15.5):
        R="Negativo"
    elif(N<12.6):
        R="Positivo"
    else:
        (N>15.5)
        R="Error"
elif(E>120 and E<=180):
    if(N>=13 and N<=15.5):
        R="Negativo"
    elif(N<13):
        R="Positivo"
    else:
        (N>15.5)
        R="Error"
elif(E>180 and S==2):
    if(N>=12 and N<=16):
        R="Negativo"
    elif(N<12):
        R="Positivo"
    else:
        (N>16)
        R="Error"
elif(E>180 and S==1):
    if(N>=14 and N<=18):
        R="Negativo"
    elif(N<14):
        R="Positivo"
    else:
        (N>18)
        R="Error"
# Salidas
print(f"Su diagnostico para anemia es: {R}")