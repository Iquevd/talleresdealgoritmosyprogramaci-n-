#Entradas
chelines_austriacos=int(input("Digite la cantidad de chelines austriacos: "))
dracmas_griegos=int(input("Digite la cantidad de dracmas griegos: "))
pesetas=int(input("Digite la cantidad de pesetas: "))
#Caja negra
conversion1=chelines_austriacos*9568.71
conversion2=(dracmas_griegos*886.07)/20110
conversion3=pesetas*0.00000816
conversion4=pesetas/92.89
#Salidas
print("El equivalente de chelines a pesetas es:",conversion1) 
print("El equivalente de dracmas griegos a francos es:",conversion2) 
print("El equivalente de pesetas a dolares es:",conversion3) 
print("El equivalente de pesetas a liras italianas es:",conversion4) 