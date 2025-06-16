import random

print("rock")
print("paper")
print("scissors")

player1 = input("Player1, make your move: ")

rand_num = random.randint(1,3)
if rand_num == 1:
    computer = "rock"
elif rand_num == 2:
    computer = "paper"
else:
    computer = "scissors"
print(f"Computer plays {computer}" )


if player1 == "rock" and computer == "scissors":
    print("Player1 wins")
elif player1 == "scissors" and computer == "paper":
    print("Player1 wins")
elif player1 == "paper" and computer == "rock":
    print("Player1 wins")
elif player1 == computer:
    print("its a tie")
else:
    print("computer wins")