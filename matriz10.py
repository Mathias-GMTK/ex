n = int(input("Informe a ordem do triângulo de Pascal: "))

triangulo = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    triangulo[i][0] = 1
    triangulo[i][i] = 1

for i in range(2, n):
    for j in range(1, i):
        triangulo[i][j] = triangulo[i-1][j-1] + triangulo[i-1][j]

print("Triângulo de Pascal de ordem", n)
for i in range(n):
    for j in range(i + 1):
        print(triangulo[i][j], end="\t")
    print()