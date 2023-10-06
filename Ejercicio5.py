entrada = input("Ingrese el significado completo: ")
palabras = entrada.split()
acrónimo = "".join(word[0].upper() for word in palabras)
print("Salida:", acrónimo)