Algoritmo inicio_la_media
	Escribir "Ingrese el primer n�mero"
	Leer a
	Escribir "Ingrese el segundo n�mero"
	Leer b
	Escribir "Ingrese el tercer n�mero"
	Leer c
	Si(a<>b y a<>c y b<>c) Entonces
		Si(a>b y a<c o a>c y a<b) Entonces
			Escribir "1. La media es: ",a
		SiNo
			Si(b>a y b<c o b<a y b>c) Entonces
				Escribir "2. La media es: ",b
			SiNo
				Escribir "3. La media es: ",c
			FinSi
		FinSi
	SiNo
		Escribir "Los n�meros no son diferentes"
	FinSi
FinAlgoritmo
