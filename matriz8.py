matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def rotacionar_90(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0])-1, -1, -1)]

def rotacionar_180(matriz):
    return [linha[::-1] for linha in matriz[::-1]]

def rotacionar_270(matriz):
    return [[matriz[j][i] for j in range(len(matriz)-1, -1, -1)] for i in range(len(matriz[0]))]

matriz_90 = rotacionar_90(matriz)
matriz_180 = rotacionar_180(matriz)
matriz_270 = rotacionar_270(matriz)

print("Matriz rotacionada em 90°:")
for linha in matriz_90:
    print(linha)

print("\nMatriz rotacionada em 180°:")
for linha in matriz_180:
    print(linha)

for linha in matriz_270:
    print(linha)