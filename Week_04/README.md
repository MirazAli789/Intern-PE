# Connect Four Game

This project contains two versions of the classic Connect Four game implemented in Python:

## 🎮 Game Versions

### 1. Graphical Version (`connect_four.py`)
- **Features:**
  - Beautiful pygame-based GUI
  - Real-time piece preview
  - Visual feedback for wins/ties
  - Mouse click controls
  - Restart functionality

- **How to Play:**
  - Run the graphical version
  - Click on any column to drop your piece
  - Player 1 (Red) goes first, followed by Player 2 (Yellow)
  - Get four pieces in a row (horizontally, vertically, or diagonally) to win!
  - Press 'R' to restart or 'Q' to quit when the game ends

### 2. Command Line Version (`connect_four_cli.py`)
- **Features:**
  - Text-based interface
  - No external dependencies
  - Simple number input system
  - Play again option

- **How to Play:**
  - Run the command line version
  - Enter column numbers (1-7) to drop your piece
  - Player 1 (X) goes first, followed by Player 2 (O)
  - Type 'quit' to exit anytime
  - Get four pieces in a row to win!

## 🚀 How to Run

### Graphical Version (Recommended)
```bash
python connect_four.py
```

### Command Line Version
```bash
python connect_four_cli.py
```

## 📋 Requirements

- **For Graphical Version:** Python 3.6+ and pygame
- **For Command Line Version:** Python 3.6+ (no additional packages needed)

## 🎯 Game Rules

1. **Objective:** Be the first player to get four of your pieces in a row
2. **Gameplay:** 
   - Players take turns dropping pieces into columns
   - Pieces fall down due to gravity
   - Win by getting 4 pieces in a row: horizontally, vertically, or diagonally
3. **Winning:** The game ends when a player gets four in a row or the board is full (tie)

## 🎨 Features

- **Smart Win Detection:** Automatically detects wins in all directions
- **Input Validation:** Prevents invalid moves
- **Visual Feedback:** Clear indication of game state
- **Restart Option:** Easy way to play multiple games
- **Tie Detection:** Handles full board scenarios

## 🛠️ Technical Details

- **Board Size:** 6 rows × 7 columns (standard Connect Four)
- **Graphics:** Pygame-based with smooth rendering
- **Colors:** Red for Player 1, Yellow for Player 2
- **Error Handling:** Robust input validation and error messages

Enjoy playing Connect Four! 🎉
