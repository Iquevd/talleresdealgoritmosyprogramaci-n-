#Entradas
x=int(input("Digite cantidad de naranjas compradas: "))
y=int(input("Digite el precio por una docena de naranjas: "))
k=int(input("Digite el precio por el cual se vendieron las naranjas: "))
#Caja negra
inversion=(x*y)/12
ganancia=(k-inversion)*100/inversion
#Salidas
print("El porcentaje de ganancia en la inversion es:",ganancia)