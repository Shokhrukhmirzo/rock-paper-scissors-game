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

#Write your code below this line 👇

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

choice_list = [rock, paper, scissors]

player_choice = choice_list[choice - 1]
computer_choice_rand = random.randint(0,3)

player_choice = choice_list[choice - 1]
computer_choice  = choice_list[computer_choice_rand - 1]
if choice >= 3:
  print("You lost becasue you chose the invalid option")
else:
  if player_choice == rock and computer_choice == scissors:
    print("You win")
  elif player_choice == scissors and computer_choice == paper:
    print("You win")
  elif player_choice == paper and computer_choice == rock:
    print("You win!")
  elif player_choice == paper and computer_choice == paper:
    print("Draw")
  elif player_choice == rock and computer_choice == rock:
    print("Draw")
  elif player_choice == scissors and computer_choice == scissors:
    print("Draw")
  else:
    print("You lose!")
  print(f"Your choice is {player_choice}")

  print(f"Computer's choice is {computer_choice}")

