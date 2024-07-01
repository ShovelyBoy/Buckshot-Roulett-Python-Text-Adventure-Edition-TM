import Damage
import Item_Randomizer
import Player_Turn
import DealerAI


#Settings = [ShellOrder0, blank1, live2, MaxHealth3, PlayerHealth4, DealerHealth5, PlayerLast6, DealerLast7, MaxItem8, PlayerItems9, DealerItems10]


def Shoot_Dealer(Settings):
    print("")
    print("*PLAYER shoots DEALER*")
    print("")
    Damage.Dealer_Damage(Settings)
    if Settings[0] == []:
        Settings[0] = 0
        Item_Randomizer.Item_Randomizer(Settings)
    else:
        DealerAI.Dealer_Turn(Settings)
    
    
def Shoot_Self(Settings):
    print("")
    print("*PLAYER Shoots Self*")
    print("")
    Damage.Player_Damage(Settings)
    if Settings[0] == []:
        Item_Randomizer(Settings)
    else:
        DealerAI.Dealer_Turn(Settings)
    
def Shoot_Player(Settings):
    print("")
    print("*DEALER shoots PLAYER*")
    print("")
    Damage.Player_Damage(Settings)
    if Settings[0] == []:
        Settings[0] = 0
        Item_Randomizer.Item_Randomizer(Settings)
    else:
        Player_Turn.Player_Turn(Settings)
        
def Dealer_Shoots_Self(Settings):
    print("")
    print("*DEALER shoots himself*")
    print("")
    Damage.Dealer_Damage(Settings)
    if Settings[0] == []:
        Settings[0] = 0
        Item_Randomizer.Item_Randomizer(Settings)
    else:
        Player_Turn.Player_Turn(Settings)