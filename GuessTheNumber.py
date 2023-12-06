import random, json, datetime, math
from os.path import exists

def create_new_records_file():
    a = []
    
    with open('records.json', 'w') as data:
        data.write(json.dumps(a))

def records_load():
    global top_records, records_list
    
    if not exists('records.json'):
        create_new_records_file()
    
    with open('records.json', 'r') as record_data:
        records_list = json.loads(record_data.read())
        top_records = sorted(records_list, key=lambda d: d['attempts'])[:3] 

def records_top_scores():
    
    if len(top_records) > 0:
        print("TOP 3 SCORES:")

        for dict in top_records:
            print(f"\t{dict["player_name"]} beat the game in {dict["attempts"]} attempts on {dict["game_mode"]} mode on {dict["date"]}")
    else:
        print('\nNo Highscores, yet.')

    print('\n')

def records_save(attempts):
    global player_name
    
    now = datetime.datetime.now()
    game_mode = 'Easy' if EASY_MODE else 'Hard'
    records_list.append({"player_name": player_name, "attempts": attempts, "date": now.strftime('%d.%m.%Y %H:%M:%S'), "game_mode": game_mode})
    
    with open('records.json', 'w') as record_data:
        record_data.write(json.dumps(records_list))

def play_game():
    
    attempts = 1

    secret = random.randint(RANGE_FROM, RANGE_TO)
    guess = secret + 1
    
    while attempts <= MAX_TRIES and secret != guess:
        guess = 'a'
        
        while not guess.isnumeric():
            guess = input(f"Guess the secret number between {RANGE_FROM} and {RANGE_TO}: ")
        
        guess = int(guess)
        
        if RANGE_FROM <= guess <= RANGE_TO:
            if guess == secret:
                print(f"You guessed it - congratulations! It's the number {secret}.")
                records_save(attempts)
                
                try:
                    if attempts < top_records[0]['attempts']:
                        print("\n***********************************************")
                        print("***************** NEW RECORD! *****************")
                        print("***********************************************")
                except:
                    pass
            
            else:
                print(f"Sorry, your guess is not correct... The secret number is not {guess}.")
                
                if attempts == MAX_TRIES:
                    print(f"Sorry, no tries left. The secret number was {secret}.")
                elif guess < secret and EASY_MODE:
                    print("Try a higher number.")
                elif guess > secret and EASY_MODE:
                    print("Try a lower number.")

                print(f"Tries left: {MAX_TRIES-attempts}\n")
                attempts += 1
        
        else:
            print(f"Please, enter a number between {RANGE_FROM} and {RANGE_TO}.\n")

def chage_game_mode():
    global MAX_TRIES, EASY_MODE
    
    if EASY_MODE:
        EASY_MODE = False
        max_tries_divisor = 5

        print('Game mode set to HARD.\n')
    
    else:
        EASY_MODE = True
        max_tries_divisor = 4
        print('Game mode set to EASY.\n')

    MAX_TRIES = math.ceil((RANGE_TO - RANGE_FROM + 1)/max_tries_divisor)

#############################################################################

RANGE_FROM = 1
RANGE_TO = 20
MAX_TRIES = math.ceil((RANGE_TO - RANGE_FROM + 1)/4)
EASY_MODE = True

top_records = []
records_list = []

#############################################################################

player_name = input("Enter your name: ")

print(f'Hi {player_name}! What would you like to do?')

while True:
    records_load()
    
    player_choice = input('\nA) Play the game\nB) Change game difficulty\nC) Top Scores\nD) Clear highscores\nE) Quit\n\nYour Choice: ').upper()

    if player_choice == 'A':
        play_game()
    
    elif player_choice == 'B':
        chage_game_mode()
    
    elif player_choice == 'C':
        records_top_scores()
    
    elif player_choice == 'D':
        create_new_records_file()
    
    elif player_choice == 'E':
        print('Bye!')
        break