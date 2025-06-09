import streamlit as st
import numpy as np
import time
import random
from streamlit_drawable_canvas import st_canvas

# Constants
grid_size = 20
tile_size = 20
game_speed = 0.2

# Initialize session state
if 'snake' not in st.session_state:
    st.session_state.snake = [(5, 5)]
    st.session_state.food = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
    st.session_state.direction = "RIGHT"
    st.session_state.game_over = False

def move_snake():
    head_x, head_y = st.session_state.snake[-1]
    if st.session_state.direction == "UP":
        head_y -= 1
    elif st.session_state.direction == "DOWN":
        head_y += 1
    elif st.session_state.direction == "LEFT":
        head_x -= 1
    elif st.session_state.direction == "RIGHT":
        head_x += 1
    
    new_head = (head_x, head_y)
    
    # Check for collisions
    if new_head in st.session_state.snake or head_x < 0 or head_x >= grid_size or head_y < 0 or head_y >= grid_size:
        st.session_state.game_over = True
        return
    
    st.session_state.snake.append(new_head)
    
    # Check for food
    if new_head == st.session_state.food:
        st.session_state.food = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
    else:
        st.session_state.snake.pop(0)

def draw_game():
    canvas = np.zeros((grid_size, grid_size, 3), dtype=np.uint8)
    
    for x, y in st.session_state.snake:
        canvas[y, x] = [0, 255, 0]  # Green for snake
    
    fx, fy = st.session_state.food
    canvas[fy, fx] = [255, 0, 0]  # Red for food
    
    return canvas

# UI
st.title("🐍 Snake Game")

# Controls
col1, col2, col3 = st.columns(3)
if col1.button("⬅️ Left"):
    if st.session_state.direction != "RIGHT":
        st.session_state.direction = "LEFT"
if col2.button("⬆️ Up"):
    if st.session_state.direction != "DOWN":
        st.session_state.direction = "UP"
if col3.button("➡️ Right"):
    if st.session_state.direction != "LEFT":
        st.session_state.direction = "RIGHT"
if st.button("⬇️ Down"):
    if st.session_state.direction != "UP":
        st.session_state.direction = "DOWN"

if st.session_state.game_over:
    st.error("Game Over! Refresh to restart.")
else:
    move_snake()
    st.image(draw_game(), width=400)
    time.sleep(game_speed)
    st.experimental_rerun()
