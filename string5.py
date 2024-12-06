a = input('Digite para transformar em leet: ')

leet = {
    "a": '4',
    "b": '6',
    "e": '3',
    "g": '9',
    "i": '1',
    "t": '7',
    "s": '5',
    "q": '9',
    "z": '2',
}

resultado = []

for i in a:
    if i.lower() in leet:
        resultado.append(leet[i.lower()])
    else:
        resultado.append(i)

print(resultado)