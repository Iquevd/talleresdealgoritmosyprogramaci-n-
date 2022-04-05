Algoritmo inicio_horas_y_minutos
	Escribir "Digite cantidad de minutos"
	Leer minutos//leemos la variable minutos
	horas<-trunc(minutos/60)//las horas de el total de minutos
	minutos2<-minutos MOD 60
	Escribir "Las horas son: " horas
	Escribir "Los minutos son: " minutos2
FinAlgoritmo
