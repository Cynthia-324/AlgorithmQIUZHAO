#
# @lc app=leetcode.cn id=647 lang=python
#
# [647] 回文子串
#

# @lc code=start
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = n
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
        for j in range(1,n):
            for i in range(0,j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = 0
                if dp[i][j] == 1:
                    res += 1
        return res
        
# @lc code=end

