import streamlit as st
import random
import time
import requests
from io import BytesIO
from PIL import Image

# Constants
GRID_SIZE = 4
CARD_SIZE = 175
TIMER_LIMIT = 15

# URLs for images
image_urls = [
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311120810/f.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311121011/d.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311120802/a.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311120802/b.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311120801/c.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311122347/z.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311122913/y.webp",
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311122913/x.webp"
]

# Load images from URLs
def load_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    return image.convert("RGB")

# Load card back image
card_back = load_image("https://media.geeksforgeeks.org/wp-content/uploads/20240311145552/geeksforgeeks.png")
card_images = [load_image(url) for url in image_urls] * 2  # Duplicate images for pairs
random.shuffle(card_images)

# Streamlit UI
st.title("GeeksforGeeks Memory Puzzle Game")

# Game State
if "card_state" not in st.session_state:
    st.session_state.card_state = [False] * (GRID_SIZE ** 2)
    st.session_state.flipped_cards = []
    st.session_state.matched_pairs = 0
    st.session_state.moves = 0
    st.session_state.timer_start_time = time.time()

# Timer Logic
elapsed_time = max(0, int(time.time() - st.session_state.timer_start_time))
remaining_time = max(0, TIMER_LIMIT - elapsed_time)
st.sidebar.write(f"**Time Remaining:** {remaining_time}s")
st.sidebar.write(f"**Moves:** {st.session_state.moves}")

# Restart Button
if st.sidebar.button("Restart Game"):
    random.shuffle(card_images)
    st.session_state.card_state = [False] * (GRID_SIZE ** 2)
    st.session_state.flipped_cards = []
    st.session_state.matched_pairs = 0
    st.session_state.moves = 0
    st.session_state.timer_start_time = time.time()
    st.experimental_rerun()

# Game Grid
grid = []
for i in range(GRID_SIZE):
    row = []
    for j in range(GRID_SIZE):
        index = i * GRID_SIZE + j
        if st.session_state.card_state[index]:
            row.append(st.image(card_images[index], use_column_width=True))
        else:
            if st.button(f"Flip {index}", key=index):
                st.session_state.card_state[index] = True
                st.session_state.flipped_cards.append(index)
                st.session_state.moves += 1
                if len(st.session_state.flipped_cards) == 2:
                    idx1, idx2 = st.session_state.flipped_cards
                    if card_images[idx1] == card_images[idx2]:
                        st.session_state.matched_pairs += 1
                    else:
                        st.session_state.card_state[idx1] = False
                        st.session_state.card_state[idx2] = False
                    st.session_state.flipped_cards = []
                st.experimental_rerun()
        
    grid.append(row)

# Check for game over
if st.session_state.matched_pairs == GRID_SIZE ** 2 // 2:
    st.success("Congratulations! You found all pairs!")
    st.stop()

if remaining_time == 0:
    st.error("Time's up! You lost the game.")
    st.stop()

