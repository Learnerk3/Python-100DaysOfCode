from tracemalloc import start
from art import logo as lg
import random
import os

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_cards = []
computer_cards = []
dealer_score = 0
computer_score = 0

def draw_card():
    return random.choice(CARDS)

def dealer_card():
    if len(dealer_cards) == 0:
        for i in range(len(dealer_cards) + 2):
            dealer_cards.append(draw_card())
    else:
        dealer_cards.append(draw_card())
    return sum(dealer_cards)

def computer_card():
    computer_cards.append(draw_card())
    return sum(computer_cards)

def winner(d_score, c_score):
    if d_score == 21:
        print("Win with a Blackjack.")
    elif c_score == 21:
        print("Opponent Win.")
    elif c_score == d_score:
        print("Draw.")
    elif d_score > 21:
        print("You went over. Opponent wins.")
    elif c_score > 21:
        print("Opponent went over. You win.")
    elif c_score > d_score:
        print("Opponent Wins.")
    else:
        print("You win.")

startGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if startGame == "y":
    print(lg)
    game_Over = False

dealer_score = dealer_card()
computer_score = computer_card()
while not game_Over:
    print(f"    Your cards: {dealer_cards}, current score: {dealer_score}")
    print(f"    Computer's first card: {computer_cards[0]}")
    if dealer_cards == 21:
        dealer_score = 0
        print(f"    Your final hand: {dealer_cards}, final score: {dealer_score}")
        while computer_score < 17:
            computer_score = computer_card()
        print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
        winner(dealer_score, computer_score)
    user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_choice == 'y':
        dealer_score = dealer_card()
        print(f"    Your cards: {dealer_cards}, current score: {dealer_score}")
        print(f"    Computer's first card: {computer_cards[0]}")
    else:
        print(f"    Your final hand: {dealer_cards}, final score: {dealer_score}")
        while computer_score < 17:
            computer_score = computer_card()
        print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
        winner(dealer_score, computer_score)
    startGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if startGame != "y":
        game_Over = True
    else:
        os.system("cls")
        print(lg)

    



    



