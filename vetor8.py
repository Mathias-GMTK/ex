N = int(input("Digite o número de elementos do vetor: "))

vetor_original = []
for i in range(N):
    valor = int(input(f"Digite o valor {i+1}: "))
    vetor_original.append(valor)

pares = []
impares = []

for valor in vetor_original:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print("Valores pares:", pares)
print("Valores ímpares:", impares)