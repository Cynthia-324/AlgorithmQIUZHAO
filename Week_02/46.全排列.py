#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if not nums: return res
        path = []
        used = [0 for _ in range(len(nums))]
        self.dfs(nums,res,path,used,0)
        return res
    def dfs(self,nums,res,path,used,usednum):
        if usednum == len(nums):
            res.append(path[:])
            return res
        for i in range(0,len(nums)):
            if used[i] == 0:
                used[i] = 1
                path.append(nums[i])
                self.dfs(nums,res,path,used,usednum+1)
                used[i] =0
                path.pop()
        return

# @lc code=end

