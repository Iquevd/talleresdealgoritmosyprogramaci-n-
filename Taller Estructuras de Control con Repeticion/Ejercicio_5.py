"""
No hay entradas
Salidas
número de términos para que un valor se aproxime a 1000 sin exceder
sumatoria --> suma
termino --> k
"""
suma=0
c=0#Contador
for k in range(1,1000):
    if(suma<=1000):
        suma=suma+((k**2)+1)/k
        if(suma<=1000):
            c=c+1
        else:
            break
print(c)