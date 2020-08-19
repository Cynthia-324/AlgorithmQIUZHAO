#
# @lc app=leetcode.cn id=91 lang=python
#
# [91] 解码方法
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        dp = [1 for i in range(len(s)+1)]
        for i in range(1,len(s)):
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    dp[i+1] = dp[i-1]
                else:
                    return 0
            else:
                if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
                    dp[i+1] = dp[i] + dp[i-1]
                else:
                    dp[i+1] = dp[i]
        
        return dp[len(s)]
# @lc code=end

