#
# @lc app=leetcode.cn id=33 lang=python
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left+1)//2
            #[mid,right]数组有序
            if nums[mid] < nums[right]:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1
            #[left,mid-1]有序
            else:
                if nums[left] <= target <= nums[mid-1]:
                    right = mid -1
                else:
                    left = mid
        if nums[left] == target: return left
        else: return -1
                


# @lc code=end

