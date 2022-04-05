Algoritmo inicio_calificacion_final
	Escribir "Ingrese primera calificación"
	Leer a
	Escribir "Ingrese segunda calificación"
	Leer b
	Escribir "Ingrese tercera calificación"
	Leer c
	Escribir "Ingrese calificación examen final"
	Leer d
	Escribir "Ingrese calificación trabajo final"
	Leer e
	promedio<-(a+b+c)/3
	porcentaje_parcial<-promedio*0.55
	porcentaje_examen_final<-d*0.30
	porcentaje_trabajo_final<-e*0.15
	calificacion_final<-porcentaje_parcial+porcentaje_examen_final+porcentaje_trabajo_final
	Escribir "La calificación final es: " calificacion_final
FinAlgoritmo
