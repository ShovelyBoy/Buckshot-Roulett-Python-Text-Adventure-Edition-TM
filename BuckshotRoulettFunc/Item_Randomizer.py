import random


#Settings = [ShellOrder0, blank1, live2, MaxHealth3, PlayerHealth4, DealerHealth5, PlayerLast6, DealerLast7, MaxItem8, PlayerItems9, DealerItems10]


def Item_Randomizer(Settings):
    MaxItem = Settings[8]
    PlayerItems = Settings[9]
    DealerItems = Settings[10]
    StoryItems = ["Beer", "Cigarette Pack", "Hand Saw", "Handcuffs", "Magnifying Glass"]

    if type(MaxItem) is int:
        PlayerItems = []
        DealerItems = []
        x = 0
        while x < MaxItem:
            PlayerItems.append(StoryItems[random.randint(0, 4)])
            DealerItems.append(StoryItems[random.randint(0, 4)])
            x += 1

    elif MaxItem == True:
        MaxItem = len(DealerItems)
    
    Settings[8] = MaxItem
    Settings[9] = PlayerItems
    Settings[10] = DealerItems