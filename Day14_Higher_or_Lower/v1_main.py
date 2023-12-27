#TODO: Load in game data and art
from replit import clear
import random


from art import logo, vs
from game_data import data

# TODO: Create a function to randomly select a dictionary from the game data list
def select_data():
    """Selects a random dictionary from the game data list"""
    return random.choice(data)

#TODO: Create a function to compare the follow
def compare(A,B):
    """Compares the follower count of two dictionaries and returns the one with the highest follower count"""
    if A > B:
        return "A"
    else:
        return "B"

#TODO: Create a function to keep track of the score
# def score():
#     """Keeps track of the score"""
#     score = 0
#     score += 1
#     return score
  
#TODO: Create a function to clear the screen
def clear_screen():
    """Clears the screen"""
    clear()
    print(logo)
    
#TODO: Create a function to ask the user if they want to play again
def play_again():
    """Asks the user if they want to play again"""
    play_again = (input(f"Do you want to play again? Type 'y' or 'n': ")).lower()
    if play_again == 'y':
        clear()  
        playgame()
    elif play_again == 'n':
        clear()
        game_over = True
        print("Thank you for playing")   

#TODO: Create a function to play the game
def playgame():
    
    print(logo)
    score = 0
    game_over = False
    
    while not game_over:
    
        #TODO: Select two dictionaries
        Dictionary_a = select_data()
        Dictionary_b = select_data()
        
        #TODO: Print the dictionaries
        print(f"Compare A: {Dictionary_a['name']}, a {Dictionary_a['description']}, from {Dictionary_a['country']}.")
        print(Dictionary_a['follower_count'])
        print(vs)
        print(f"Against B: {Dictionary_b['name']}, a {Dictionary_b['description']}, from {Dictionary_b['country']}.")
        print(Dictionary_b['follower_count'])
        
        #TODO: Ask the user to guess who has more followers
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        comparison = (compare(Dictionary_a['follower_count'], Dictionary_b['follower_count'])).lower()
        print(f"comparison: {comparison}")
        
        if guess == comparison:
            score +=1
            print("You are correct!")
            print(f"Your score is {score}")
            
        else:
            print("You are wrong!")
            print(f"Your final score is {score}")
            play_again()
            
            
            #TODO: Create a function to ask the user if they want to play again
def play_again():
    """Asks the user if they want to play again"""
    play_again = (input(f"Do you want to play again? Type 'y' or 'n': ")).lower()
    if play_again == 'y':
        clear()  
        playgame()
    elif play_again == 'n':
        clear()
        game_over = True
        print("Thank you for playing")   

playgame()