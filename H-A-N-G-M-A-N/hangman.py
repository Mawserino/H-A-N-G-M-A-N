import random
import string 

from puzzles import puzzles

def get_valid_puzzle(puzzles):
    puzzle = random.choice(puzzles)

    while '-' in puzzle or ' ' in puzzle:
        puzzle = random.choice(puzzles)

    return puzzle.upper()
    
def hangman():
    puzzle = get_valid_puzzle(puzzles)
    puzzle_letters = set(puzzle)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 5

    while la
    len(puzzle_letters)  > 0 and lives > 0:
        print("Used Letters:  ", " ".join(used_letters))
        print("Lives: ", lives)

        puzzle_list =  [letter if letter in used_letters else '-' for letter in puzzle]
        print("Current puzzle: ", ' '.join(puzzle_list))
               

        letter_choice = input ("Choose a letter: ").upper()
        if letter_choice in alphabet - used_letters:
            used_letters.add(letter_choice)
            if letter_choice in puzzle_letters:
                puzzle_letters.add(letter_choice)
            
            else:
                lives = lives - 1
                print ('Letter not in word.')

        elif letter_choice in alphabet - used_letters:
            print ("Letter already chosen, Please choose a another letter")

        else:
            print ("Invalid choice, please choose another letter")
    

    if lives == 0:
        print ("You dead, game over. the word was ", puzzle)
    else:
        print ("YOU DID IT!! CONGRATS")


hangman()


