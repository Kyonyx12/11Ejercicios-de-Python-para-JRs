def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

palabras = []
for _ in range(5):
    palabra = input("Ingrese una palabra: ")
    palabras.append(palabra)

for palabra in palabras:
    if es_palindromo(palabra):
        print(f"{palabra} es palíndromo.")
    else:
        print(f"{palabra} no es palíndromo.")