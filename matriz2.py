matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

soma_primeira_coluna = sum(linha[0] for linha in matriz)

produto_primeira_linha = 1
for valor in matriz[0]:
    produto_primeira_linha *= valor

soma_total = sum(sum(linha) for linha in matriz)

produto_diagonal_principal = 1
for i in range(len(matriz)):
    produto_diagonal_principal *= matriz[i][i]

print(f"Soma dos elementos da primeira coluna: {soma_primeira_coluna}")
print(f"Produto dos elementos da primeira linha: {produto_primeira_linha}")
print(f"Soma de todos os elementos: {soma_total}")
print(f"Produto da diagonal principal: {produto_diagonal_principal}")