import pyfiglet
import random

lists = ['Yes', 'No', 'Perhaps', 'Try again later!']
rlists = random.choice(lists)
def ball8_game():
    banner = pyfiglet.figlet_format("8 - BALL")
    print(banner)
    i = 1
    while i > 0:
        print("Welcome. I am your 8-BALL.")

        question = input("Enter 'Q' to quite.\nAsk me any yes/no question: ").upper()

        if question == 'Q':
            print("Goodbye...")
            break
        else:
            if '?' not in question:
                print('Please ask a valid question...\n')
                continue
            else:
                print(rlists + '\n')
                i += 1
                break