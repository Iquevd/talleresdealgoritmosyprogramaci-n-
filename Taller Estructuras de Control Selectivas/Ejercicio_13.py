"""
Entradas
Fecha actual del sistema --> X
Fecha de nacimiento --> formato año/mes/dia --> F
--> año nacimiento --> A
--> mes nacimiento --> M
--> dia nacimiento --> D
Salidas
Edad --> E
Signo --> S
"""
#Entradas
from datetime import datetime
X=datetime.now()
año_actual=X.year
mes_actual=X.month
dia_actual=X.day
F=input("Digite fecha de nacimiento año/mes/dia: ")
año_nacimiento,mes_nacimiento,dia_nacimiento=F.split("/")
A=int(año_nacimiento)
M=int(mes_nacimiento)
D=int(dia_nacimiento)
#Caja negra
E=año_actual-A
if M==11 and D>=22 or M==12 and D<=21:
    S="Sagitario"
elif M==12 and D>=22 or M==1 and D<=20:
    S="Capricornio"
elif M==1 and D>=21 or M==2 and D<=19:
    s="Acuario"
elif M==2 and D>=20 or M==3 and D<=19:
    S="Piscis"
elif M==3 and D>=21 or M==4 and D<=20:
    S="Aries"
elif M==4 and D>=21 or M==5 and D<=21:
    S="Tauro"
elif M==5 and D>=22 or M==6 and D<=21:
    S="Geminis"
elif M==6 and D>=22 or M==7 and D<=22:
    S="Cancer"
elif M==7 and D>=23 or M==8 and D<=23:
    S="Leo"
elif M==8 and D>=24 or M==9 and D<=22:
    S="Virgo"
elif M==9 and D>=23 or M==10 and D<=22:
    S="Libra"
elif M==10 and D>=23 or M==11 and D<=21:
    S="Escorpion"
#Salidas
print(f"Su signo Zodiacal es: {S}")
print(f"Su edad es: {E}")