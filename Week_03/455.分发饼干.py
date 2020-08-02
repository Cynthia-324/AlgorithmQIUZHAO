#
# @lc app=leetcode.cn id=455 lang=python
#
# [455] 分发饼干
#

# @lc code=start
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        gi, sj = 0, 0
        while gi <len(g) and sj < len(s):
            if g[gi] <= s[sj]:
                gi += 1
            sj += 1
        return gi

        
# @lc code=end

