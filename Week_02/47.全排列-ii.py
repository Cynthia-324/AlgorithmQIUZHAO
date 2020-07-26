#
# @lc app=leetcode.cn id=47 lang=python
#
# [47] 全排列 II
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []
        used = [0 for _ in range(len(nums))]
        nums.sort()
        self.dfs(nums,res,path,used,0)
        return res
    def dfs(self,nums,res,path,used,usednums):
        if usednums == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if(used[i] == 0):
                #上一个相同的元素刚刚用过，处在同一层，被置0，则跳过
                if(i>0 and nums[i] == nums[i-1] and used[i-1] == 0):
                    continue
                used[i] = 1
                path.append(nums[i])
                self.dfs(nums,res,path,used,usednums+1)
                used[i] = 0
                path.pop()
        return

# @lc code=end

