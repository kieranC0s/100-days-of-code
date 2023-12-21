import random

from hangman_words import word_list

chosen_words = random.choice(word_list)
word_length = len(chosen_words)

end_of_game = False
lives = 6

from hangman_art import logo
print(logo)

# #Testing code
# print(f'The solution is {chosen_words}.')

#create blanks
display = []
for _ in range(word_length):
    display += "_"
    
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You've already guessed {guess}")
        
    #check guessed letter
    for position in range(word_length):
        letter = chosen_words[position]
        
        if letter == guess:
            display[position] = letter
    
    #Check if user is wrong.    
    if guess not in chosen_words:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The correct word was {chosen_words}")
        
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
        
    #check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
        
    from hangman_art import stages
    print(stages[lives])