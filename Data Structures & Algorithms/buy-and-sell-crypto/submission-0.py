class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0

        for r in range(1, len(prices)):
            if buy > prices[r]:
                buy = prices[r]

            elif prices[r] - buy > res:
                res = prices[r] - buy
        return res