class Solution:
    def coinChange(self,amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype : int
        """

        dp = [amount+1]*(amount+1)
        dp[0] = 0

        for a in range(1,amount+1):
            for coin in coins:
                if a-coin >=0:
                    dp[a] = min(dp[a], 1+dp[a-c])

        return dp[amount] if dp[amount] != amount+1 else -1