import time
import os

import Player_Turn
import Shell_Randomizer
import random


#Settings = [ShellOrder0, blank1, live2, MaxHealth3, PlayerHealth4, DealerHealth5, PlayerLast6, DealerLast7, MaxItem8, PlayerItems9, DealerItems10]


def Shell_Randomizer(Settings):
    ShellOrder = Settings[0]
    ShellShow = []
    blank = Settings[1]
    live = Settings[2]
    
    if type(ShellOrder) is list:
        Settings[1] = ShellOrder.count("blank")
        Settings[2] = ShellOrder.count("live")
        ShellShow = ShellOrder.copy()
        random.shuffle(ShellShow)
        for x in ShellShow:
            print(" -", x)
        Player_Turn.Player_Turn(Settings)
    
    elif ShellOrder == 0:
        Settings[0] = random.randint(2, 8)
        Shell_Randomizer(Settings)
    
    elif ShellOrder == 1:
        blank = Settings[1]
        live = Settings[2]
    
    elif ShellOrder == 2:
        blank = 1
        live = 1
    
    elif ShellOrder == 3:
        blank = random.randint(1, 2)
        live = 3 - blank
    
    elif ShellOrder == 4:
        blank = random.randint(1, 3)
        live = 4 - blank
    
    elif ShellOrder == 5:
        blank = random.randint(1, 3)
        live = 5 - blank
    
    elif ShellOrder == 6:
        blank = random.randint(2, 4)
        live = 6 - blank
    
    elif ShellOrder == 7:
        blank = random.randint(3, 4)
        live = 7 - blank
    
    elif ShellOrder == 8:
        blank = 4
        live = 4
    
    if ShellOrder in range(1, 9):
        Settings[1] = blank
        Settings[2] = live
        ShellOrder = []
        x = 0
        y = 0
        while x < blank:
            ShellOrder.append("blank")
            x+=1
        while y < live:
            ShellOrder.append("live")
            y+=1
        
        ShellShow = ShellOrder.copy()
        random.shuffle(ShellOrder)
        Settings[0] = ShellOrder
        
        random.shuffle(ShellShow)
        for x in ShellShow:
            print(" -", x)
        time.sleep(3)
        os.system('cls')
        
        #DealerAI.Dealer_Turn(Settings)
        Player_Turn.Player_Turn(Settings)