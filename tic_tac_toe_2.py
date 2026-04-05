# https://www.hack2hire.com/companies/databricks/coding-questions/684c9251cab8e9bb7ea93aeb/practice?questionId=684cd590cab8e9bb7ea93b11

from typing import List, Optional

class TicTacToe:
    def __init__(self, n: int, m: int, k: int):
        self.rows = n
        self.cols = m
        self.k = k
        self.board = [[0] * m for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        def check_win(row, col, player):
                dirs = [[0, 1], [1, 0], [1, 1], [1, -1]]

                for dir in dirs:
                    count = 1
                    r = row + dir[0]
                    c = col + dir[1]

                    while r >=0 and r < self.rows and c>=0 and c < self.cols and self.board[r][c] == player:
                        r += dir[0]
                        c += dir[1]
                        count +=1
                    r = row - dir[0]
                    c = col - dir[1]
                    while r >=0 and r < self.rows and c>=0 and c < self.cols and self.board[r][c] == player:
                        r -= dir[0]
                        c -= dir[1]
                        count+=1

                    if count >= self.k:
                        return True
                return False


        if check_win(row, col, player):
            return player
        return 0

