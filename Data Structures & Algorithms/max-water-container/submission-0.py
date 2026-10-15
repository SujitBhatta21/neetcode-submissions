class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        area = 0

        while l <= r:
            curr_area = min(height[l], height[r]) * (r - l)
            area = max(area, curr_area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1


        return area