import random

# ... [The rest of the code from your snippet is here] ...

def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += '_'
    return guessed_word

def is_guess_in_word(guess, secret_word):
    return guess in secret_word

def spaceman(secret_word):
    attempts = len(secret_word) + 3
    letters_guessed = []

    print(f"Welcome to Spaceman! Try to guess the word. The word has {len(secret_word)} letters.")
    
    while attempts > 0:
        guess = input(f"You have {attempts} attempts left. Please guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter only one letter!")
            continue
        
        if guess in letters_guessed:
            print("You already guessed that letter!")
            continue

        letters_guessed.append(guess)

        if is_guess_in_word(guess, secret_word):
            print("Nice guess!")
        else:
            print("Oops! That letter isn't in the word.")
            attempts -= 1
        
        print(get_guessed_word(secret_word, letters_guessed))
        
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            return

    print(f"Sorry, you ran out of attempts. The word was {secret_word}.")

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
    from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    with open('words.txt', 'r') as f:
        words_list = f.read().splitlines()
    
    if len(words_list) == 1:  # If all words are on a single line
        words_list = words_list[0].split(' ')
    
    return random.choice(words_list)

secret_word = load_word()
spaceman(secret_word)
