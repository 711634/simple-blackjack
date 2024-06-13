# simple-blackjack

To start game run "cd [file location]" then "python3 app.py"

Blackjack Game

Welcome to the Blackjack game! This project allows you to play Blackjack against a dealer either through a command-line interface (CLI) or a web-based interface.

Features:

- **Deck Creation**: A standard deck of 52 cards is shuffled for randomness.
- **Hand Value Calculation**: Card values are summed, with face cards (Jack, Queen, King) worth 10 points and Aces worth either 1 or 11 points.
- **Gameplay**:
  - **Initial Deal**: Both player and dealer are dealt two cards.
  - **Player Actions**: Choose to 'Hit' (draw a card) or 'Stand' (end your turn).
  - **Dealer Actions**: Dealer draws cards until their hand value is at least 17.
- **Game States**:
  - **New Game**: Start a new game.
  - **Hit**: Draw another card.
  - **Stand**: Dealer plays out their hand.
- **Outcome Determination**: The winner is determined based on standard Blackjack rules.

Technologies Used:

- **Python**: Backend logic and CLI game.
- **Flask**: Web framework for the web-based game.
- **JavaScript (assumed)**: Handles interactivity on the client side for the web version.
- **HTML/CSS**: Structure and style the web page.

How to Play:

1. **Command-Line Version**:
   - Run the Python script to start the game.
   - Follow prompts to 'Hit' or 'Stand' and see the results in the terminal.

2. **Web Version**:
   - Start the Flask server.
   - Open the web page to play the game.
   - Use buttons to 'Hit' or 'Stand' and see the results update dynamically.

This project combines Python’s powerful backend with Flask's web framework to offer a fun and interactive Blackjack game experience. Enjoy playing!
