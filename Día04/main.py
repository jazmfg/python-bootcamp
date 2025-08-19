# Piedra, Papel, Tijera 

import random

piedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

tijeras = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

dibujo = {
    "piedra": piedra,
    "papel": papel,
    "tijera": tijeras
}

opciones = ["piedra", "papel", "tijera"]

usuario = input("\nElige una opción: piedra, papel o tijera: ").lower()

if usuario not in opciones:
    print("Por favor elige piedra, papel o tijera")
else:
    computadora = random.choice(opciones)
    
    print(f"\nComputadora eligió: {computadora}")
    print(dibujo[computadora])

    print(f"\nTú elegiste: {usuario}")
    print(dibujo[usuario])

    if computadora == usuario:
        print("¡Empate!")
    elif (
        (computadora == "piedra" and usuario == "tijera") or
        (computadora == "papel" and usuario == "piedra") or
        (computadora == "tijera" and usuario == "papel")
    ):
        print("¡Gana la computadora!")
    else:
        print("¡Tú ganas!")