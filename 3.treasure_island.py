print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____..
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!!!")
print("Your mission is to find the treasure.")
print("-" * 20) 

step1 = input('You\'re at a crossroad. Where do you want to go?\nType "left" or "right".\n').lower()

if step1 == "left":
    print("-" * 50) 
    step2 = input('You\'ve come to a lake. There is an island in the middle of a lake.\nType "wait" to wait for a boat.\nType "swin" to swin across.\n').lower()
    if step2 == "wait":
        print("-" * 50) 
        step3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.\nWhich colour do you choose?\n').lower()
        if step3 == "red":
            print("-" * 50) 
            print("Burned by fire.\nGAME OVER.")
        elif step3 == "blue":
            print("-" * 50) 
            print("Eaten by beasts.\nGAME OVER.")
        elif step3 == "yellow":
            print("-" * 50) 
            print("YOU FOUND THE TREASURE!\nCONGRATULATIONS!!!")
        else:
            print("-" * 50) 
            print("The crest was empty.\nGAME OVER.")
    else:
        print("-" * 50) 
        print("Attacked by trout.\nGAME OVER.")
else:
    print("-" * 50) 
    print("Fall into a hole.\nGAME OVER.")