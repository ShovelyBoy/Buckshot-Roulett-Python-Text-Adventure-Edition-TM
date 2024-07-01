import random
import time

import Shooting


#Settings = [ShellOrder0, blank1, live2, MaxHealth3, PlayerHealth4, DealerHealth5, PlayerLast6, DealerLast7, MaxItem8, PlayerItems9, DealerItems10]


def Dealer_Turn(Settings):
    time.sleep(2)

    if Settings[8] == False:
        if Settings[1] == Settings[2]:
            if random.randint(1, 2) == 1:
                Shooting.Shoot_Player(Settings)
            if random.randint(1, 2) == 2:
                Shooting.Dealer_Shoots_Self(Settings)
        
        if Settings[1] > Settings[2]:
            Shooting.Dealer_Shoots_Self(Settings)

        if Settings[1] < Settings[2]:
            Shooting.Shoot_Player(Settings)
