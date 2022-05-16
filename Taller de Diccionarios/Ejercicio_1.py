"""
diccionario -- d
tamaño -- t
contador -- c
"""
lista=[12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64, 23] 
a=list(set(lista))
d={}
t=len(a)-1
while(t>=0):
    c=0
    for i in lista:
        if(a[t]==i):
            c=c+1
        d.update({a[t]:c})
    t=t-1
print(d)