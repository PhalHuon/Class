#This program asks the user to guess the hardcoded number that was initially put into the program.
#it will say too low or too high depending on the guess

def roulette():
    max_Attempts = int(input("Enter a number to guess the number: "))
    original_num = 10
    attempts = 0
    while attempts < max_Attempts:
        guess_Num = int (input ("Guess the number again: "))
        if guess_Num == original_num:
            print ("correct")
            break
        elif guess_Num < original_num:
            print ("the guess is too low")
        elif guess_Num > original_num:
            print("the guess is too high")
           
        else:
            print ("Error")
      
        attempts = attempts + 1
    if attempts == max_Attempts:
        print ("you lose")

roulette()
