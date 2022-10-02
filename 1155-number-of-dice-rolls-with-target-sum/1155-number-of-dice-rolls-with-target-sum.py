class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:    
        dp = [1] + [0 for _ in range(target)]
        
        for _ in range(d):
            for t in range(target, -1, -1):
                dp[t] = sum(dp[max(0, t - f) : t])
        
        return dp[target] % (10 ** 9 + 7)