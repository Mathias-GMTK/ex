n = input("Digite um numero: ")

digit = {
    '0': 'zero',
    '1': 'um',
    '2': 'dois',
    '3': 'três',
    '4': 'quatro',
    '5': 'cinco',
    '6': 'seis',
    '7': 'sete',
    '8': 'oito',
    '9': 'nove'
}

resultado = []

for i in n:
    resultado.append(digit[i])

print(resultado)