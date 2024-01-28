class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        mat = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)
        
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r]) or (board[r][c] in cols[c]) or (board[r][c] in mat[(r//3,c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                mat[(r//3,c//3)].add(board[r][c])
        return True