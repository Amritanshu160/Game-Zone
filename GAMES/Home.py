import streamlit as st

st.set_page_config(page_title="Mini Game Hub", layout="centered")

st.title("🎮 Welcome to the Mini Game Hub!")
st.markdown("Enjoy a collection of classic games, each designed for fun and quick play!")

st.markdown("---")

st.subheader("🕵️ Hangman")
st.write("Guess the hidden word one letter at a time. Be careful — too many wrong guesses and it's game over!")

st.subheader("🧠 Memory Puzzle")
st.write("Test your memory by flipping cards to find matching pairs. The fewer moves you make, the better!")

st.subheader("🏓 Pong")
st.write("Relive the arcade era! Control the paddle and try to bounce the ball past your opponent.")

st.subheader("🐍 Snake Game")
st.write("Control a growing snake as it eats food. Don't crash into the walls or yourself!")

st.subheader("✊✋✌️ Rock Paper Scissors")
st.write("A simple game of luck and strategy. Choose rock, paper, or scissors and see if you can beat the computer!")

st.subheader("⭕❌ Tic-Tac-Toe")
st.write("Play the classic game of Xs and Os. Get three in a row before your opponent does!")

st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")

