import hangmanfunctions

def play():
    
    MAXMISTAKES = 5
    
    #Header
    print("************************************")
    print("********  This is Hangman  *********")
    print("************************************\n\n")
    
    #define secret word and make the canvas
    over = 0
    mistakes = 0
    secret_word = hangmanfunctions.randompick ("words.txt")
    secret_word = str.strip(str.lower(secret_word))
    guessed = []
    guessed_right = 0
    situation = (len(secret_word)*"_")
    hangmanfunctions.hangprint(mistakes)
    
    #Loop - get the letter and check if it has been tried before and if it's valid
    while not over:
        print(situation, "\n")
        print(f"So far, you've made {mistakes} mistakes\n")
        print("Letters Guessed:", guessed, "\n") 
        guess = input("Guess a letter:\n")
        guess = str.strip(str.lower(guess))
               
        
        #check if the letter has already been guessed
        if (guess not in guessed):
            guessed.append(guess)
            
        else:
            print("This letter has already been guessed. Try another one\n")
            continue
        
        #check if the letter is in the word
        if (guess not in secret_word):
            mistakes = mistakes +1
            over = hangmanfunctions.checkloss(over, MAXMISTAKES, mistakes, secret_word)
        #if it is, update the situation and sum the correct letters
        else:
            i = 0
            for letter in secret_word:
                if (letter == guess):
                    guessed_right = guessed_right + 1
                    situation = situation[:i] + guess + situation[i+1:]
                    over = hangmanfunctions.checkvictory(over, len(secret_word), guessed_right, secret_word, mistakes)              
                i += 1 
        if not over:
            hangmanfunctions.hangprint(mistakes)
            
        
if (__name__ == "__main__"):
    play()
        