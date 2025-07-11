# Snake Game

A classic Snake Game implemented in Python using Pygame.

## Features

- Classic Snake gameplay
- Score tracking
- Game over screen with restart option
- Smooth controls with arrow keys
- Colorful graphics

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Make sure you have Python installed
2. Install pygame:
   ```
   pip install pygame
   ```

## How to Play

1. Run the game:
   ```
   python snake_game.py
   ```

2. Controls:
   - **Arrow Keys**: Move the snake (Up, Down, Left, Right)
   - **Space**: Restart the game (when game over)
   - **Escape**: Quit the game (when game over)

3. Game Rules:
   - Use arrow keys to control the snake
   - Eat the red food to grow and increase your score
   - Avoid hitting the walls or the snake's own body
   - The game gets more challenging as the snake grows longer

## Game Features

- **Score System**: Each food eaten increases your score by 1
- **Collision Detection**: Game ends if snake hits walls or itself
- **Food Placement**: Food appears randomly on the game board
- **Restart Feature**: Press Space after game over to play again

## Controls Summary

| Key | Action |
|-----|--------|
| ↑ | Move Up |
| ↓ | Move Down |
| ← | Move Left |
| → | Move Right |
| Space | Restart Game |
| Esc | Quit Game |

## Tips

- Plan your moves ahead to avoid trapping yourself
- Try to keep the snake in open areas
- The snake cannot reverse direction directly (e.g., can't go left if moving right)

Enjoy playing the Snake Game!
