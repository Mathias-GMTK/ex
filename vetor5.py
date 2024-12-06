A = [2, 4, 7, 13, 14, 15, 16]
B = [1, 6, 7, 11, 13, 16, 18]

uniao = []

for i in range(len(A)):
    uniao.append(A[i])

for elem in B:
    if elem not in uniao:
        uniao.append(elem)

interseccao = []

for elem in A:
    if elem in B:
        interseccao.append(elem)

diferenca = []

for elem in A:
    if elem not in B:
        diferenca.append(elem)
for elem in B:
    if elem not in A:
        diferenca.append(elem)

print("União:", sorted(uniao))
print("Intersecção:", sorted(interseccao))
print("Diferença:", sorted(diferenca))