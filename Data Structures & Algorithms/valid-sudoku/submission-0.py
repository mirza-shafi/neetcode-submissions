from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        print(rows)
        print(cols)
        
        for i in range(9):
            for j in range(9):
                a = board[i][j]
                if a != ".":
                    if a in rows[i] or a in cols[j] or a in boxes[(i // 3) * 3 + (j // 3)]:
                        return False
                    rows[i].add(a)
                    cols[j].add(a)
                    boxes[(i // 3) * 3 + (j // 3)].add(a)
        return True
