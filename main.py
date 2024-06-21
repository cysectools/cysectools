import pyfiglet
from function import ball8_game

cbanner = pyfiglet.figlet_format("CYSECTOOLS", font="slant")
print(cbanner)

a = 1
while a > 0:
    before = input("Enter 'S' to start and 'Q' to quite: ").upper()

    if before == 'S':
        ball8_game()
        break
    elif before == 'Q':
        print("Goodbye...")
        break
    else:
        print("Please input valid letter.")
        continue