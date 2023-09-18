# 213. House Robber II

[Leetcode Problem](https://leetcode.com/problems/house-robber-ii/description/)

```markdown
You are a professional robber planning to rob houses along a street. Each house 
has a certain amount of money stashed. All houses at this place are arranged in 
a circle. That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, and it will 
automatically contact the police if two adjacent houses were broken into on
the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the 
police.
```

In **[House Robber I,](https://leetcode.com/problems/house-robber/)** houses are in a linear arrangement, not circular. We use bottom-up dynamic programming to find the max amount of money.

```python
def rob(self, nums: List[int]) -> int:
      if len(nums) < 3:
          return max(nums)

      dp = [0] * (len(nums) + 1)
      dp[1], dp[2] = nums[0], nums[1]

      for i in range(3,len(nums) + 1):
          dp[i] = max(dp[i-2] + nums[i-1], dp[i-3] + nums[i-1])
      
      return max(dp)
```

In House Robber II, the last and first house cannot both be robbed, as they are next to each other in a circular arrangement. So, the problem becomes to rob either:

1.  House[1] to House[n-1] 
2. House[2] or House[n]

Which can now be solved using our solution from [House Robber I](https://leetcode.com/problems/house-robber/editorial/)

```python
def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
                return max(nums)

        def helper(nums: List[int]) -> int:
            dp = [0] * (len(nums) + 1)
            dp[1], dp[2] = nums[0], nums[1]

            for i in range(3,len(nums) + 1):
                dp[i] = max(dp[i-2] + nums[i-1], dp[i-3] + nums[i-1])
            
            return max(dp)

        return max(helper(nums[:-1]), helper(nums[1:]))
```