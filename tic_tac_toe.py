import numpy as np

class TicTacToe:
    def __init__(self):
        self.game = np.zeros((3, 3), dtype=str)

    def is_valid(self, move):
        try:
            row, column = map(int, move.split(","))
            if self.game[row, column] == "":
                return True
        except:
            return False
        return False

    def print_game_board(self):
        for row in self.game:
            print("|".join(cell if cell != "" else " " for cell in row))
            print("-" * 5) 
        print()

    def check_winner(self):
        for i in range(3):
            if all(self.game[i, j] == self.game[i, 0] and self.game[i, 0] != "" for j in range(3)):
                return self.game[i, 0]  # Winner in a row

            if all(self.game[j, i] == self.game[0, i] and self.game[0, i] != "" for j in range(3)):
                return self.game[0, i]  # Winner in a column

        # Check diagonals
        if all(self.game[i, i] == self.game[0, 0] and self.game[0, 0] != "" for i in range(3)):
            return self.game[0, 0]  # Winner in the main diagonal

        if all(self.game[i, 2 - i] == self.game[0, 2] and self.game[0, 2] != "" for i in range(3)):
            return self.game[0, 2]  # Winner in the other diagonal

        return None 

    def update_array(self, move, symbol):
        row, column = map(int, move.split(","))
        self.game[row, column] = symbol

    def select_symbol(self):
        symbol = input("Choose Symbol 'X' or 'O' (type 'quit' to end): ")
        if symbol.lower() == "quit":
            return "quit"
        elif symbol == 'X' or symbol == 'O':
            return symbol
        else:
            print("Wrong Symbol. Please choose 'X' or 'O'.")
            return self.select_symbol()

    def make_move(self, symbol):
        move = input("Enter a Position (row, column) or type 'quit' to leave: ")
        if move.lower() == "quit":
            return "quit"
        elif self.is_valid(move):
            self.update_array(move, symbol)
        else:
            print("Invalid move. Try again.")
            return self.make_move(symbol)

    def start_game(self):
        symbol = self.select_symbol()
        if symbol == "quit":
            print("Game ended.")
            return

        last_symbol = None

        while np.any(self.game == ""):
            result = self.make_move(symbol)

            if result == "quit":
                print("Game ended. The winner is:", last_symbol)
                return

            self.print_game_board()

            if self.check_winner():
                break

            last_symbol = symbol
            symbol = 'X' if symbol == 'O' else 'O'

        if self.check_winner():
            print("The winner is:", symbol)
        else:
            print("It's a Tie")

Game = TicTacToe()
Game.start_game()