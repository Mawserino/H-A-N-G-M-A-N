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
        if word[i] in letters_tried:
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
            hidden_word = update_hidden(word, letters_tried, hidden_word)
def main():
    game()


if __name__ == '__main__':
    main()
