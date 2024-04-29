import random
str = input("Do you want to roll a dice y/n?")
while str!="y":
    str=input("Do you want to roll a dice y/n?")
while str=="y":
    num = random.randint(1,6)
    if num==1:
        print("_______")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("-------")
    elif num==2:
        print("_______")
        print("[     ]")
        print("[0   0]")
        print("[     ]")
        print("-------")
    elif num==3:
        print("_______")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("-------")
    elif num==4:
        print("_______")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("-------")
    elif num==5:
        print("_______")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("-------")
    elif num==6:
        print("_______")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("-------")
    str=input("Do you want to roll again y/n?")