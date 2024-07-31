# Connect Four

A simple Connect Four game implemented in Python. The game allows a user to play against the computer.

## How to Play

The game is played on a 6x7 grid. Players take turns to drop their pieces into one of the columns. The first player to align four of their pieces vertically, horizontally, or diagonally wins the game.

## Features

- Human vs. Computer gameplay
- Simple text-based interface
- Valid move checks and win detection

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/ConnectFour.git
    cd ConnectFour
    ```

2. **Run the game**:
    ```bash
    python connect_four.py
    ```

## Code Overview

- `ConnectFour` class: Handles the game logic, including board setup, move validation, piece placement, win detection, and computer moves.
- `print_board`: Prints the current state of the game board.
- `is_valid`: Checks if a move is valid (i.e., if the column is not full).
- `get_next_open_row`: Gets the next available row in a column.
- `drop_piece`: Places a piece in the specified column.
- `winning_move`: Checks for a winning move.
- `computer_move`: Handles the computer's move logic.
- `is_full`: Checks if the board is full, resulting in a tie game.
- `play`: Main game loop that alternates turns between the player and the computer, handles input validation, and checks for win/tie conditions.

## Example

\`\`\`
  1 | 2 | 3 | 4 | 5 | 6 | 7
-----------------------------
F |   |   |   |   |   |   |  
-----------------------------
E |   |   |   |   |   |   |  
-----------------------------
D |   |   |   |   |   |   |  
-----------------------------
C |   |   |   |   |   |   |  
-----------------------------
B |   |   |   |   |   |   |  
-----------------------------
A |   |   |   |   |   |   |  
-----------------------------
Your turn. Choose a column (1-7): 
\`\`\`
