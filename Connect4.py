import random

class ConnectFour:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.player_turn = 'X'
        self.computer_turn = 'O'

    def print_board(self):
        print("  1 | 2 | 3 | 4 | 5 | 6 | 7")
        print("-"*29)
        for i, row in enumerate(self.board[::-1]):
            print(f"{chr(65+5-i)} | " + " | ".join(row))
            print("-"*29)

    def is_valid(self, column):
        return self.board[5][column] == ' '

    def get_next_open_row(self, column):
        for row in range(6):
            if self.board[row][column] == ' ':
                return row

    def drop_piece(self, column, piece):
        row = self.get_next_open_row(column)
        self.board[row][column] = piece

    def winning_move(self, piece):
        for c in range(7-3):
            for r in range(6):
                if self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == piece:
                    return True

        for c in range(7):
            for r in range(6-3):
                if self.board[r][c] == piece and self.board[r+1][c] == piece and self.board[r+2][c] == piece and self.board[r+3][c] == piece:
                    return True

        for c in range(7-3):
            for r in range(6-3):
                if self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                    return True

        for c in range(7-3):
            for r in range(3, 6):
                if self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                    return True

    def computer_move(self):
        possible_moves = [i for i, x in enumerate(self.board[5]) if x == " "]
        move = random.choice(possible_moves)
        self.drop_piece(move, self.computer_turn)

    def play(self):
        while True:
            self.print_board()
            column = int(input("Your turn. Which column? ")) - 1
            if self.is_valid(column):
                self.drop_piece(column, self.player_turn)
                if self.winning_move(self.player_turn):
                    self.print_board()
                    print("You win!")
                    break
                self.computer_move()
                if self.winning_move(self.computer_turn):
                    self.print_board()
                    print("Computer wins!")
                    break
            else:
                print("Invalid move! Try again.")

if __name__ == '__main__':
    game = ConnectFour()
    game.play()