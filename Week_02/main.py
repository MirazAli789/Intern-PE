class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
    
    def display_board(self):
        """Display the current state of the game board"""
        print("\n   |   |   ")
        print(f" {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} ")
        print("___|___|___")
        print("   |   |   ")
        print(f" {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} ")
        print("___|___|___")
        print("   |   |   ")
        print(f" {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} ")
        print("   |   |   ")
        print()
    
    def display_positions(self):
        """Display the position numbers for reference"""
        print("\nPosition numbers:")
        print("   |   |   ")
        print(" 1 | 2 | 3 ")
        print("___|___|___")
        print("   |   |   ")
        print(" 4 | 5 | 6 ")
        print("___|___|___")
        print("   |   |   ")
        print(" 7 | 8 | 9 ")
        print("   |   |   ")
        print()
    
    def is_valid_move(self, position):
        """Check if the move is valid"""
        if position < 1 or position > 9:
            return False
        
        row = (position - 1) // 3
        col = (position - 1) % 3
        
        return self.board[row][col] == ' '
    
    def make_move(self, position):
        """Make a move on the board"""
        row = (position - 1) // 3
        col = (position - 1) % 3
        self.board[row][col] = self.current_player
    
    def check_winner(self):
        """Check if there's a winner"""

        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        return None
    
    def is_board_full(self):
        """Check if the board is full (tie game)"""
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True
    
    def switch_player(self):
        """Switch between X and O players"""
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def reset_game(self):
        """Reset the game board for a new game"""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
    
    def play(self):
        """Main game loop"""
        print("🎮 Welcome to Tic Tac Toe! 🎮")
        print("=" * 30)
        
        while True:
            self.display_positions()
            self.display_board()
            
            print(f"Player {self.current_player}'s turn")
            
            try:
                position = int(input("Enter position (1-9): "))
                
                if not self.is_valid_move(position):
                    print("❌ Invalid move! Please choose an empty position (1-9).")
                    continue
                
                self.make_move(position)
                

                winner = self.check_winner()
                if winner:
                    self.display_board()
                    print(f"🎉 Congratulations! Player {winner} wins! 🎉")
                    break
                

                if self.is_board_full():
                    self.display_board()
                    print("🤝 It's a tie! Well played both players!")
                    break
                
                self.switch_player()
                
            except ValueError:
                print("❌ Please enter a valid number between 1 and 9.")
            except KeyboardInterrupt:
                print("\n👋 Thanks for playing! Goodbye!")
                break

        while True:
            play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
            if play_again in ['y', 'yes']:
                self.reset_game()
                self.play()
                break
            elif play_again in ['n', 'no']:
                print("👋 Thanks for playing Tic Tac Toe! Goodbye!")
                break
            else:
                print("Please enter 'y' for yes or 'n' for no.")


def main():
    """Main function to start the game"""
    game = TicTacToe()
    game.play()


if __name__ == "__main__":
    main()
