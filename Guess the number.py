'''
Este programa es una simple implementacion del juego guess the number en Python 3.3.2, donde la PC tomara el papel
de estar generando un numero aleatorio en un cierto rango predefinido y estara pidiendo que el jugador
adivine el numero y mostrando mensajes dependiendo si el numero proporcionado por el jugador es
menor, mayor o correcto, claro que para poder ganar tiene que lograrlo en el numero de intentos
predefinidos el cual fue calculado en base al algoritmo de busqueda binaria.

Guess the number
Created by: Jassael Ruiz
Version: 1.0
'''

import random as r
import sys
sys.path.append("..")
import simplegui as sg
import math

# initialize global variables
secret_number = 0
low_range = 0
high_range = 100
remaining_guesses = int(math.ceil(math.log(high_range, 2)))
guess_number = 0

# helper function to start and restart the game
def new_game():
    global secret_number, remaining_guesses
    secret_number = r.randint(low_range, high_range - 1)
    remaining_guesses = int(math.ceil(math.log(high_range, 2)))
    print("New game.", "Range is from "+str(low_range)+" to "+str(high_range))
    print("Number of remaining guesses is "+str(remaining_guesses))
    print("")

# event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global low_range, high_range, remaining_guesses
    low_range = 0
    high_range = 100
    remaining_guesses = int(math.ceil(math.log(high_range, 2)))
    new_game()   

def range1000():
    # button that changes range to range [0,1000) and restarts
    global low_range, high_range, remaining_guesses
    low_range = 0
    high_range = 1000
    remaining_guesses = int(math.ceil(math.log(high_range, 2)))
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global guess_number, secret_number, remaining_guesses
    isNumber = True
    remaining_guesses -= 1
    
    try:
        guess_number = int(guess)
    except:
        print("Invalid input!, try again please")
        isNumber = False

    if(remaining_guesses > 0):
        if(isNumber):
            print("Guess was: "+guess)
            print("Number of remaining guesses is: "+str(remaining_guesses))
            if(guess_number == secret_number):
                print("Correct!. You win\n")
                new_game()
            elif(secret_number < guess_number):
                print("Lower!\n")
            else:
                print("Higher!\n")
    else:
        game_over()
        
def game_over():
    print("You Lose. You do not have more remaining guesses\n")
    new_game()
    
       
# create frame
f = sg.create_frame("Guess the number!!", 200, 200)

# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 100)
f.add_button("Range is [0, 1000)", range1000, 100)
g = f.add_input("Guess number", input_guess, 100)
g.set_text(0)

# call new_game and start frame
new_game()
f.start()
