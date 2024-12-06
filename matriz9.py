matriz_tempos = [
    [0, 2, 11, 6, 15, 11, 1],
    [2, 0, 7, 12, 4, 2, 15],
    [11, 7, 0, 11, 8, 3, 13],
    [6, 12, 11, 0, 10, 2, 1],
    [15, 4, 8, 10, 0, 5, 13],
    [11, 2, 3, 2, 5, 0, 14],
    [1, 15, 13, 1, 13, 14, 0]
]

def tempo_entre_cidades(cidade1, cidade2):
    return matriz_tempos[cidade1-1][cidade2-1]

def tempo_total_trajeto(rota):
    tempo_total = 0
    for i in range(len(rota) - 1):
        tempo_total += tempo_entre_cidades(rota[i], rota[i+1])
    return tempo_total

cidade1 = int(input("Informe a primeira cidade (1-7): "))
cidade2 = int(input("Informe a segunda cidade (1-7): "))
print(f"Tempo necessário para percorrer da cidade {cidade1} para a cidade {cidade2}: {tempo_entre_cidades(cidade1, cidade2)}")

rota = []
while True:
    cidade = int(input("Informe uma cidade para adicionar à rota (0 para terminar): "))
    if cidade == 0:
        break
    rota.append(cidade)

if len(rota) > 1:
    print(f"Tempo total para cumprir o trajeto fornecido: {tempo_total_trajeto(rota)}")
else:
    print("Rota inválida. É necessário informar pelo menos duas cidades.")