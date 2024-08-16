from typing import List

class Solution:
    def is_safe(self, board, row, col, n):
        # Check this row on the left side
        for i in range(col):
            if board[row][i] == 1:
                return False

        # Check upper diagonal on the left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check lower diagonal on the left side
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve_n_queens(self, board, col, n, solutions):
        # Base case: If all queens are placed
        if col >= n:
            # Make a deep copy of the board and add it to the solutions list
            solutions.append([row[:] for row in board])
            return

        # Consider this column and try placing this queen in all rows one by one
        for i in range(n):
            if self.is_safe(board, i, col, n):
                # Place this queen in board[i][col]
                board[i][col] = 1

                # Recursively place the rest of the queens
                self.solve_n_queens(board, col + 1, n, solutions)

                # If placing queen in board[i][col] doesn't lead to a solution, remove the queen
                board[i][col] = 0

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[0 for _ in range(n)] for _ in range(n)]
        solutions = []
        self.solve_n_queens(board, 0, n, solutions)

        # Convert the board of 0s and 1s into the required string format
        formatted_solutions = []
        for solution in solutions:
            formatted_solution = []
            for row in solution:
                formatted_solution.append("".join("Q" if cell == 1 else "." for cell in row))
            formatted_solutions.append(formatted_solution)

        return formatted_solutions

