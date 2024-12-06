seq1 = input("Digite a primeira sequência de números: ")
seq2 = input("Digite a segunda sequência de números: ")

num1 = [int(digito) for digito in seq1]
num2 = [int(digito) for digito in seq2]

while len(num1) < len(num2):
    num1.insert(0, 0)
while len(num2) < len(num1):
    num2.insert(0, 0)

resultado = []
pivo = 0

for i in range(len(num1) - 1, -1, -1):
    total = num1[i] + num2[i] + pivo
    pivo = total // 10
    resultado.insert(0, total % 10)

if pivo > 0:
    resultado.insert(0, pivo)

print("Sequência resultante da soma:", resultado)