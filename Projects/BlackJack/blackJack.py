from art import logo as lg
import random
DECK_OF_CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_cards = []
computer_cards = []
dl_score = 0
cp_score = 0
gameOver = False

def draw_card():
    return random.choice(DECK_OF_CARDS)

user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if user_choice == 'y':
    print(lg)

def dealer_card():
    dealer_cards.append(draw_card())
    if len(dealer_cards) < 2:
        dealer_cards.append(draw_card())
    print(f"    Your cards: {dealer_cards}, current score: {sum(dealer_cards)}")
    

def computer_card():
    for i in range(len(computer_cards) + 1):
        if sum(computer_cards) < 17:
            computer_cards.append(draw_card())
    print(f"    Computer's first card: {computer_cards[0]}")
    # print(computer_cards)

def winner(dl_score, cp_score):
    print(f"    Your final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
    print(f"    Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    if dl_score > 21:
        print("You went over. You lose")
    elif cp_score > 21:
        print("Computer went over. You win")
    elif dl_score == cp_score or cp_score == dl_score:
        print("Draw")
    elif cp_score < dl_score:
        print("You win")
    gameOver = True


while not gameOver:
    dealer_card()
    dl_score = sum(dealer_cards)
    computer_card()
    cp_score = sum(computer_cards)
    if dl_score == 21:
        print(f"    Your final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
        print(f"    Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        print("You win")
        gameOver = True
    else:
        user_continues = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if user_continues == 'y':
            dealer_card()
            dl_score = sum(dealer_cards)
            computer_card()
            cp_score = sum(computer_cards)
        else:
            computer_card()
            cp_score = sum(computer_cards)
    winner(dl_score, cp_score)
    if user_continues != 'y':
        gameOver = True


        
    