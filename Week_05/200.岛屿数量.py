#
# @lc app=leetcode.cn id=200 lang=python
#
# [200] 岛屿数量
#

# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid,i,j):
            if not 0 <= i <= len(grid) or not 0 <= j <= len(grid[0]) or grid[i][j] == '0':return
            grid[i][j] = '0'
            dfs(grid,i-1,j)
            dfs(grid,i+1,j)
            dfs(grid,i,j-1)
            dfs(grid,i,j+1)
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dfs(grid,i,j)
                res += 1
        return res
# @lc code=end

