# 🎮 Game Zone

**Game Zone** is a collection of **six classic games** built using **Python** and **Streamlit**, offering a simple, interactive arcade experience in the browser. Whether you enjoy reflex-based, logic, or memory games — this bundle has something for everyone.

---

## 🕹️ Games Included

### 1. 🪨📜✂️ Rock-Paper-Scissors
- Play against a computer opponent
- Fun emoji-based UI
- Randomized opponent choices
- Interactive result display

### 2. ❌⭕ Tic-Tac-Toe
- Two-player game (X vs O)
- Instant win/draw detection
- Session state-based move tracking
- Easy restart button

### 3. 🏓 Pong
- Keyboard-controlled Pong game using **Pygame**
- Left player: `W/S` | Right player: `↑/↓`
- Ball bouncing and collision physics
- Score tracking in Streamlit session

### 4. 🐍 Snake Game
- Classic snake game recreated in Python
- Collect food and avoid collisions
- Growing snake mechanic
- Score display and game-over detection

### 5. 🧠 Memory Puzzle
- Flip tiles and match pairs
- Tracks number of moves
- Highlights matched tiles
- Good for training short-term memory

### 6. 🔤 Hangman
- Guess letters of a hidden word
- Tracks incorrect guesses with visual hangman states
- Displays correct and incorrect letters
- Word list is randomly selected

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Game Logic:** Python
- **Additional Tools:**
  - `pygame` (for Pong and Snake)
  - `numpy` (Tic-Tac-Toe)
  - `random` (RPS, Hangman, Memory)
  - `time`, `os`, `string` as needed

---

## 📁 Project Structure

```
Game-Zone/
├── Pong.py                 # Pong game using Pygame
├── Rock-Paper.py           # Rock-Paper-Scissors game
├── Tic-Tac-Toe.py          # Classic 3x3 Tic Tac Toe
├── Snake.py                # Snake game (Pygame or Canvas-based)
├── Memory-Puzzle.py        # Memory flip card puzzle
├── Hangman.py              # Hangman word guessing game
└── README.md               # Documentation
```

---

## ▶️ How to Run

Install dependencies:

```bash
pip install streamlit pygame numpy
```

Then run each game using:

```bash
streamlit run Pong.py
streamlit run Rock-Paper.py
streamlit run Tic-Tac-Toe.py
streamlit run Snake.py
streamlit run Memory-Puzzle.py
streamlit run Hangman.py
```

> 🔁 Each game runs as an independent Streamlit app  
> ⚠️ Games like Pong and Snake require keyboard input and may need local desktop execution (not suitable for Streamlit Cloud)

---

## 🧩 Future Improvements

- Add a homepage to launch all games from one interface
- Track high scores across sessions
- Add multiplayer/online support for some games
- Enhance mobile responsiveness

---

## 👤 Author

**Amritanshu Bhardwaj**  
AI & Data Science Department  
BMS College of Engineering  

---
