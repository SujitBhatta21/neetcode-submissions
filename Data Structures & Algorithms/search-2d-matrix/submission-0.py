class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = [0, 0]
        last_length = len(matrix) - 1
        high = [len(matrix) - 1, len(matrix[0]) - 1]


        while low[0] <= high[0] and low[1] <= high[1]:
            mid = [(low[0] + high[0]) // 2, (low[1] + high[1]) // 2]

            if matrix[mid[0]][mid[1]] == target:
                return True
            else:
                if matrix[mid[0]][mid[1]] > target:
                    if matrix[mid[0]][0] > target:
                        high = [mid[0] - 1, len(matrix[mid[0]]) - 1]
                    else:
                        high[1] = mid[1] - 1
                else:
                    # current_n_last_length
                    n = len(matrix[mid[0]]) - 1
                    if matrix[mid[0]][n] < target:
                        low[0] = mid[0] + 1
                    else:
                        low[1] = mid[1] + 1


        return False

          
            