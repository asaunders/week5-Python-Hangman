import random
HANGMANPICS = ['''

    +---+
    |   |
        |
        |
        |
        |
===========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
===========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
===========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
===========''', '''

    +---+
    |   |
    O   |
   /|\  |
  /     |
        |
===========''', '''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
===========''']

words = 'apple banana chocolate doughnut thunder'.split()

def getWord(wordList)
    # This function returns a random word from the "words" list.
    wordIndex = random.randint (0, len(wordList) - 1)
    return wordList(wordIndex)

def displayBoard(HANGMANPICS, missedGuesses, correctGuesses, secretWord):
        print(HANGMANPICS[len(missedGuesses)])

    print('Missed letters:', end=' ')
    for letter in missedGuesses:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with
# correctly guessed letters
        if secretWord[i] in correctGuesses:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in
# between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes
# sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Try again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play
#again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')
missedGuesses = ''
correctGuessees = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedGuesses, correctGuesses,
secretWord)

# Player input.
    guess = getGuess(missedGuesses + correctGuesses)

     if guess in secretWord:
        correctGuesses = correctGuesses + guess

# Check for player victory.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctGuesses:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Congratulations! The secret word is "' + secretWord + '"!
You won!')
            gameIsDone = True
    else:
        missedGuesses = missedGuesses + guess

# Check for GAME OVER.
        if len(missedGuesses) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedGuesses,
correctGuesses, secretWord)
            print('You have run out of guesses!\nAfter ' +
str(len(missedGuesses)) + ' missed guesses and ' +
str(len(correctGuesses)) + ' correct guesses, the word was "' +
secretWord + '"')
            gameIsDone = True

# Ask player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedGuesses = ''
            correctGuesses = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
