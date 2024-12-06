frase = input("Digite uma frase: ")

space = 0
vogais = 0

for i in frase:
    if i in "aeiouAEIOU":
        vogais += 1
    elif i == " ":
        space += 1

print(f"Total de espaco: {space} Total de vogais: {vogais}")