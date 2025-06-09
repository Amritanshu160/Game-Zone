import random
import streamlit as st

# Hangman drawing stages
HANGMAN_PICS = [
    '''
       +---+
           |
           |
           |
           |
           |
    =========
    ''', '''
       +---+
       O   |
           |
           |
           |
           |
    =========
    ''', '''
       +---+
       O   |
       |   |
           |
           |
           |
    =========
    ''', '''
       +---+
       O   |
      /|   |
           |
           |
           |
    =========
    ''', '''
       +---+
       O   |
      /|\\  |
           |
           |
           |
    =========
    ''', '''
       +---+
       O   |
      /|\\  |
      /    |
           |
           |
    =========
    ''', '''
       +---+
       O   |
      /|\\  |
      / \\  |
           |
           |
    =========
    '''
]

# List of words for the game
words = ['python', 'streamlit', 'hangman', 'programming', 'development']

# Choose a random word from the list
def get_random_word():
    return random.choice(words).lower()

# Display the current state of the word being guessed
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Main game logic
def main():
    st.title('Enhanced Hangman Game - Streamlit')

    # Initial game setup
    if 'word' not in st.session_state:
        st.session_state.word = get_random_word()
        st.session_state.guessed_letters = []
        st.session_state.missed_guesses = 0

    word = st.session_state.word
    guessed_letters = st.session_state.guessed_letters
    missed_guesses = st.session_state.missed_guesses

    # Show current hangman picture
    st.text(HANGMAN_PICS[missed_guesses])

    # Show guessed letters and current word state
    st.write(f"Guessed Letters: {' '.join(guessed_letters)}")
    st.write(f"Word: {display_word(word, guessed_letters)}")

    # Input for new guess
    guess = st.text_input('Guess a letter').lower()

    # Check guess on button click
    if st.button('Submit Guess'):
        if guess in guessed_letters:
            st.warning('You already guessed that letter!')
        elif guess in word:
            st.session_state.guessed_letters.append(guess)
            st.success(f'Correct! "{guess}" is in the word.')
        else:
            st.session_state.guessed_letters.append(guess)
            st.session_state.missed_guesses += 1
            st.error(f'Wrong guess! "{guess}" is not in the word.')

    # Check if the player won
    if set(word).issubset(set(guessed_letters)):
        st.balloons()  # Celebration with balloons
        st.success(f'Congratulations! You guessed the word: {word}')
        if st.button('Play Again'):
            st.session_state.word = get_random_word()
            st.session_state.guessed_letters = []
            st.session_state.missed_guesses = 0

    # Check if the player lost
    elif missed_guesses >= len(HANGMAN_PICS) - 1:
        st.error(f'Sorry, you lost! The word was: {word}')
        if st.button('Play Again'):
            st.session_state.word = get_random_word()
            st.session_state.guessed_letters = []
            st.session_state.missed_guesses = 0

if __name__ == '__main__':
    main()