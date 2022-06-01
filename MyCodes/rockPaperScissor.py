import random
from tkinter import PIESLICE
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
player_Choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_Choice = random.randint(0, 2)

if player_Choice == 0:
    print(rock)
elif player_Choice == 1:
    print(paper)
else:
    print(scissors)

print("Computer chose:")

if computer_Choice == 0:
    print(rock)
elif computer_Choice == 1:
    print(paper)
else:
    print(scissors)

if player_Choice == 0 and computer_Choice == 2:
    print("You win!")
elif player_Choice == 1 and computer_Choice == 0:
    print("You win!")
elif player_Choice == 2 and computer_Choice == 1:
    print("You win!")
elif player_Choice == computer_Choice:
    print("Draw!")
else:
    print("You lose.")
