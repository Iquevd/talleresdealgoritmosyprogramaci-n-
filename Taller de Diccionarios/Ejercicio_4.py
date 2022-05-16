"""
estudiantes -- e
total -- t
suspendidos -- s
aprobados -- p
media -- m
notas -- n
nombre -- x
"""
e={ 
    "1":{ 
        "nombre":"Lorea", 
        "nota":8 
 }, 
    "2":{ 
        "nombre":"Markel", 
        "nota":4.2 
 }, 
    "3":{ 
        "nombre":"Julen", 
        "nota":6.5 
 } } 
t=3
for i in range(0,10):
    a=input("Nombre del estudiante: ")
    b=float(input("Nota: "))
    t=t+1
    e.update({f"{t}":{"nombre":a, "nota":b}})
s=[]
p=[]
m=[]
for j in e:
    x=e[j]["nombre"]
    n=e[j]["nota"]
    if n<6:
        s.append(x)
    else:
        p.append(x)
    m.append(n)
print("Los estudiantes suspendidos son: ",", ".join(s))
print("Los estudiantes aprobados son: ",", ".join(p))
print("La media es de: ",round(sum(m)/len(m),2))