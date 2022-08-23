import random

#Header
print("************************************")
print("Welcome to the Guess the Number game")
print("************************************\n\n")

#Get the Secret Number
sec_num = random.randint(0,9)

#define state as not won and start counter for number of plays and max playability
ganhou = 0
guess_count = 0

#Define dificuldade
print("define the level of the game\n")
print("1 -  Hard\n")
print ("2 - Medium\n")
print("3 - Easy\n")
level = int(input())

while (level not in [1, 2, 3]):
    level = int(input("select a valid level\n"))

if level == 1:
    max_plays = 3
elif level == 2:
    max_plays = 4
else:
    max_plays = 5

#compare the results with the guessings
for plays in range(1,max_plays + 1):
    if not ganhou:    
        #Get the guessing
        print(f"{plays} of {max_plays} tries\n")
        guess = input("Guess a number\n")
        
        if (int(guess) > 9 or int(guess) < 0):
            print("you have to guess a number between 0 and 9")
            continue
        
        else:
            guess_count = guess_count + 1

            #Compare
            if int(guess) == sec_num:
                ganhou = 1
                print(f"Congratulations, you won the game in {guess_count} tries\n\n")
                
            elif int(guess) < sec_num and guess_count < max_plays:
                print("Not this time. The number is greater than your guessing")
            
            elif guess_count <  max_plays:
                print("Not this time. The number is smaller than your guessing")

if not ganhou:
    print ("You have no more tries. Game Over")
