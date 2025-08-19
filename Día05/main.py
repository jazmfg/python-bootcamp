# Generador de contraseñas: 
# Pregunta al usuario cuántas letras, simbolos y números quiere en su contraseña

import string
import random

print("\nBienvenido al generador de PyPassword!\n")

letras = string.ascii_letters + "ñÑ"
numeros = string.digits
simbolos = string.punctuation

eleccion_letras = int(input("Cuántas letras quieres en tu contraseña: "))
eleccion_numeros = int(input("Cuántos números quieres en tu contraseña: "))
eleccion_simbolos = int(input("Cuántos simbolos quieres en tu contraseña: "))

contraseña = []

for _ in range(eleccion_letras):
    contraseña.append(random.choice(letras))

for _ in range(eleccion_simbolos):
    contraseña.append(random.choice(simbolos))

for _ in range(eleccion_numeros):
    contraseña.append(random.choice(numeros))

random.shuffle(contraseña)

contraseña_final = "".join(contraseña)
print(f"Tu contraseña generada es {contraseña_final}")