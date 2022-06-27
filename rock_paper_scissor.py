import random
choices = ['Rock', 'Paper', 'Scissors']
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("rock, paper or scissors?:  ").capitalize()
    if player == computer:
        print(f'computer choice was {computer} and it is tie')
    elif player == 'Rock':
        if computer == 'Paper':
            print(f'computer choice was {computer}, you loose!')
            cpu_score += 1
        else:
            print(f'computer choice was {computer}, you win!')
            player_score += 1
    elif player == 'Paper':
        if computer == 'Scissors':
            print(f'computer choice was {computer}, you loose')
            cpu_score += 1
        else:
            print(f'computer choice was {computer}, you win')
            player_score += 1
    elif player == 'Scissors':
        if computer == 'Rock':
            print(f'computer choice was {computer}, you loose')
            cpu_score += 1
        else:
            print(f'computer choice was {computer}, you win')
            player_score += 1
    elif player == 'end':
        print('Final scores: ')
        print(f'cpu score is: {cpu_score}')
        print(f'player score is: {player_score}')
