# Write your code here
import random

# greeting
your_name = input()
print('Enter your name: >', your_name)
print('Hello,', your_name)

# getting current score
rating_file = open('rating.txt', 'r')
score = 0
for line in rating_file:
    if your_name in line:
        score_list = line.split()
        score = int(score_list[-1])

moves = []
# you can enter "rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire"
your_moves = input()
if your_moves == '':
    moves = ['rock', 'paper', 'scissors']
else:  
    moves = your_moves.split(',')
print("Okay, let's start")
while True:
    user_move = input()
    if user_move == '!exit':
        break
    elif user_move == '!rating':
        print('Your rating:', score)
    elif user_move not in moves:
        print('Invalid input')
    else:
        random.seed()
        computer_move = random.choice(moves)

        user_index = moves.index(user_move)
        computer_index = moves.index(computer_move)
        
        new_list = moves[user_index + 1:] + moves[:user_index]
        half = len(new_list) // 2
        winning_moves = new_list[half:]
        

        if user_move == computer_move:
            print(f"There is a draw ({computer_move})")
            score += 50
        elif computer_move in winning_moves:
            print(f"Well done. The computer chose {computer_move} and failed")
            score += 100
        else:
            print(f"Sorry, but the computer chose {computer_move}")

print('Bye!')