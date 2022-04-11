#Entradas
n1=int(input("Ingrese la cantida de billetes de 50000: "))
n2=int(input("Ingrese la cantida de billetes de 20000: "))
n3=int(input("Ingrese la cantida de billetes de 10000: "))
n4=int(input("Ingrese la cantida de billetes de 5000: "))
n5=int(input("Ingrese la cantida de billetes de 2000: "))
n6=int(input("Ingrese la cantida de billetes de 1000: "))
n7=int(input("Ingrese la cantida de billetes de 500: "))
n8=int(input("Ingrese la cantida de billetes de 100: "))
#Caja negra
c1=n1*50000
c2=n2*20000
c3=n3*10000
c4=n4*5000
c5=n5*2000
c6=n6*1000
c7=n7*500
c8=n8*100
cantidad_total=c1+c2+c3+c4+c5+c6+c7+c8
#Salidas
print("El dinero total es:",cantidad_total)