frase = input("Digite uma frase: ")

frase_convertida = []

for char in frase:
    if char.islower():
        frase_convertida.append(char.upper())
    elif char.isupper():
        frase_convertida.append(char.lower())
    else:
        frase_convertida.append(char)

print(frase_convertida)