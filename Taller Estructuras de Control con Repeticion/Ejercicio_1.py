"""
Entradas
N y K --> int --> N,K
Salidas
Números de enteros desde N hasta K --> int --> N
"""
#Entradas
N,K=input("Digite los numeros N,K: ").split(",")
N=int(N)
K=int(K)
#Caja negra y Salidas
if K<N:
    while K<=N:
        print(N)
        N=N-1
else:
    print("Intenta que el primero sea mayor que el segundo ")