import random

numero_oculto = random.randint(1, 50)
intentos = 0

while True:
    intento = int(input("Adivina el número oculto (entre 1 y 50): "))
    intentos += 1

    if intento < 1 or intento > 50:
        print("Error: Ingresa un número dentro del rango válido.")
    elif intento < numero_oculto:
        print("El número oculto es mayor. Intenta de nuevo.")
    elif intento > numero_oculto:
        print("El número oculto es menor. Intenta de nuevo.")
    else:
        print(f"¡Enhorabuena! Has adivinado el número oculto {numero_oculto} en {intentos} intentos.")
        break