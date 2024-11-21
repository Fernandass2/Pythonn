letra = input("Digite uma letra: ")

if letra in 'aeiouAEIOU':
    print("Vogal")
elif len(letra) == 1 and  letra.isalpha():
    print("Consoante")
else:
    print("Letra Inválida.")

