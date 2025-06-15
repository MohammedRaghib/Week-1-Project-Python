import random

CHOICES = {
    1: 'Rock',
    2: 'Paper',
    3: 'Scissors'
}

def check(playerchoice, compchoice):
    comp_choice_name = CHOICES[compchoice]

    if playerchoice == compchoice:
        return {
            'message': f'Computer also chose {comp_choice_name}. It\'s a Tie!',
            'player_won': None 
        }
    elif (playerchoice == 1 and compchoice == 3) or \
         (playerchoice == 2 and compchoice == 1) or \
         (playerchoice == 3 and compchoice == 2):
        return {
            'message': f'Computer chose {comp_choice_name}. Player wins!',
            'player_won': True
        }
    else:
        return {
            'message': f'Computer chose {comp_choice_name}. Computer wins!',
            'player_won': False
        }
    
def display_final_score(score):
    print("\n--- Final Score ---")
    for key, value in score.items():
        if key != 'Winner': 
            print(f'{key}: {value}')
    print(f"Overall Winner: {score['Winner']}")
    print("-------------------")

    play_again = input('Want to play again? [y/n]: ').strip().lower()

    if play_again == 'y':
        play()
    else:
        print("Thanks for playing!")


def play():
    while True:
        rounds_input = input('Enter the number of rounds to be played: ').strip()
        try:
            rounds = int(rounds_input)
            if rounds <= 0:
                print("Please enter a positive number of rounds.")
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number only.')
    
    score = {
        'Player Wins': 0,
        'Computer Wins': 0,
        'Ties': 0, 
        'Total Rounds Played': 0,
        'Winner' : ''
    }

    for _ in range(rounds):
        print(f"\n--- Round {score['Total Rounds Played'] + 1} of {rounds} ---")
        
        while True:
            player_choice_str = input("Enter your choice (rock, paper, scissors): ").strip().lower()
            
            int_player_choice = 0
            if player_choice_str == 'rock':
                int_player_choice = 1
            elif player_choice_str == 'paper':
                int_player_choice = 2
            elif player_choice_str == 'scissors':
                int_player_choice = 3
            else:
                print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")
                continue

            break 

        comp_choice = random.randint(1, 3) 
        
        result = check(playerchoice=int_player_choice, compchoice=comp_choice)
        print(result['message'])

        score['Total Rounds Played'] += 1
        if result['player_won'] is True:
            score['Player Wins'] += 1
        elif result['player_won'] is False:
            score['Computer Wins'] += 1
        else:
            score['Ties'] += 1
        
    if score['Player Wins'] > score['Computer Wins']:
        score['Winner'] = 'Player'
    elif score['Computer Wins'] > score['Player Wins']:
        score['Winner'] = 'Computer'
    else:
        score['Winner'] = 'Tie! No overall winner.'
    
    display_final_score(score)

play()
