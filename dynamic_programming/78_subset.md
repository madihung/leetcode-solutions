# 78. Subsets

[Link to leetcode problem](https://leetcode.com/problems/subsets/)

```markdown
Given an integer array **nums**, return all possible subsets *(the power set)* 
The solution must not contain duplicate subsets
```

- For each element in the **nums** array there are two choices: 1) add the element  2) don’t add the element
- Number of possible subsets = 2^n
- Time complexity = O(n * 2^n)
- backtracking = brute force method but is still efficient for this problem

**Decision Tree**

![subsets.jpeg](/images/subsets.jpeg)

```python
def subsets(self, nums: List[int]) -> List[List[int]]:

    def dfs(i):
        # i = levels in the decision tree
        # ex) consider adding 1, 2, 3 -> three levels, recursion 3x
        if i >= len(nums):
            result.append(subset[:])
            return

        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)
        # decision to not include nums[i]
        subset.pop()
        dfs(i + 1)

    result = []
    subset = []
    dfs(0)
    
    return result
```