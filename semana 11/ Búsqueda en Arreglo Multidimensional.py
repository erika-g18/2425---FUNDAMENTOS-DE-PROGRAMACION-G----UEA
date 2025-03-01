#definir una matriz de 3*3
# fecha 28/02/2025
from typing import Any

matriz = [
    [4,5,9,7],
    [1,2,3,4],
    [9,8,7,6]
]

def buscar_valor(matriz,valor):
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j]==valor:
               return i,j
    return None

numero_buscar=9

resultado=buscar_valor(matriz, numero_buscar)

if resultado:
    print(f"El resultado del numero {numero_buscar} se encuentra en:({resultado})")

else:
    print(f"el numero no se encuentra en la matriz")