# 📘 Assignment: Games in Python

## 🎯 Objective

Build the classic word-guessing Hangman game using Python to practice string manipulation, loops, conditionals, and user input handling.

## 📝 Tasks

### 🛠️	Word Selection and Game Setup

#### Description
Create the foundation for your Hangman game by implementing word selection and basic game state tracking.

#### Requirements
Completed program should:

- Define a list of at least 5 words for the game
- Randomly select a word from the list using the `random` module
- Initialize variables to track the hidden word (e.g., `_ _ _ _` format)
- Set up a counter for remaining attempts (e.g., 6 attempts)


### 🛠️	Game Logic and User Interaction

#### Description
Implement the main game loop that accepts player guesses and updates the game state accordingly.

#### Requirements
Completed program should:

- Accept letter guesses from the player using `input()`
- Check if the guessed letter is in the word
- Update the displayed word to reveal correctly guessed letters
- Decrease remaining attempts for incorrect guesses
- Track and display all previously guessed letters
- Continue the loop until the word is guessed or attempts run out


### 🛠️	Win/Lose Conditions and Messages

#### Description
Add game-ending logic with appropriate win or lose messages for the player.

#### Requirements
Completed program should:

- Detect when the player has guessed all letters (win condition)
- Detect when attempts reach zero (lose condition)
- Display a congratulatory message when the player wins
- Display the correct word and an encouraging message when the player loses
- Ask if the player wants to play again (optional enhancement)
