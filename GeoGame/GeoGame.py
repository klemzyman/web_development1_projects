import json, random, os
from thefuzz import fuzz

def clear_terminal():
    os.system('cls')

def play_game(selection):
    
    def get_round_data(selection):
    
        if selection == len(continents):
            continent = continents[random.randint(1, len(continents)-2)]
        else:
            continent = continents[selection - 1]

        country, capital = random.choice(list(world_data[continent].items()))
        
        return country, capital

    def get_rounds(rounds=0):
        
        if NUMBER_OF_ROUNDS == 0:
            if selection < 7:
                rounds = len(list(world_data[continents[selection - 1]]))
            else: 
                for k, v in world_data.items():
                    rounds += len(v)
        else:
            if selection < 7:
                rounds = min(len(list(world_data[continents[selection - 1]])), NUMBER_OF_ROUNDS)
            else:
                for k, v in world_data.items():
                    rounds += len(v)
                
                rounds = min(rounds, NUMBER_OF_ROUNDS)
        
        return rounds
    
    countries_played = ['a']
    country = 'a'
    rounds=get_rounds()

    for i in range(rounds):
        guess = ''                           
        current_try = 1
        
        print(f'ROUND #{i+1} of {rounds}')

        while country in countries_played:
            country, capital = get_round_data(selection)

        countries_played.append(country)

        while current_try <= MAX_TRIES:
            guess = input(f'What is the capital of {country}?  ')
            
            if guess == '-':
                current_try = MAX_TRIES + 1
            elif guess == '!':
                print('Exiting game ...')
                exit()
            else:
                guess_distance = fuzz.token_set_ratio(guess, capital)
            
                if guess_distance > 80:
                    print(f'Correct! Then capital of {country} is {capital}.\n')
                    break
                elif MAX_TRIES != 0:
                        current_try += 1
                        print('Try again.')
                                         
            
        else:
            print(f'The correct answer was {capital}.\n')
       
def list_continents():
    for index, continent in enumerate(continents):
        print(f'{index+1}) {continent}')

def list_other_choices():
    choices = ['Show Tips', 'Settings']

    print()
    for index, choice in enumerate(choices):
      print(f"{len(continents)+index+1}) {choice}")
    
    print('0) Quit\n')

def user_choice(selection = 'a'):
    
    while not selection.isnumeric():
        selection = input("Your choice: ")
    
    print('\n')
    return int(selection)

def load_data():
    global world_data, continents, tips
    
    with open('countries.json', 'r', encoding='utf-8') as data:
        world_data = json.loads(data.read())

    continents = list(world_data.keys())
    continents.append('All Continents')

    tips = ["Enter '-' if you wish to pass to the next questions.",
            "When playing, enter '!' to exit the game."]

def list_tips():
    for tip in tips:
        print(f'\tTip: {tip}')

    input("\nGo back?")
    os.system('cls')

def changes_settings():
    global NUMBER_OF_ROUNDS, MAX_TRIES
    
    print()
    
    x = 'a'
    
    while not x.isnumeric():
        x = input('How many rounds per game do you want to play? (0 = unlimited)  ')
    NUMBER_OF_ROUNDS = int(x)

    x = 'a'
    
    while not x.isnumeric():
        x = input('How many tries would you like? (0 = unlimited)  ')
    MAX_TRIES = int(x)

    clear_terminal()


NUMBER_OF_ROUNDS = 5
MAX_TRIES = 3

load_data()
clear_terminal()

print('Hi!', end=' ')

while True:
    print('Which continent would you like to play?')
        
    list_continents()
    list_other_choices()
    
    selection = user_choice()
    
    if 1 <= selection <= 7:
        play_game(selection) 

        play_again = input('Would you like to play again? Y/N  ').upper()

        if play_again != 'Y':
            clear_terminal()
            break
        else:
            clear_terminal()
    elif selection == 8:
        list_tips()
    elif selection == 9:
        changes_settings()
    elif selection == 0:
        clear_terminal()
        break
