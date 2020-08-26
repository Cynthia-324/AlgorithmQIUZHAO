#
# @lc app=leetcode.cn id=32 lang=python
#
# [32] 最长有效括号
#

# @lc code=start
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        dp = [0] * n
        for i in range(1,n):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = 2
                    if i - 2 >= 0:
                        dp[i] += dp[i-2]
                elif dp[i-1] > 0:
                    if i - dp[i-1] -1 >= 0 and s[i - dp[i-1] -1] == "(":
                        dp[i] = dp[i-1] + 2
                        if i - dp[i-1] -2 >= 0:
                            dp[i] += dp[i - dp[i-1] -2]
            if dp[i] > res:
                res = dp[i]
        return res
# @lc code=end

