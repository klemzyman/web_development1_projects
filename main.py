import json, random
from thefuzz import fuzz

GAMES_NO = 5
MAX_TRIES = 3

with open('countries.json', 'r') as data:
    countries = json.loads(data.read())

for i in range(GAMES_NO):
    guess = ''                           
    current_try = 1
    country, capital = random.choice(list(countries.items()))

    while current_try <= MAX_TRIES:
        guess = input(f'What is the capital of {country}?\t')
        guess_distance = fuzz.token_set_ratio(guess, capital)
        
        #if guess.lower() == capital.lower():
        if guess_distance > 80:
            print(f'Correct! Then capital of {country} is {capital}.\n')
            break
        else:
            current_try += 1
            print('Try again.')
        
    else:
        print(f'Sorry, the correct answer is {capital}.')