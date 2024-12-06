N = int(input("Informe o tamanho da ordem da matriz identidade: "))

matriz_identidade = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    matriz_identidade[i][i] = 1

print("Matriz identidade de ordem", N)
for linha in matriz_identidade:
    print(linha)