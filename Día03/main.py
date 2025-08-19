# La Isla del Tesoro:

# - Estás en una encrucijada. ¿Adónde quieres ir? 'Izquierda' o 'Derecha' 
# - Si eliges la izquierda, llegas a un lago. Si eliges la derecha, caes en un agujero 
# - Si escribes 'esperar', esperas un bote. Si escribes 'nadar', cruzas nadando y te ataca una trucha 
# - Si esperas, llegas sano y salvo a la isla y encuentras una casa con tres puertas: roja, amarilla y azul. Elige una 
# - La puerta roja es una habitación llena de fuego, la amarilla es donde está el tesoro y la azul está llena de cocodrilos

print("\n¡Bienvenid@ a la isla del tesoro!\n")

eleccion1 = input("Te encuentras en una encrucijada hacia dónde deseas ir 'izquierda' o 'derecha':\n").lower()

if eleccion1 == "izquierda":
    print("Has llegado a un lago grande y profundo")
    
    eleccion2 = input("\n¿Quieres esperar un barco escribe 'esperar'? ¿Quieres cruzar nadando escribe 'nadar'?\n").lower()
    
    if eleccion2 == "esperar":
        print("Has llegado a la isla ileso")
        
        eleccion3 = input("\nEncuentras una casa con 3 puertas: 'roja', 'amarilla' y 'azul' elige una:\n").lower()
        
        if eleccion3 == "roja":
            print("Haz entrado a una habitación llena de fuego ¡Fin del juego!")
            
        elif eleccion3 == "amarilla":
            print("Haz encontrado el tesoro ¡Felicidades haz ganado!")
            
        elif eleccion3 == "azul":
            print("Haz entrado en una habitación llena de cocodrilos ¡Fin del juego!")
        
        else: 
            print("Solo puedes escoger una de las siguiente opciones: 'roja', 'amarilla', 'azul'")
        
    elif eleccion2 == "nadar":
        print("Te ha mordido una trucha ¡Fin del juego!")
        
    else:
        print("Solo puedes escribir 'nadar' o 'esperar'")
    
elif eleccion1 == "derecha":
    print("Haz caído a un agujero ¡Fin del juego!")
    
else:
    print("Solo puedes elegir 'izquierda' o 'derecha'")