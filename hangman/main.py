import requests

def fetch_random_word():
    url = 'https://random-word-api.vercel.app/api?words=1'
    response = requests.get(url)
    data = response.json()
    word = data[0].upper()
    return word

def hangman():
    word = fetch_random_word()
    letters_tried = []
    incorrect_guess = 0
    simple_art = [
        '''
         O
        ''',
        '''
         O
         |
        ''',
        '''
         O
        /|
        ''',
        '''
         O
        /|\
        ''',
        '''
         O
        /|\
        /
        ''',
        '''
         O
        /|\
        / \
        '''
    ]

    return word, letters_tried, incorrect_guess, simple_art

def update_hidden(word, letters_tried, hidden_word):
    for i in range(len(word)):
        if word[i] in letters_tried[i]:
            hidden_word[i] = word[i]
    return hidden_word

def game():
    word, letters_tried, incorrect_guess, simple_art = hangman()
    hidden_word = ["_"] * len(word)

    while incorrect_guess < len(simple_art):
        print("Word: ", hidden_word)
        print("Words: ", word)
        guess = input("Guess a letter: ").upper()

        if guess in letters_tried:
            print("You already guessed that letter!")
            continue

        letters_tried.append(guess)

        if guess in word:
            hidden_word = update_hidden_word(word, letters_tried, hidden_word)




def initialize_game():
    word = fetch_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    hangman_art = [
        '''
           +---+
               |
               |
               |
              ===''',
        '''
           +---+
           O   |
               |
               |
              ===''',
        '''
           +---+
           O   |
           |   |
               |
              ===''',
        '''
           +---+
           O   |
          /|   |
               |
              ===''',
        '''
           +---+
           O   |
          /|\  |
               |
              ===''',
        '''
           +---+
           O   |
          /|\  |
          /    |
              ===''',
        '''
           +---+
           O   |
          /|\  |
          / \ |
              ==='''
    ]

    return word, guessed_letters, incorrect_guesses, hangman_art


# Function to display the hangman and the word progress
def display_hangman(incorrect_guesses, hangman_art, hidden_word):
    print(hangman_art[incorrect_guesses])
    print("Word:", hidden_word)


# Function to check if the game is won
def is_game_won(hidden_word):
    return "_" not in hidden_word


# Function to update the hidden word with correctly guessed letters
def update_hidden_word(word, guessed_letters, hidden_word):
    for i in range(len(word)):
        if word[i] in guessed_letters:
            hidden_word[i] = word[i]
    return hidden_word


# Function to play the game
def play_game():
    word, guessed_letters, incorrect_guesses, hangman_art = initialize_game()
    hidden_word = ["_"] * len(word)

    while incorrect_guesses < len(hangman_art):
        display_hangman(incorrect_guesses, hangman_art, hidden_word)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            hidden_word = update_hidden_word(word, guessed_letters, hidden_word)
            if is_game_won(hidden_word):
                print("Congratulations! You won!")
                print("The word was:", word)
                break
        else:
            incorrect_guesses += 1

    if incorrect_guesses == len(hangman_art):
        print(hangman_art[incorrect_guesses])
        print("Sorry, you lost!")
        print("The word was:", word)


# Main function to start the game
def main():
    game()


if __name__ == '__main__':
    main()
