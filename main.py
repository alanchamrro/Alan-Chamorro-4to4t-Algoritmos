import random


palabras = ["perro", "gato", "casa", "python", "escuela", "teclado", "monitor", "futbol", "musica", "robot"]


palabra = random.choice(palabras)
adivinada = ["_"] * len(palabra)
intentos = 7

print(" juego del ahorcado ")

while intentos > 0 and "_" in adivinada:
    print(" ".join(adivinada))
    print(f"Intentos restantes: {intentos}")

    letra = input("adivina una letra: ")

    if letra in palabra:
        for x in range(len(palabra)):
            if palabra[x] == letra:
                adivinada[x] = letra
    else:
        intentos -= 1


if "_" not in adivinada:
    print(f"ganaste la palabra era: {palabra}")
else:
    print(f"perdiste. La palabra era: {palabra}")