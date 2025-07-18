class ConnectFourCLI:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player = 1
        
    def display_board(self):
        """Display the current state of the board"""
        print("\n" + "=" * 29)
        print("  1   2   3   4   5   6   7")
        print("+" + "---+" * 7)
        
        for row in reversed(self.board):
            print("|", end="")
            for cell in row:
                if cell == 1:
                    print(" X ", end="|")
                elif cell == 2:
                    print(" O ", end="|")
                else:
                    print("   ", end="|")
            print()
            print("+" + "---+" * 7)
            
    def is_valid_move(self, col):
        """Check if a move is valid"""
        if col < 0 or col >= self.cols:
            return False
        return self.board[self.rows - 1][col] == ' '
        
    def make_move(self, col, player):
        """Make a move in the specified column"""
        for row in range(self.rows):
            if self.board[row][col] == ' ':
                self.board[row][col] = player
                return True
        return False
        
    def check_winner(self, player):
        """Check if the current player has won"""
        # Check horizontal
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row][col + i] == player for i in range(4)):
                    return True
                    
        # Check vertical
        for row in range(self.rows - 3):
            for col in range(self.cols):
                if all(self.board[row + i][col] == player for i in range(4)):
                    return True
                    
        # Check diagonal (positive slope)
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if all(self.board[row + i][col + i] == player for i in range(4)):
                    return True
                    
        # Check diagonal (negative slope)
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row - i][col + i] == player for i in range(4)):
                    return True
                    
        return False
        
    def is_board_full(self):
        """Check if the board is full"""
        return all(self.board[self.rows - 1][col] != ' ' for col in range(self.cols))
        
    def get_player_symbol(self, player):
        """Get the symbol for the current player"""
        return 'X' if player == 1 else 'O'
        
    def get_player_name(self, player):
        """Get the name for the current player"""
        return f"Player {player} ({self.get_player_symbol(player)})"
        
    def play(self):
        """Main game loop"""
        print("Welcome to Connect Four!")
        print("Player 1 is X, Player 2 is O")
        print("Enter column number (1-7) to drop your piece")
        print("Type 'quit' to exit the game")
        
        while True:
            self.display_board()
            
            # Get player input
            current_player_name = self.get_player_name(self.current_player)
            try:
                move = input(f"\n{current_player_name}, enter your move (1-7): ").strip()
                
                if move.lower() == 'quit':
                    print("Thanks for playing!")
                    break
                    
                col = int(move) - 1  # Convert to 0-based index
                
                if not self.is_valid_move(col):
                    print("Invalid move! Column is full or doesn't exist. Try again.")
                    continue
                    
                # Make the move
                self.make_move(col, self.current_player)
                
                # Check for winner
                if self.check_winner(self.current_player):
                    self.display_board()
                    print(f"\n🎉 {current_player_name} wins! 🎉")
                    
                    # Ask if they want to play again
                    play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
                    if play_again == 'y':
                        self.__init__()  # Reset the game
                        continue
                    else:
                        print("Thanks for playing!")
                        break
                        
                # Check for tie
                if self.is_board_full():
                    self.display_board()
                    print("\n🤝 It's a tie! The board is full. 🤝")
                    
                    # Ask if they want to play again
                    play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
                    if play_again == 'y':
                        self.__init__()  # Reset the game
                        continue
                    else:
                        print("Thanks for playing!")
                        break
                        
                # Switch players
                self.current_player = 2 if self.current_player == 1 else 1
                
            except ValueError:
                print("Please enter a valid number (1-7) or 'quit'")
            except KeyboardInterrupt:
                print("\n\nThanks for playing!")
                break

if __name__ == "__main__":
    game = ConnectFourCLI()
    game.play()
