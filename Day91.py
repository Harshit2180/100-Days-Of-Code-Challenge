# Question Link
# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1

        
"""
I initialized a list dp of size amount + 1, where each element is set to amount + 1 to represent an initially unreachable state. The first element was set to 0 since no coins are needed to make an amount of 0. I then iterated over every possible amount 'a' from 1 to amount. For each 'a', I checked every coin in the coins list. If the current coin could contribute to forming the amount, I updated dp[a] by taking the minimum of its current value and 1 + dp[a - c], which represents adding one coin to the solution for a - c. Finally, if dp[amount] was still set to its initial value, it meant that forming the amount was impossible, so I returned -1. Otherwise, I returned dp[amount], which represented the minimum number of coins required.
"""