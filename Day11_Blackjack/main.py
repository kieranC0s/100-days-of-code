import random
from replit import clear
from art import logo

def deal_card():
    '''Returns a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    '''Takes in a list of cards and returns the score calculated from the cards'''
    score = sum(cards)
    if score == 21:
        return 0
    if 11 in cards and score > 21:
            cards.remove(11)
            cards.append(1)
    return score

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw"
    elif computer_score == 0:
        return "You lose, opponent has Blackjack"
    elif user_score == 0:
        return "You win with a Blackjack"
    elif user_score > 21:
        return "You went over, you lose"
    elif computer_score > 21:
        return "Opponent went over, you win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
        
def play_game():

    print(logo)
    
    user_cards = []
    computer_cards = []
    is_game_over = False
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_choice = input("Type 'yes' to get another card, type 'no' to pass: ")
            if user_choice == 'yes':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    while computer_score !="0" and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"  Your final hand: {user_cards}, Your final score: {user_score}")
    print(f"  Computer's final hand: {computer_cards}, Computer final score: {computer_score}")
    print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

while input("Do you a want to play a game of Blackjack? Type 'yes' or 'no': ") == 'yes':
    clear()
    play_game()

