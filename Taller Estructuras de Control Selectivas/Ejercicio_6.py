"""
Entradas
N digitos --> str --> A,B,C,D
Salidas
Resultado redondeado --> int --> N
"""
#Entradas
A,B,C,D= input(f"Digite los números A,B,C,D que forman N: ").split(",")
A=str(A)
B=str(B)
C=str(C)
D=str(D)
#Caja negra
N=A+B+C+D  #Suma de los Str para generar el número N
N=int(N)  #Transformación de N a un número de tipo Int
if(N<=(int(A)*1000+int(B)*100+50)):
    N=N-int(C+D)
elif(N>(int(A)*1000+int(B)*100+50)):
    N=(N-int(C+D))+100
#Salidas
print(f"El resultado redondeado es: {N}")