string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()

if sorted(string1) == sorted(string2):
    print("As strings são anagramas.")
else:
    print("As strings não são anagramas.")