import Item_Randomizer
import Shell_Randomizer

def Game_Round(ShellOrder0, blank1, live2, MaxHealth3, PlayerHealth4, DealerHealth5, PlayerLast6, DealerLast7, MaxItem8, PlayerItems9, DealerItems10):
    Settings = [ShellOrder0, blank1, live2, MaxHealth3, PlayerHealth4, DealerHealth5, PlayerLast6, DealerLast7, MaxItem8, PlayerItems9, DealerItems10]

    if Settings[8] != False:
        Item_Randomizer.Item_Randomizer(Settings)
        
    Shell_Randomizer.Shell_Randomizer(Settings)