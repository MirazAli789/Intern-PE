import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
ROWS = 6
COLS = 7
CELL_SIZE = 100
RADIUS = int(CELL_SIZE/2 - 5)

# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Screen dimensions
WIDTH = COLS * CELL_SIZE
HEIGHT = (ROWS + 1) * CELL_SIZE

class ConnectFour:
    def __init__(self):
        self.board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.current_player = 1  # 1 for Player 1 (Red), 2 for Player 2 (Yellow)
        self.game_over = False
        self.winner = None
        
        # Initialize Pygame screen
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Connect Four")
        self.clock = pygame.time.Clock()
        
        # Font for displaying text
        self.font = pygame.font.Font(None, 36)
        
    def drop_piece(self, row, col, piece):
        """Drop a piece into the board"""
        self.board[row][col] = piece
        
    def is_valid_location(self, col):
        """Check if a column is valid for placing a piece"""
        return self.board[ROWS-1][col] == 0
        
    def get_next_open_row(self, col):
        """Get the next available row in a column"""
        for r in range(ROWS):
            if self.board[r][col] == 0:
                return r
                
    def winning_move(self, piece):
        """Check if the current move results in a win"""
        # Check horizontal locations
        for c in range(COLS-3):
            for r in range(ROWS):
                if (self.board[r][c] == piece and 
                    self.board[r][c+1] == piece and 
                    self.board[r][c+2] == piece and 
                    self.board[r][c+3] == piece):
                    return True
                    
        # Check vertical locations
        for c in range(COLS):
            for r in range(ROWS-3):
                if (self.board[r][c] == piece and 
                    self.board[r+1][c] == piece and 
                    self.board[r+2][c] == piece and 
                    self.board[r+3][c] == piece):
                    return True
                    
        # Check positively sloped diagonals
        for c in range(COLS-3):
            for r in range(ROWS-3):
                if (self.board[r][c] == piece and 
                    self.board[r+1][c+1] == piece and 
                    self.board[r+2][c+2] == piece and 
                    self.board[r+3][c+3] == piece):
                    return True
                    
        # Check negatively sloped diagonals
        for c in range(COLS-3):
            for r in range(3, ROWS):
                if (self.board[r][c] == piece and 
                    self.board[r-1][c+1] == piece and 
                    self.board[r-2][c+2] == piece and 
                    self.board[r-3][c+3] == piece):
                    return True
                    
        return False
        
    def is_board_full(self):
        """Check if the board is full (tie game)"""
        for col in range(COLS):
            if self.is_valid_location(col):
                return False
        return True
        
    def draw_board(self):
        """Draw the game board"""
        for c in range(COLS):
            for r in range(ROWS):
                pygame.draw.rect(self.screen, BLUE, 
                               (c*CELL_SIZE, r*CELL_SIZE+CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.circle(self.screen, BLACK, 
                                 (int(c*CELL_SIZE+CELL_SIZE/2), 
                                  int(r*CELL_SIZE+CELL_SIZE+CELL_SIZE/2)), RADIUS)
                
        for c in range(COLS):
            for r in range(ROWS):
                if self.board[r][c] == 1:
                    pygame.draw.circle(self.screen, RED, 
                                     (int(c*CELL_SIZE+CELL_SIZE/2), 
                                      HEIGHT-int(r*CELL_SIZE+CELL_SIZE/2)), RADIUS)
                elif self.board[r][c] == 2:
                    pygame.draw.circle(self.screen, YELLOW, 
                                     (int(c*CELL_SIZE+CELL_SIZE/2), 
                                      HEIGHT-int(r*CELL_SIZE+CELL_SIZE/2)), RADIUS)
        pygame.display.update()
        
    def draw_piece_preview(self, mouse_x):
        """Draw a preview of where the piece will be placed"""
        col = int(math.floor(mouse_x / CELL_SIZE))
        if 0 <= col < COLS and self.is_valid_location(col):
            color = RED if self.current_player == 1 else YELLOW
            pygame.draw.circle(self.screen, color, 
                             (int(col*CELL_SIZE+CELL_SIZE/2), int(CELL_SIZE/2)), RADIUS)
                             
    def display_winner(self):
        """Display the winner message"""
        if self.winner:
            winner_text = f"Player {self.winner} Wins!"
            color = RED if self.winner == 1 else YELLOW
        else:
            winner_text = "It's a Tie!"
            color = WHITE
            
        text_surface = self.font.render(winner_text, True, color)
        text_rect = text_surface.get_rect(center=(WIDTH//2, CELL_SIZE//2))
        
        # Draw semi-transparent background
        overlay = pygame.Surface((WIDTH, CELL_SIZE))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        self.screen.blit(text_surface, text_rect)
        
        # Display restart instruction
        restart_text = "Press 'R' to restart or 'Q' to quit"
        restart_surface = self.font.render(restart_text, True, WHITE)
        restart_rect = restart_surface.get_rect(center=(WIDTH//2, CELL_SIZE//2 + 40))
        self.screen.blit(restart_surface, restart_rect)
        
    def reset_game(self):
        """Reset the game to initial state"""
        self.board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.current_player = 1
        self.game_over = False
        self.winner = None
        
    def run(self):
        """Main game loop"""
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r and self.game_over:
                        self.reset_game()
                    elif event.key == pygame.K_q:
                        running = False
                        
                if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    mouse_x = event.pos[0]
                    col = int(math.floor(mouse_x / CELL_SIZE))
                    
                    if 0 <= col < COLS and self.is_valid_location(col):
                        row = self.get_next_open_row(col)
                        self.drop_piece(row, col, self.current_player)
                        
                        # Check for win
                        if self.winning_move(self.current_player):
                            self.game_over = True
                            self.winner = self.current_player
                        elif self.is_board_full():
                            self.game_over = True
                            self.winner = None  # Tie game
                        else:
                            # Switch players
                            self.current_player = 2 if self.current_player == 1 else 1
                            
            # Clear screen
            self.screen.fill(BLACK)
            
            # Draw the game board
            self.draw_board()
            
            # Draw piece preview if game is not over
            if not self.game_over:
                mouse_x = pygame.mouse.get_pos()[0]
                self.draw_piece_preview(mouse_x)
            
            # Display winner if game is over
            if self.game_over:
                self.display_winner()
                
            pygame.display.update()
            self.clock.tick(60)
            
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = ConnectFour()
    game.run()
