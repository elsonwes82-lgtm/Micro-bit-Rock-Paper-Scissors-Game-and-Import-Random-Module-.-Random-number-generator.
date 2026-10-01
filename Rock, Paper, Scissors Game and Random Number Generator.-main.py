# Imports go at the top
from microbit import *
import random
#Random number shake device
#shake = random
#random.choice = []

rock = Image("00000:09990:09990:09990:00000")                      
paper = Image("99999:90009:90009:90009:99999")                        
scissors = Image.SCISSORS

choices = [rock, paper, scissors]
'''
while True:                                  #Project Random
    if accelerometer.was_gesture("shake"):
        display.show(random.randint(1,6))'''
        
while True:                                  #Project Rock, Paper, Scissors 
    if accelerometer.was_gesture("shake"):
        display.show(random.choice(choices))
    
#First install battery and next send the program to micro:bit.
#To play count to 3 and on 3 shake the device to reveal the result "Rock, Paper, Scissors".
#If the opponent doesnt have a microbit they use their hand.
#First to 5 wins the game.
#Reset button can be used to clear screen.
