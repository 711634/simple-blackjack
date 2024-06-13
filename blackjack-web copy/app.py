from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_game', methods=['POST'])
def new_game():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    game_state = {
        'deck': deck,
        'player_hand': player_hand,
        'dealer_hand': dealer_hand,
        'player_value': calculate_hand_value(player_hand),
        'dealer_value': calculate_hand_value(dealer_hand[:1])  # Only show one dealer card initially
    }
    return jsonify(game_state)

@app.route('/hit', methods=['POST'])
def hit():
    game_state = request.json
    deck = game_state['deck']
    player_hand = game_state['player_hand']
    
    player_hand.append(deck.pop())
    player_value = calculate_hand_value(player_hand)
    
    if player_value > 21:
        return jsonify({'bust': True, 'player_hand': player_hand, 'player_value': player_value})
    
    return jsonify({'bust': False, 'player_hand': player_hand, 'player_value': player_value})

@app.route('/stand', methods=['POST'])
def stand():
    game_state = request.json
    deck = game_state['deck']
    player_hand = game_state['player_hand']
    dealer_hand = game_state['dealer_hand']
    
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    return jsonify({
        'dealer_hand': dealer_hand,
        'dealer_value': dealer_value,
        'player_value': player_value,
        'result': determine_winner(player_value, dealer_value)
    })

def determine_winner(player_value, dealer_value):
    if player_value > 21:
        return "Dealer wins!"
    elif dealer_value > 21 or player_value > dealer_value:
        return "You win!"
    elif player_value < dealer_value:
        return "Dealer wins!"
    else:
        return "It's a tie!"

if __name__ == '__main__':
    app.run(debug=True)

