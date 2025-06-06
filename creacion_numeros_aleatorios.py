import random #libreria para llamar y crear numeros random

numeros = []

for i in range(100): #ciclo para repartir 100 veces las interacciones
    n = random.randint(1,100) #crea el numero entre 1 y 100
    numeros.append(n) #guardamos en la lista al numero aleatorio

print(numeros) 

#contadore de numeros pares
cont = 0
for i in range(len(numeros)):
    if numeros[i]%2==0:
        cont+=1
print(f"canttidad de numeros pares : {cont}")