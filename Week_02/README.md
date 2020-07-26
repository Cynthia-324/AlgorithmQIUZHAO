### Week 02 总结
#### 一、知识点总结
#### 1.1 复习
1.Map 	key-value键值对 key不重复
2.set	不重复元素的集合
 **两数之和**
 思路：unordered_map （c++）、hash_map={} （python）
 ```python 
#cpp
for(int i=0;i<nums.size();i++){
            if(dict.find(target-nums[i]) != dict.end()){
                res[0] = dict[target-nums[i]];
                res[1] = i;
                return res;
            }
            dict[nums[i]] = i;
 }
#python
for index,num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num],index]
            hashmap[num] = index 
 ```
 时间复杂度：O(n) 空间复杂度：O(n)

 **三数之和**
 思路：num1 = -(num2+nums3)
 固定一个数，双指针二分查找
**接雨水**
首尾双指针，取左右立柱的较小值，并更新左右边界最大值
计算每个立柱存水量
```python
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        l_max=r_max = 0
        sum_trap = 0
        while left<right:
                if height[left]<height[right]:
                    if height[left] < l_max:
                        sum_trap = sum_trap + l_max - height[left]
                    else :
                        l_max = height[left]
                    left += 1
                else:
                    if height[right] < r_max:
                        sum_trap = sum_trap + r_max - height[right]
                    else:
                        r_max = height[right]
                    right -= 1
        return sum_trap
```
#### 1.2 知识点总结
**二叉树的遍历：
递归/栈：**
```python
class Solution(object):
    def __init__(self):
        self.res = []
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
        	self.res.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.res
        '''
        #root left right
        res,stack=[],[]
        while root or stack:
            if root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            else:
                temp = stack.pop()
                root = temp.right
        return res
        '''

class Solution(object):
    def __init__(self):
        self.res = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.inorderTraversal(root.left)
            self.res.append(root.val)
            self.inorderTraversal(root.right)
        return self.res
        '''
        #left root right
        stack,res =[],[]
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                temp = stack.pop()
                res.append(temp.val)
                root = temp.right
        return res
        '''

class Solution(object):
    def __init__(self):
        self.res = []
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.res.append(root.val)
        return self.res
        '''
        #left right  root 
                stack,res=[],[]
        cur = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else :
                root = stack[-1]
                #若刚刚遍历右子节点，需加入根节点
                if root.right == None or root.right == cur:
                    res.append(root.val)
                    stack.pop()
                    cur = root
                    root = None
                else :
                    root = root.right
        return res
        '''
```

**全排序**
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200726115547163.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTY5NDM2Mw==,size_16,color_FFFFFF,t_70)
[leetcode题解——liweiw](https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/).
深度优先搜索，回溯算法
        

 - 终止条件：如果数字全用完了(usednum == nums.size())，则表示一个可能的结果结束 返回 path
 - 每一次选择路径，判断该数字是否使用过 used
 -  当进行一次遍历后，对使用的数字恢复原来的状态
 - 需要的参数：dfs(nums,res,path,used,usednum)

        
