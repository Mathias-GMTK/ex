V1 = [3,5,6,7,1,12,10,32,12,5,64,1,2,6,7]
V2 = [6,12,4,6,6,7,4,32,12,5,6,4,4,2,1]

contador = 0
for i in range(15):
    if V1[i] == V2[i]:
        contador += 1

print(f"Quantidade de vezes que V1 e V2 possuem os mesmos números nas mesmas posições: {contador}")