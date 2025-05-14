import random

print("¡Bienvenido al juego 'Adivina el número'!")
print("Intenta adivinar un número entre 1 y 100.")

secret = random.randint(1, 100)  
attempt = 0 

while True:
    user_guess = input("Introduzca su número:") 
    attempt += 1
    if user_gess == secret:  # Nombre de variable incorrecto
        print("¡Felicitaciones, adivinaste el número!")
        break
    elif user_guess > secret:  
        print("Su número es mayor que el objetivo.")
    elif user_guess < secret:  
        print("Su número es inferior al objetivo.")