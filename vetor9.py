N = int(input("Digite o número de elementos do vetor A: "))
M = int(input("Digite o número de elementos do vetor B: "))

A = []
B = []

print("Digite os elementos do vetor A em ordem crescente:")
for i in range(N):
    valor = int(input(f"A[{i}]: "))
    A.append(valor)

print("Digite os elementos do vetor B em ordem crescente:")
for i in range(M):
    valor = int(input(f"B[{i}]: "))
    B.append(valor)

C = []

i, j = 0, 0

while i < N and j < M:
    if A[i] < B[j]:
        C.append(A[i])
        i += 1
    else:
        C.append(B[j])
        j += 1

while i < N:
    C.append(A[i])
    i += 1

while j < M:
    C.append(B[j])
    j += 1

print(C)