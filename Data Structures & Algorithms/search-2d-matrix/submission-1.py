class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = [0, 0]
        len_row, len_col = len(matrix) - 1, len(matrix[0]) -1
        r = [len_row, len_col]

        while l[1] <= r[1] and l[0] <= r[0]:
            mid = [(l[0] + r[0]) // 2, (l[1] + r[1]) // 2]
            
            if matrix[mid[0]][mid[1]] == target:
                return True
            elif matrix[mid[0]][mid[1]] > target:
                if matrix[mid[0]][0] > target:
                    r = [mid[0] - 1, len_col]
                else:
                    r = [mid[0], mid[1]-1]
            else:
                if matrix[mid[0]][len_col] < target:
                    l = [mid[0] + 1, 0]
                else:
                    l = [mid[0], mid[1] + 1]

        return False