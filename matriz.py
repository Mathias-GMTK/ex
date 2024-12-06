matriz = []

for i in range(2):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("Matriz 2x4:")
for linha in matriz:
    print(linha)