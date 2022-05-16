"""
usuarios -- u
intentos -- x
nombre -- n
apellido -- p
"""
u={ 
    "iperurena":{ 
        "nombre": "Iñaki", 
        "apellido": "Perurena", 
        "password": "123123" 
    }, 
    "fmuguruza": { 
        "nombre": "Fermín", 
        "apellido": "Muguruza", 
        "password": "654321" 
    }, 
    "aolaizola":{ 
        "nombre": "Aimar", 
        "apellido": "Olaizola", 
        "password": "123456" 
    } } 
x=1
for i in u:
    a=input("Usuario: ")
    b=input("Contraseña: ")
    if a in u and b==u[a]["password"]:
        n=u[a]["nombre"]
        p=u[a]["apellido"]
        print(n,p)
        break
    else:
        print("Intento Fallido",x)
        x=x+1