#Entradas
c1=float(input("Ingrese la primera calificación: "))
c2=float(input("Ingrese la segunda calificación: "))
c3=float(input("Ingrese la tercera calificación: "))
ef=float(input("Ingrese la calificación del examen final: "))
tf=float(input("Ingrese la calificación del trabajo final: "))
#Caja negra
promedio=(c1+c2+c3)/3
p_parcial=promedio*0.55
p_ef=ef*0.30
p_tf=tf*0.15
calificacion=p_parcial+p_ef+p_tf
#Salidas
print("La calificación final es:",calificacion)