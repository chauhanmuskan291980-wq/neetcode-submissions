class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for row in range(9):
            seen = set()

            for col in range(9):
                value = board[row][col]

                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        # Check columns
        for col in range(9):
            seen = set()

            for row in range(9):
                value = board[row][col]

                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        # Check 3x3 boxes
        for box_row in range(3):
            for box_col in range(3):

                seen = set()

                start_row = box_row * 3
                start_col = box_col * 3

                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):

                        value = board[row][col]

                        if value == ".":
                            continue

                        if value in seen:
                            return False

                        seen.add(value)

        return True
        