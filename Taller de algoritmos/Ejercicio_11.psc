Algoritmo inicio_calificacion_final
	Escribir "Ingrese primera calificaci�n"
	Leer a
	Escribir "Ingrese segunda calificaci�n"
	Leer b
	Escribir "Ingrese tercera calificaci�n"
	Leer c
	Escribir "Ingrese calificaci�n examen final"
	Leer d
	Escribir "Ingrese calificaci�n trabajo final"
	Leer e
	promedio<-(a+b+c)/3
	porcentaje_parcial<-promedio*0.55
	porcentaje_examen_final<-d*0.30
	porcentaje_trabajo_final<-e*0.15
	calificacion_final<-porcentaje_parcial+porcentaje_examen_final+porcentaje_trabajo_final
	Escribir "La calificaci�n final es: " calificacion_final
FinAlgoritmo
