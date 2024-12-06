matriculas = []

for i in range(100):
    while True:
        matricula = int(input(f"Digite o número de matrícula {i+1}: "))
        if matricula in matriculas:
            print("Número de matrícula já existe.")
        else:
            matriculas.append(matricula)
            break

print("Números de matrículas armazenados:", matriculas)