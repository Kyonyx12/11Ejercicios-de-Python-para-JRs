import random

def jugar_juego():
    opciones = ["piedra", "papel", "tijeras"]
    
    while True:
        jugador = input("Elige piedra, papel o tijeras (o 'salir' para terminar): ").lower()
        if jugador == "salir":
            break
        
        computadora = random.choice(opciones)
        
        if jugador not in opciones:
            print("Opción no válida. Por favor, elige entre piedra, papel o tijeras.")
            continue
        
        print(f"Jugador elige: {jugador}")
        print(f"Computadora elige: {computadora}")
        
        if jugador == computadora:
            print("¡Empate!")
        elif (
            (jugador == "piedra" and computadora == "tijeras") or
            (jugador == "papel" and computadora == "piedra") or
            (jugador == "tijeras" and computadora == "papel")
        ):
            print("¡Ganaste!")
        else:
            print("¡La computadora gana!")
            
jugar_juego()