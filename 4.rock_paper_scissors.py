import random

print("---------- Rock Paper Scissors ✊✋✌ ----------")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]
result = " "

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
player_choice = choices[player] 

#Computer's choice - 0 rock; 1 paper; 2 scissors 
computer = random.randint(0, 2)
computer_choice = choices[computer]

if player >= 0 and player <= 2:
    if player == 0 and computer == 2:
        result = "You win"
    elif computer == 0 and player == 2:
        result = "You loose"
    elif player > computer:
        result = "You win"
    elif computer > player:
        result = "You loose"    
    elif player == computer:
        result = "Draw"
    print("{}\nComputer chose:\n{}\n{}\n\n-".format(player_choice, computer_choice, result))
else:
    print("Invalid number...")       
