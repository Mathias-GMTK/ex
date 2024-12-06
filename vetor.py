A = []
for i in range(100):
    valor = float(input(f"Digite o valor {i+1}: "))
    A.append(valor)

soma = sum(A)

media = soma / len(A)

maior = max(A)
menor = min(A)

print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")