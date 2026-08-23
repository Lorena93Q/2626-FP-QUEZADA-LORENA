# Programa: Declaracion y recorrido de una matriz 3x3
# Arreglos Multidimensionales

def main():
    # Declaracion de una matriz de 3x3 con numeros enteros
    matriz = [
        [2, 4, 6],
        [1, 3, 5],
        [7, 8, 9]
    ]

    print("Valores de la matriz 3x3:\n")

    # Recorrido de la matriz utilizando ciclos anidados
    for i in range(3):
        for j in range(3):
            print(f"matriz[{i}][{j}] = {matriz[i][j]}")

    print("\nRepresentacion completa de la matriz:")
    for fila in matriz:
        print(fila)

