#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #dp[i][j] 表示从i到j是否为回文字串
        #dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        res = 1
        start = 0
        for i in range(n):
            dp[i][i] = 1
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
                    if j-i+1 > res:
                        res =  j-i+1
                        start = i

        return  s[start:start + res]

# @lc code=end

