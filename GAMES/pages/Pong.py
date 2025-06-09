import streamlit as st
import pygame
import time

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 500
BALL_SPEED = [4, 4]
PADDLE_SPEED = 20

# Streamlit app setup
st.title("🏓 Pong Game with Streamlit")
st.write("Use W/S for the left paddle and Up/Down arrows for the right paddle.")

# Game state
if "left_score" not in st.session_state:
    st.session_state.left_score = 0
    st.session_state.right_score = 0

def game_loop():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong Game")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    
    # Paddles and ball
    left_paddle = pygame.Rect(50, HEIGHT // 2 - 40, 10, 80)
    right_paddle = pygame.Rect(WIDTH - 60, HEIGHT // 2 - 40, 10, 80)
    ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 15, 15)
    ball_speed = BALL_SPEED.copy()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle.top > 0:
            left_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
            left_paddle.y += PADDLE_SPEED
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
            right_paddle.y += PADDLE_SPEED

        # Move ball
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        # Ball collision with top/bottom
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed[1] = -ball_speed[1]

        # Ball collision with paddles
        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            ball_speed[0] = -ball_speed[0]

        # Scoring
        if ball.left <= 0:
            st.session_state.right_score += 1
            ball.center = (WIDTH // 2, HEIGHT // 2)
            ball_speed = BALL_SPEED.copy()
        if ball.right >= WIDTH:
            st.session_state.left_score += 1
            ball.center = (WIDTH // 2, HEIGHT // 2)
            ball_speed = BALL_SPEED.copy()

        # Draw everything
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, left_paddle)
        pygame.draw.rect(screen, WHITE, right_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
        pygame.display.flip()

        time.sleep(0.01)
    pygame.quit()

if st.button("Start Game"):
    game_loop()

st.write(f"**Score:** Left Player - {st.session_state.left_score}, Right Player - {st.session_state.right_score}")
