Notas = [9.9, 9.7, 9.8, 10, 10]

nota_max = max(Notas)
nota_min = min(Notas)

Notas.remove(nota_max)
Notas.remove(nota_min)

media_final = sum(Notas) / len(Notas)

print(media_final)