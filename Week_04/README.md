DP步骤： 


* 找到重复性（分治） 
* 定义状态数组（前缀型，后缀型，坐标型，序列型，划分型，区间型） 
* DP方程 

解决的问题 


1. 求方案总数 
2. 求最大最小值 
3. 求可行性（存在性）问题 

类型： 

区间型、双序列、划分型、坐标型、序列型、背包型、状态压缩型 

**动态规划4步解题法** 


* 确定状态 
    * 研究最优策略的最后一步 
    * 转化为子问题 
* 转移方程 
    * 根据子问题定义直接得到 
* 初始条件和边界情况 
    * 细心，考虑周全 
* 计算顺序 
    * 利用之前的计算结果 

![图片](https://uploader.shimo.im/f/lo4ryxWZ2Yg8r88t.png!thumbnail)

# 1332 乘积为B 

```python
def getMinCost(self, B, A): 
        # A的长度 
        n = len(A) 
        # 存B的因数的数组 
        factor = [] 
        # 找出B的因子 并存入factor 
        for i in range(1, B + 1): 
            if (B % i == 0): 
                factor.append(i) 
        # B因子的数量 
        m = len(factor) 
        # 初始化dp数组 
        dp = [sys.maxsize for i in range(m)] 
        # dp数组边界条件 
        dp[0] = 0 
        for i in range(n): 
            # 初始化本次循环中被更新的dp数组 
            tmp = [sys.maxsize for i in range(m)] 
            for j in range(m): 
                # dp[j]为无穷，无法去更新 
                if (dp[j] != sys.maxsize): 
                    # 枚举factor[j]的倍数，将前i个数的乘积由factor[j]变换成factor[k] 
                    for k in range(j, m): 
                        if (factor[k] % factor[j] == 0): 
                            tmp[k] = min(tmp[k], dp[j] + abs(factor[k] // factor[j] - A[i])) 
            # 交换dp数组 和tmp数组，dp滚动数组优化空间 
            # 一直用dp数组去更新下一次的tmp数组 
            dp=tmp 
        return (int)(dp[m - 1]) 
```
