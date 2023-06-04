'''
Author : EKENEDO NZUBE EMMANUEL

Purpose: The purpose of this game is to allow the user to guess the same word as the secret word correctly, 
the user is given a prompt hint to enable him know the lenght of the word. If the letter in the guess word is 
in the same spot as in  secret word, it will be print in upper case if not it will be printed lower case, if 
it is neither there in secret word, a hint with '_' will be shown to him. 

'''

secretWord = 'commit'
userGuess = ''
guessCount = 0
hint = ' _ ' *len(secretWord)
print(f'Your hint is:{hint}')

# we have to keep asking the user to guess as long as guess is not equall to secret word
while secretWord != userGuess:
    userGuess = input(' Please what is your guess? ').lower()
    guessCount += 1
    #checking if secret word is same as guess word
    if secretWord == userGuess:
        print('You guessed correctly!')
        print(f'It took you {guessCount} number of guesses')
        #checking the length secret word is the same as guess word
    elif len(secretWord) != len(userGuess):
        print('Sorry your guess must be of the same number with secret word')
        
    else:
        print('Your guess was incorrect!.')
        print(f"Your hint is:{hint}")
        #checking if the letters and the index of the guess word is the with the secret word
        for index, letter in enumerate(userGuess):
            if userGuess[index] == secretWord[index]:
                print(letter.upper(), end = ' ')
            elif letter in secretWord:
                print(letter.lower(), end = '')
            else:
                print('_', end = ' ') 