#
# @lc app=leetcode.cn id=547 lang=python
#
# [547] 朋友圈
#

# @lc code=start
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        count = 0
        visited = set()
        
        def dfs(i):
            for j in range(N):
                if M[i][j] and j not in visited:
                    visited.add(j)
                    dfs(j)
        
        for i in range(N):
            if  i not in visited:
                count += 1
                visited.add(i)
                dfs(i)
        
        return count 

# @lc code=end

