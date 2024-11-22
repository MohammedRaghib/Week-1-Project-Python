# prints the game intro
print('Lets play rock paper scissors')

# dict to track score
scoreboard = {
    "playerscore": 0,
    "compscore": 0,
    "draws": 0,
    "rounds": 0
}

# Game functionality
def game(scoreboard):
    while True:
        # prompts user to make an input
        player_input = input('Enter your choice (type exit to leave): ') 

        # imports the random function from python built in library
        import random 

        # generates the comp choice which is absolutely randomised
        # 1 is rock, 2 is paper, 3 is scissors
        random_number = random.randint(1,3)

        # test to see if random fucntion works:
        # print(random_number)

        # lowercases player input to make it easier to check
        pil = player_input.lower()

        # conditional statements to check and respond accordingly to the player and comps choice

        if pil == 'rock' and random_number == 1:
            print('Tie') # 1a. player and comp choice rock = tie
            scoreboard['draws'] += 1
            scoreboard['rounds'] += 1
        elif pil == 'paper' and random_number == 2:
            print('Tie') # 1b. player and comp choice paper = tie
            scoreboard['draws'] += 1
            scoreboard['rounds'] += 1
        elif pil == 'scissors' and random_number == 3:
            print('Tie') # 1c. player and comp choice scissors = tie
            scoreboard['draws'] += 1
            scoreboard['rounds'] += 1
        elif pil == 'rock' and random_number == 3:
            print('You win') # 2a. player choice rock and comp choice scissors = player wins
            scoreboard['playerscore'] += 1
            scoreboard['rounds'] += 1
        elif pil == 'scissors' and random_number == 1:
            print('Comp wins') # 2b. player choice scissors and comp choice rock = comp wins
            scoreboard['compscore'] += 1
            scoreboard['rounds'] += 1
        elif pil == 'scissors' and random_number == 2:
            print('You win') # 3a. player choice scissors and comp choice paper = player wins
            scoreboard['playerscore'] += 1
            scoreboard['rounds'] += 1
        elif pil == 'paper' and random_number == 3:
            print('Comp wins') # 3b. player choice paper and comp choice scissors = comp wins
            scoreboard['compscore'] += 1
            scoreboard['rounds'] += 1
        elif pil == 'paper' and random_number == 1:
            print('You win') # 4a. player choice paper and comp choice rock = player wins
            scoreboard['playerscore'] += 1
            scoreboard['rounds'] += 1
        elif pil == 'rock' and random_number == 2:
            print('Comp wins') # 4b. player choice rock and comp choice paper = comp wins
            scoreboard['compscore'] += 1
            scoreboard['rounds'] += 1
        elif pil == 'exit':
            print('')
            print('Hope you had fun, here are the scores:')
            print('')
            print(f'Rounds played: {scoreboard['rounds']}')
            print(f'Draws: {scoreboard['draws']}')
            print(f'Your score: {scoreboard['playerscore']}')
            print(f'Comp score: {scoreboard['compscore']}')
            break
        else:
            print('Not a valid input')
# Intializes game
game(scoreboard)