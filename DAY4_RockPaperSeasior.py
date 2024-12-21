import random
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

game_img = [rock,paper,scissors]
user_chosen = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))

print(game_img[user_chosen])

computer_choice = random.randint(0,2)
print("computer choice:")

print(game_img[computer_choice])

if user_chosen >= 3 or user_chosen < 0:
    print("Invalid! YOU LOSE")

elif user_chosen == 0 and computer_choice == 2:
    print("YOU WIN!")

elif user_chosen == 2 and computer_choice == 0:
    print("YOU WIN!")

elif computer_choice > user_chosen:
    print("YOU WIN!")

elif user_chosen > computer_choice:
    print("YOU WIN!")

elif computer_choice == user_chosen:
    print("...MATCH DRAW...")