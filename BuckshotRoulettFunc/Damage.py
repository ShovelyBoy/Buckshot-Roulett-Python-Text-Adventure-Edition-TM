#Settings = [ShellOrder0, blank1, live2, MaxHealth3, PlayerHealth4, DealerHealth5, PlayerLast6, DealerLast7, MaxItem8, PlayerItems9, DealerItems10]


def Dealer_Damage(Settings):
    ShellCount = Settings[0]
    print("")
    if ShellCount[0] == "blank":
        print("\n\n\n\n*click*\n\n\n\n")
    elif ShellCount[0] == "live":
        print("\n\n\n\n*B A N G*\n\n\n\n")
        if Settings[5] > 0:
            Settings[5] -= 1
        elif Settings[5] == 0 and Settings[7] != False:
            Settings[7] -= 1
    print("")
    ShellCount.pop(0)
    Settings[0] = ShellCount
    Settings[1] = ShellCount.count("blank")
    Settings[2] = ShellCount.count("live")
        

def Player_Damage(Settings):
    ShellCount = Settings[0]
    print("")
    if ShellCount[0] == "blank":
        print("\n\n\n\n*click*\n\n\n\n")
    elif ShellCount[0] == "live":
        print("\n\n\n\n*B A N G*\n\n\n\n")
        if Settings[4] > 0:
            Settings[4] -= 1
        elif Settings[4] == 0 and Settings[6] != False:
            Settings[6] -= 1
    print("")
    ShellCount.pop(0)
    Settings[0] = ShellCount
    Settings[1] = ShellCount.count("blank")
    Settings[2] = ShellCount.count("live")
