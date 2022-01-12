#Rock-Paper-Scissors Game

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

import random
game_pics = [rock, paper, scissors]
user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if user_choose >= 3 or user_choose < 0:
  print("Sorry, Choose the correct option")
else:
  print(game_pics[user_choose])
  
  comp_random_choose = random.randint(0,2)
  print("Computer chose: ", comp_random_choose)
  print[game_pics[comp_random_choose]]

  #Compare the user and computer chosen options
  if user_choose == 0 and comp_random_choose == 2:
    print("You won the game")
  elif user_choose == 2 and comp_random_choose == 1:
    print("You won the game")
  elif user_choose == 1 and comp_random_choose == 0:
    print("You won the game")
  elif user_choose == comp_random_choose:
    print("Handshake, game is drawn")
  else:
    print("Sorry!, You lost the game")