nome = input("Digite um nome: ")

conectores = {"e", "do", "da", "dos", "das", "de", "di", "du"}

palavras = nome.split()

iniciais = []

for palavra in palavras:
    if palavra.lower() not in conectores:
        iniciais.append(palavra[0].upper())

print(iniciais)