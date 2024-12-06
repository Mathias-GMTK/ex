vetor = [1,5,9,0,3,7,2,8,6,4,11,15,19,20,25,30,35,40,45,50]
print("Vetor original:", vetor)

for i in range(10):
    vetor[i], vetor[19 - i] = vetor[19 - i], vetor[i]

print("Vetor modificado:", vetor)