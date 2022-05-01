"""
Entradas
Contraseña --> int --> c
Salidas
Si es correcta --> str --> Acesso Permitido
Si es incorrecta --> str --> Senha Invalida
"""
# Entrada
c=int(input())
# Caja negra
while (c!=2002):
    print("Senha Invalida")#Salida
    c=int(input())
#Salida
print("Acesso Permitido")