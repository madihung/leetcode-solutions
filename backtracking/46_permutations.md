# 46. Permutations
```markdown
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.
```

**Decision Tree**

- at each level theres ~ n choices for each element in **nums** to add next → iterate through in **nums** the backtracking function

![permutations.jpeg](/images/permutations.jpeg)

```python
def permute(self, nums: List[int]) -> List[List[int]]:
				res = []
        def dfs(subset):
            if len(subset) == len(nums):
                res.append(subset[:])
                return
            
            for n in nums:
                if n not in subset:
                    subset.append(n)
                    dfs(subset)
                    subset.pop()

        dfs([])
        return res
```