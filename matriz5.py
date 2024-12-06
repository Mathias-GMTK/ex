A = [
    [-7, 8],
    [4, 9],
    [2, 1]
]

At = []

for j in range(len(A[0])):
    linha = []
    for i in range(len(A)):
        linha.append(A[i][j])
    At.append(linha)

print("Matriz At (transposta de A):")
for linha in At:
    print(linha)