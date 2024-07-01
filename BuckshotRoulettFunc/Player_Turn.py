import time
import os

import Shooting


#Settings = [ShellOrder0, blank1, live2, MaxHealth3, PlayerHealth4, DealerHealth5, PlayerLast6, DealerLast7, MaxItem8, PlayerItems9, DealerItems10]


def Player_Turn(Settings):
    time.sleep(4)
    '''if Settings[0] == []:
        Settings[0] = 0
        Item_Randomizer.Item_Randomizer(Settings)'''
    print("")
    print(Settings[0])
    print("             Player's health:", "⚡︎" * Settings[6] + "🗲 " * Settings[4])
    print("             DEALER's health:", "⚡︎" * Settings[7] + "🗲 " * Settings[5])
    print("Options:")
    print("     a> Shoot DEALER")
    print("     s> Shoot SELF")
    
    if Settings[8] != False:
        PlayerItems = Settings[9]
        letter = ("d", "f", "g", "h", "j", "k", "l", "z")
        print("\t\t\t Item Inventory (8 max):")
        x = 0
        while x < len(PlayerItems):
            print("\t\t\t\t" + letter[x] + "> Use...", PlayerItems[x])
            x += 1
        
    print("")
    choice = input("select: ")
    
    if choice == "a":
        Shooting.Shoot_Dealer(Settings)
        
    if choice == "s":
        Shooting.Shoot_Self(Settings)
    
    if choice == "d" and Settings[8] != False:
        print("Insert item usage here ;)")
        #Use_Item()
    print("")