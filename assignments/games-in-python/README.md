# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python using strings, loops, conditionals, and user input. This assignment helps students practice handling game state, validating guesses, and updating output dynamically.

## 📝 Tasks

### 🛠️ Set Up the Game Logic

#### Description
Create a simple Hangman game that randomly selects a secret word and allows the player to guess letters one at a time.

#### Requirements
Completed program should:

- Use a predefined list of words and randomly choose one at the start of the game.
- Display the word as blanks or underscores for unguessed letters, such as `_ _ _ _ _`.
- Accept single-letter guesses from the user using `input()`.
- Update the displayed word after each correct guess.
- Keep track of how many incorrect guesses the player has left.

### 🛠️ Add Win/Lose Conditions and Feedback

#### Description
Finish the game by checking whether the player has guessed the word or exhausted all attempts, and provide clear feedback at the end.

#### Requirements
Completed program should:

- End the game when the player correctly guesses the entire word.
- End the game when the player runs out of allowed attempts.
- Tell the player whether they won or lost at the end of the game.
- Show which letters have already been guessed to avoid repeated input.
- Display a friendly message after each guess to indicate whether it was correct or incorrect.
