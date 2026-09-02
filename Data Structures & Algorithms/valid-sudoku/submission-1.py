class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # iterate through each value
            # check if there is any duplicate number in each row
            # check if there is any duplicate number in each column
            # check if there is any duplicate in each box

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]

        # boxes = {}
        # boxes[(0,0)] = set()
        # boxes[(0,1)] = set()
        # boxes[(0,2)] = set()
        # boxes[(1,0)] = set()
        # boxes[(1,1)] = set()
        # boxes[(1,2)] = set()
        # boxes[(2,0)] = set()
        # boxes[(2,1)] = set()
        # boxes[(2,2)] = set()

        boxes = {}
        for r_box in range(3):
            for c_box in range(3):
                boxes[(r_box, c_box)] = set()

        for r_index in range(len(board)):
            for c_index in range(len(board[0])):
                if board[r_index][c_index] == ".":
                    continue
                
                if board[r_index][c_index] in rows[r_index]:
                    return False
                else:
                    rows[r_index].add(board[r_index][c_index])
                
                if board[r_index][c_index] in cols[c_index]:
                    return False
                else:
                    cols[c_index].add(board[r_index][c_index])
                
                box = (r_index // 3, c_index // 3)
                
                if board[r_index][c_index] in boxes[box]:
                    return False
                else:
                    boxes[box].add(board[r_index][c_index])

        return True
                
        # Time complexity: O(n^2)
        # Space complexity: O(n^2)

        