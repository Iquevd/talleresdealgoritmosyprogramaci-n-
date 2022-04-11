#Entradas
#Matematicas
examen_m=float(input("Ingrese calificación del examen de Matematicas: "))
tarea1_m=float(input("Ingrese calificación de la tarea 1: "))
tarea2_m=float(input("Ingrese calificación de la tarea 2: "))
tarea3_m=float(input("Ingrese calificación de la tarea 3: "))
#Física
examen_f=float(input("Ingrese calificación del examen de Física: "))
tarea1_f=float(input("Ingrese calificación de la tarea 1: "))
tarea2_f=float(input("Ingrese calificación de la tarea 2: "))
#Química
examen_q=float(input("Ingrese calificación del examen de Química: "))
tarea1_q=float(input("Ingrese calificación de la tarea 1: "))
tarea2_q=float(input("Ingrese calificación de la tarea 2: "))
tarea3_q=float(input("Ingrese calificación de la tarea 3: "))
#Caja negra
promedio_m=examen_m*0.90+((tarea1_m+tarea2_m+tarea3_m)/3)*0.10
promedio_f=examen_f*0.80+((tarea1_f+tarea2_f)/2)*0.20
promedio_q=examen_q*0.85+((tarea1_q+tarea2_q+tarea3_q)/3)*0.15
promedio_general=(promedio_m+promedio_f+promedio_q)/3
#Salidas
print(f"El promedio general es: {promedio_general}")