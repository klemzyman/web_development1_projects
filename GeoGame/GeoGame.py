import json, random
from thefuzz import fuzz

def get_round_data(selection):
    if selection == len(continents):
        continent = continents[random.randint(1, len(continents)-1)]
    else:
        continent = continents[selection - 1]

    country, capital = random.choice(list(world_data[continent].items()))
    
    return country, capital

def play_game(selection):

    countries_played = ['a']
    country = 'a'
    
    for i in range(NUMBER_OF_ROUNDS):
        guess = ''                           
        current_try = 1
        
        while country in countries_played:
            country, capital = get_round_data(selection)

        countries_played.append(country)

        while current_try <= MAX_TRIES:
            guess = input(f'What is the capital of {country}?\t')
            guess_distance = fuzz.token_set_ratio(guess, capital)
            
            if guess_distance > 80:
                print(f'Correct! Then capital of {country} is {capital}.\n')
                break
            else:
                current_try += 1
                print('Try again.')
            
        else:
            print(f'Sorry, the correct answer is {capital}.')

def list_continents():
    for index, continent in enumerate(continents):
        print(f'{index+1}) {continent}')

def user_choice(selection = 'a'):
    while not selection.isnumeric():
        selection = input("Your choice: ")
    
    return int(selection)

def load_data():
    global world_data, continents
    
    with open('countries.json', 'r', encoding='utf-8') as data:
        world_data = json.loads(data.read())

    continents = list(world_data.keys())
    continents.append('All Continents')

NUMBER_OF_ROUNDS = 5
MAX_TRIES = 3

load_data()

while True:
    print('Hi! Which continent would you like to play?')
        
    list_continents()
    
    selection = user_choice()
    
    play_game(selection) 

    play_again = input('Would you like to play again? Y/N  ').upper()

    if play_again != 'Y':
        break
