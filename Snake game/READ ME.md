# Snake Game

A classic Snake game implementation in Python using Pygame.

## Features

- Classic snake gameplay
- Score tracking
- Grid-based movement
- Food spawning
- Game over detection
- Pause functionality
- Smooth controls

## Installation

1. Make sure you have Python 3.6+ installed
2. Install Pygame:
   ```bash
   pip install -r requirements.txt
   ```
   Or directly:
   ```bash
   pip install pygame
   ```

## How to Play

1. Run the game:
   ```bash
   python snake_game.py
   ```

2. Controls:
   - **Arrow Keys**: Move the snake (Up, Down, Left, Right)
   - **SPACE**: Pause/Unpause the game
   - **R**: Restart the game (when game over)
   - **ESC**: Quit the game

3. Objective:
   - Eat the red food to grow longer and increase your score
   - Avoid hitting yourself
   - The snake wraps around the screen edges

## Game Rules

- Each food eaten increases your score by 10 points
- Each food eaten makes the snake grow by 1 segment
- Game ends if the snake collides with itself
- The snake can wrap around screen edges

Enjoy playing!
