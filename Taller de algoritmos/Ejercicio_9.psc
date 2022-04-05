Algoritmo inicio_sueldo_base_y_comisiones
	Escribir "Digite su sueldo base"
	Leer sb
	Escribir "Digite valor de la primera venta"
	Leer venta1
	Escribir "Digite valor de la segunda venta"
	Leer venta2
	Escribir "Digite valor de la tercera venta"
	Leer venta3
	total_ventas<-venta1+venta2+venta3
	comisiones<-total_ventas*0.10
	total_a_pagar<-sb+comisiones
	Escribir "Su sueldo es: " sb
	Escribir "El total a pagar es: " total_a_pagar
FinAlgoritmo
