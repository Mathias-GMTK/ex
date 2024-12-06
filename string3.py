codigo = input("Digite um código de cinco algarismos: ")

if len(codigo) != 5 or not codigo.isdigit():
    print("Deve conter 5 algarismos!")
else:
    A = int(codigo[0])
    B = int(codigo[1])
    C = int(codigo[2])
    D = int(codigo[3])
    E = int(codigo[4])

    S = 6 * A + 5 * B + 4 * C + 3 * D + 2 * E

    DigitoV = S % 7

    print("Dígito verificador:", S)