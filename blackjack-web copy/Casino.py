import random

def create_deck():
    """Create a deck of cards."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(value, suit) for suit in suits for value in values]
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    """Calculate the value of a hand."""
    value = 0
    aces = 0
    for card in hand:
        if card[0] in ['K', 'Q', 'J']:
            value += 10
        elif card[0] == 'A':
            value += 11
            aces += 1
        else:
            value += int(card[0])
    
    # Adjust for aces
    while value > 21 and aces:
        value -= 10
        aces -= 1
    
    return value

def display_hand(hand, name):
    """Display the cards in a hand."""
    print(f"{name}'s hand: ", end='')
    for card in hand:
        print(f"{card[0]} of {card[1]}", end=', ')
    print(f"Value: {calculate_hand_value(hand)}")

def blackjack():
    """Main function to play Blackjack."""
    print("Welcome to Blackjack!")
    deck = create_deck()
    
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    display_hand(player_hand, "Player")
    print(f"Dealer shows: {dealer_hand[0][0]} of {dealer_hand[0][1]}")
    
    # Player's turn
    while True:
        action = input("Do you want to [H]it or [S]tand? ").upper()
        if action == 'H':
            player_hand.append(deck.pop())
            display_hand(player_hand, "Player")
            if calculate_hand_value(player_hand) > 21:
                print("You bust! Dealer wins.")
                return
        elif action == 'S':
            break
        else:
            print("Invalid input, please enter 'H' to Hit or 'S' to Stand.")
    
    # Dealer's turn
    display_hand(dealer_hand, "Dealer")
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        display_hand(dealer_hand, "Dealer")
        if calculate_hand_value(dealer_hand) > 21:
            print("Dealer busts! You win.")
            return
    
    # Final result
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    if player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

# Run the game
blackjack()
