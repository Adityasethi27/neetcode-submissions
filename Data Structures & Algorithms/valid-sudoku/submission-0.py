from typing import List


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Check Rows
        for i in range(9):
            s = set()
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                if value in s:
                    return False
                s.add(value)

        # 2. Check Columns
        for col in range(9):
            s = set()
            for row in range(9):
                value = board[row][col]
                if value == ".":
                    continue
                if value in s:
                    return False
                s.add(value)

        # 3. Check 3x3 Subgrids
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                s = set()
                for i in range(3):
                    for j in range(3):
                        val = board[row + i][col + j]
                        if val == ".":
                            continue
                        if val in s:
                            return False
                        s.add(val)

        return True