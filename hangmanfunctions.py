import os
import random

def checkvictory(over, lenght, guessed_right, secret_word, mistakes):
    if guessed_right == lenght:
        hangprint(mistakes)
        print(f"Congratulations. You won the game. The word is {secret_word}")
        over = 1
        return over
    
def checkloss(over, maxmistakes, mistakes, secret_word):
    if maxmistakes == mistakes:
        over = 1
        if over:
            hangprint(mistakes)
            print(f"You lost the game. Game over. The word is {secret_word}")
        return over
    
def randompick (filename):
    file = open(filename, "r")
    words = file.readlines()
    file.close()
    return words[random.randrange(len(words))]
    
def hangprint(mistakes):
    os.system('cls')    
    print("     ___________.._______")
    print("| .__________))______|")
    print("| | / /      ||")
    print("| |/ /       ||")
    match mistakes:
        case 0:
            print("| | /        ||      ")
            print("| |/         ||      ")
            print("| |          ||")
            print("| |         (()) ")
            print("| |        ")
            print("| |       ")
            print("| |     ")
            print("| |     ")
            print("| |     ")
            print("| |      ")
            print("| |     ")
            print("| |          ")
            print("| |        ")
            print("| |       ")
            print("-------------------------")
            print("|-|-------\ \---------|-|")
            print("| |        \ \        | |")
            print(": :         \ \       : :")
        case 1:
            print("| | /        ||.-''.")
            print("| |/         |/  _  \\")
            print("| |          ||  `/,|")
            print("| |          (\\\\`_.'")
            print("| |         .-`--'.")
            print("| |       ")
            print("| |     ")
            print("| |     ")
            print("| |     ")
            print("| |      ")
            print("| |     ")
            print("| |          ")
            print("| |        ")
            print("| |       ")
            print("-------------------------")
            print("|-|-------\ \---------|-|")
            print("| |        \ \        | |")
            print(": :         \ \       : :")
        case 2:
            print("| | /        ||.-''.")
            print("| |/         |/  _  \\")
            print("| |          ||  `/,|")
            print("| |          (\\\\`_.'")
            print("| |         .-`--'.")
            print("| |           . . Y\\")
            print("| |          |   | \\\\")
            print("| |          | . |  \\\\")
            print("| |          |   |   (`")
            print("| |               ")
            print("| |               ")
            print("| |               ")
            print("| |               ")
            print("| |               ")
            print("-------------------------")
            print("|-|-------\ \---------|-|")
            print("| |        \ \        | |")
            print(": :         \ \       : :")
        case 3:
            print("| | /        ||.-''.")
            print("| |/         |/  _  \\")
            print("| |          ||  `/,|")
            print("| |          (\\\\`_.'")
            print("| |         .-`--'.")
            print("| |        /Y . . Y\\")
            print("| |       // |   | \\\\")
            print("| |      //  | . |  \\\\")
            print("| |     ')   |   |   (`")
            print("| |               ")
            print("| |               ")
            print("| |               ")
            print("| |               ")
            print("| |               ")
            print("-------------------------")
            print("|-|-------\ \---------|-|")
            print("| |        \ \        | |")
            print(": :         \ \       : :")
        case 4:
            print("| | /        ||.-''.")
            print("| |/         |/  _  \\")
            print("| |          ||  `/,|")
            print("| |          (\\\\`_.'")
            print("| |         .-`--'.")
            print("| |        /Y . . Y\\")
            print("| |       // |   | \\\\")
            print("| |      //  | . |  \\\\")
            print("| |     ')   |   |   (`")
            print("| |          ||'     ")
            print("| |          ||      ")
            print("| |          ||      ")
            print("| |          ||      ")
            print("| |         / |    ")
            print("-------------------------")
            print("|-|-------\ \---------|-|")
            print("| |        \ \        | |")
            print(": :         \ \       : :")
        case 5:
            print("| | /        ||.-''.")
            print("| |/         |/  _  \\")
            print("| |          ||  `/,|")
            print("| |          (\\\\`_.'")
            print("| |         .-`--'.")
            print("| |        /Y . . Y\\")
            print("| |       // |   | \\\\")
            print("| |      //  | . |  \\\\")
            print("| |     ')   |   |   (`")
            print("| |          ||'||")
            print("| |          || ||")
            print("| |          || ||")
            print("| |          || ||")
            print("| |         / | | \\")
            print("-------------------------")
            print("|-|-------\ \---------|-|")
            print("| |        \ \        | |")
            print(": :         \ \       : :")
    print("\n\n")
    
    
    
    
    
    
    
    