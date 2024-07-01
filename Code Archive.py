# begening
def name():
    name = input()
    if name.upper() == "GOD" or name.upper() == "DEALER":
        print("Contract already exists, write YOUR name:")
        name()
    else:
        print("General Release of Liability signed, no turning back: "+name.upper())
    print("")

def intro():
    print("\n \" You walk forward towards the door, you kick it open and exit. \" ")
    print("* DEALER: \"Please sign the waiver.\"")
    name()
    print("")

def begin():
	print("\n \" You open your eyes and look around. You are standing in the middle of a public bathroom just by the sinks. The tiled floors you're standing on are jagged, with some tiles detached, some broken, and some missing. The walls are also tiled, grey and almost yellow, with what you assume to be soot dripping from the gaps between the tiles. The mirror above the sinks are as large as a thin bed sheet. You cannot make out your appearance from how covered the mirror is in dark grease spots which give it a course sandpaper look. In the top right corner of the mirror, large black letters stand apart, spelling out: 'A F R A I D'. Grease is also dripping from the top frame, for good measure. An orange pill bottle is resting beside one of the sinks. Infront of you is a door. \" \n")
	print("Options: \n", "    > door \n")
	choice = input("select: ")
    if choice == "door":
        intro()
    print("")

def menu():
    print("Buckshot Roulette: Python Text Adventure Edition \n")
    print("Options: \n", "    > play \n", "    > about \n")
    choice = input("select: ")
    if choice == "play":
        begin()
    elif choice == "about":
        print("Felt like flexing my pre-college coding skills lol \n\n")
        menu()
    print("")
        
menu()



'''import random
import Damage
import DealerAI
import Item_Randomizer
import Player_Turn
import Shell_Randomizer'''

from BuckshotRoulettFunc import Game_Round
from BuckshotRoulettFunc import Item_Randomizer
from BuckshotRoulettFunc import Shell_Randomizer

Game_Round(["live", "live"], 0, 0, 2, 2, 2, 2, 2, False, False, False)
#["live", "live", "live", "live"]
#["live", "blank", "live", "blank"]'


'''import os
import time
 

print("ooooooooooooo")
print("ooooooooooooo")
print("ooooooooooooo")
time.sleep(3)

os.system("cls")

print("wwwwwwwwwwwww")
print("wwwwwwwwwwwww")
print("wwwwwwwwwwwww")'''