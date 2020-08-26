#
# @lc app=leetcode.cn id=290 lang=python
#
# [290] 单词规律
#

# @lc code=start
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        return list(map(pattern.index,pattern)) == list(map(str.index,str))
# @lc code=end

