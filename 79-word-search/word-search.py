class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #backtracking problem

        rows, cols = len(board), len(board[0])

        #depth first search function to search for word[index:]
        def dfs(r, c, index):
            #if all chars are matched
            if index == len(word):
                return True

            #check boundaries and character match
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[index]):
                return False

            #marking curr cell as visited
            temp = board[r][c]
            board[r][c] = "#"

            #all four directions
            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )

            #restore the cell (backtrack)
            board[r][c] = temp

            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False

        