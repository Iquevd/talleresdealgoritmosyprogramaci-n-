"""
No hay entradas
Salidas
Numeros impares<100 (no multiplos de 7) --> int --> i
"""
#Caja negra y Salidas
for i in range(1,101,2):
    if(i%7==0):
        continue
print(i)