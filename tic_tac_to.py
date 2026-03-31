# Input
# ["TicTacToe", "move", "move", "move", "move", "move", "move"]
# [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2]]
# Output
# [null, 0, 0, 0, 0, 0, 2]
#
# Explanation
# TicTacToe ticTacToe = new TicTacToe(3);
# // Assume that player 1 is "X" and player 2 is "O"
# Board after move("X", 0, 0) =
# |	X	|	 	|	 	|
# |	 	|	 	|	 	|
# |	 	|	 	|	 	|
# move("X", 0, 0); // return 0 (no one wins)
# Board after move("O", 0, 2) =
# |	X	|	 	|	O	|
# |	 	|	 	|	 	|
# |	 	|	 	|	 	|
# move("O", 0, 2); // return 0 (no one wins)
# Board after move("X", 2, 2) =
# |	X	|	 	|	O	|
# |	 	|	 	|	 	|
# |	 	|	 	|	X	|
# move("X", 2, 2); // return 0 (no one wins)
# Board after move("O", 1, 1) =
# |	X	|	 	|	O	|
# |	 	|	O	|	 	|
# |	 	|	 	|	X	|
# move("O", 1, 1); // return 0 (no one wins)
# Board after move("X", 2, 0) =
# |	X	|	 	|	O	|
# |	 	|	O	|	 	|
# |	X	|	 	|	X	|
# move("X", 2, 0); // return 0 (no one wins)
# Board after move("O", 1, 0) =
# |	X	|	 	|	O	|
# |	O	|	O	|	 	|
# |	X	|	 	|	X	|
# move("O", 1, 0); // return 2 (player 2 wins, because there is a row with three 'O's).
from distutils.command.check import check

class TicTacTo:

    def __init__(self, n):
        self.number = n
        self.board = [[' ' for i in range(n)] for j in range(n)]
        self.number_of_moves = 0

    def move(self, player, x, y):

        if self.number_of_moves == self.number *self.number:
            return -2

        self.board[x][y] = player
        self.number_of_moves += 1

        def check_row(x, y, player):
            for i in range(self.number):
                if self.board[x][i] != player:
                    return False
            return True

        def check_col(x, y, player):
            for i in range(self.number):
                if self.board[i][y] != player:
                    return False
            return True

        def check_diagonal(x, y, player):
            if x != y:  # cell not on the diagonal, skip
                return False
            for i in range(self.number):
                if self.board[i][i] != player:
                    return False
            return True

        def check_anti_diagonal(x, y, player):
            if x + y != self.number - 1:  # cell not on the anti-diagonal, skip
                return False
            for i in range(self.number):
                if self.board[i][self.number - 1 - i] != player:
                    return False
            return True

        if check_row(x, y, player):
            return player
        elif check_col(x,y, player):
            return player
        elif check_diagonal(x,y, player):
            return player
        elif check_anti_diagonal(x, y, player):
            return player
        return -1


if __name__ == "__main__":

    # Test 1: Example from the problem (player 2 wins via row)
    print("Test 1: Player 2 wins via row")
    t = TicTacTo(3)
    print(t.move(1, 0, 0))  # expected -1  → board[0][0] = 1
    print(t.move(2, 1, 0))  # expected -1  → board[1][0] = 2
    print(t.move(1, 0, 1))  # expected -1  → board[0][1] = 1
    print(t.move(2, 1, 1))  # expected -1  → board[1][1] = 2
    print(t.move(1, 2, 2))  # expected -1  → board[2][2] = 1 (blocks diagonal)
    print(t.move(2, 1, 2))

    # Test 2: Player 1 wins via column
    print("\nTest 2: Player 1 wins via column")
    t = TicTacTo(3)
    print(t.move(1, 0, 0))  # expected -1
    print(t.move(2, 0, 1))  # expected -1
    print(t.move(1, 1, 0))  # expected -1
    print(t.move(2, 1, 1))  # expected -1
    print(t.move(1, 2, 0))  # expected 1

    # Test 3: Player 1 wins via diagonal
    print("\nTest 3: Player 1 wins via diagonal")
    t = TicTacTo(3)
    print(t.move(1, 0, 0))  # expected -1
    print(t.move(2, 0, 1))  # expected -1
    print(t.move(1, 1, 1))  # expected -1
    print(t.move(2, 0, 2))  # expected -1
    print(t.move(1, 2, 2))  # expected 1

    # Test 4: Player 2 wins via anti-diagonal
    print("\nTest 4: Player 2 wins via anti-diagonal")
    t = TicTacTo(3)
    print(t.move(1, 0, 0))  # expected -1
    print(t.move(2, 0, 2))  # expected -1
    print(t.move(1, 1, 0))  # expected -1
    print(t.move(2, 1, 1))  # expected -1
    print(t.move(1, 2, 2))  # expected -1
    print(t.move(2, 2, 0))  # expected 2

    # Test 5: Draw (board full, no winner)
    print("\nTest 5: Draw")
    t = TicTacTo(3)
    print(t.move(1, 0, 0))  # expected -1
    print(t.move(2, 0, 1))  # expected -1
    print(t.move(1, 0, 2))  # expected -1
    print(t.move(2, 1, 0))  # expected -1
    print(t.move(1, 1, 2))  # expected -1
    print(t.move(2, 1, 1))  # expected -1
    print(t.move(1, 2, 1))  # expected -1
    print(t.move(2, 2, 2))  # expected -1
    print(t.move(1, 2, 0))  # expected -1