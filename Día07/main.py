# Ahorcado

# El usuario debe adivinar una palabra letra por letra
# Tiene un número limitado de intentos antes de perder
# Si acierta, la letra se muestra en su lugar
# Si se equivoca, pierde una vida

import random
from arte import etapas, logo
from palabras import lista_palabras

print(logo)

fin_del_juego = False
vidas = len(etapas) - 1

palabra_elegida = random.choice(lista_palabras)
longitud_palabra = len(palabra_elegida)

pantalla = ["_"] * longitud_palabra

while not fin_del_juego:
    intento = input("Adivina una letra: ").lower()

    if intento in pantalla:
        print(f"Ya habías adivinado la letra '{intento}'.")

    for posicion in range(longitud_palabra):
        letra = palabra_elegida[posicion]
        if letra == intento:
            pantalla[posicion] = letra

    print(f"{' '.join(pantalla)}")

    if intento not in palabra_elegida:
        print(f"\nLa letra '{intento}' no está en la palabra. ¡Pierdes una vida!")
        vidas -= 1
        if vidas == 0:
            fin_del_juego = True
            print("¡Perdiste!")
            print(f"La palabra era: {palabra_elegida}.")

    if "_" not in pantalla:
        fin_del_juego = True
        print("¡Ganaste!")

    print(etapas[vidas])