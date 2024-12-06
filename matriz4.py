A = [
    [2, -3],
    [-1, 4]
]

oposta_A = []

for i in range(len(A)):
    linha = []
    for j in range(len(A[i])):
        linha.append(-A[i][j])
    oposta_A.append(linha)

print("Matriz -A:")
for linha in oposta_A:
    print(linha)