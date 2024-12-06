A = [
    [2, 3, 1],
    [-1, 0, 2]
]

B = [
    [1, -2],
    [0, 5],
    [4, 1]
]

if len(A[0]) != len(B):
    print("As matrizes não podem ser multiplicadas.")
else:
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]

    print("Matriz A x B:")
    for linha in C:
        print(linha)