#
# @lc app=leetcode.cn id=64 lang=python
#
# [64] 最小路径和
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]

        dp[0][0] = grid[0][0]
        for i in range(1,len(grid)):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1,len(grid[0])):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                dp[i][j] = min(dp[i-1][j],dp[j][i-1])+grid[i][j]
        return dp[len(grid)-1][len(grid[0])-1]
# @lc code=end

