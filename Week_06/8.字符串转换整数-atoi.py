#
# @lc app=leetcode.cn id=8 lang=python
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i=0
        n=len(str)
        while i<n and str[i]==' ':
            i=i+1
        if n==0 or i==n:
            return 0
        flag=1
        if str[i]=='-':
            flag=-1
        if str[i]=='+' or str[i]=='-':
            i=i+1
        INT_MAX=2**31-1
        INT_MIN=-2**31
        ans=0
        while i<n and '0'<=str[i]<='9':
            ans=ans*10+int(str[i])-int('0')
            i+=1
            if(ans-1>INT_MAX):
                break

        ans=ans*flag
        if ans>INT_MAX:
            return INT_MAX
        return INT_MIN if ans<INT_MIN else ans
# @lc code=end

