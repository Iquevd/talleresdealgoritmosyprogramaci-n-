#Entradas
mujeres=int(input("Digite cantidad de mujeres: "))
hombres=int(input("Digite cantidad de hombres: "))
#Caja negra
total_estudiantes=mujeres+hombres#int
mp=(mujeres*100)/total_estudiantes#float
hp=(hombres*100)/total_estudiantes#floar
#Salidas
print(f"El procentaje de mujeres es: {round (mp,2)} y el porcentaje de hombres es: {round (hp,2)}")#str