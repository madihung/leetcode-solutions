# 70. Climbing Stairs

```markdown
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. 

In how many distinct ways can you climb to the top?
```

**Decision Tree**

- Two options: one or two steps
- Notice the two circle subtrees are the exact same → overlapping subproblems
- This problem could be solved using backtracking (dfs), but DP will optimize the algo by saving the solution to repeated subproblems so they do not have to be recalculated

![climbingStairs.jpeg](/images/climbingStairs.jpeg)
---

**Backtracking Approach**

```python

def climbStairs(self, n: int) -> int:

      self.res = 0
      def backtrack(steps: int):
          if steps == n:
              self.res += 1
              return
          elif steps > n:
              return
          else: 
              # take one step
              backtrack(steps + 1)
              # take two steps
              backtrack(steps + 2)
      
      backtrack(0)
      return self.res
```

Time Complexity = O(2^n) = size of recursion tree

Space Complexity = O(n) = size of recursive stack

**DP Bottom up Approach**

- using a bottom-up approach
- two base cases: 1) at step 5 ; 2) at step 4
    - both require a single step to get the n = 5, which is why index 4 and 5 of the array are 1
    - every index (i) prior to 4 and 5 are the sum of arr[i+1] and arr[i+2]
- Consider i = 3, which has two cases
    1. take one step: you would land on index 4, which means theres only 1 way to proceed to reach n = 5
    2. take two steps: you would land on index 5, which means theres only 1 way to proceed to reach n = 5
    
    → From i = 3 there are a total of two ways to get to n = 5 from index 3
    

![IMG_3D760CC23C7C-1.jpeg](https://prod-files-secure.s3.us-west-2.amazonaws.com/65366120-3a32-4c75-8482-9146a8fc036b/ba3e3d31-34bc-44bf-b2b0-75eb32fcb1fa/IMG_3D760CC23C7C-1.jpeg)

```python
def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        dp = [0] * (n+1) 
        dp[n] = 1
        dp[n-1] = 1

        for i in reversed(range(0,n-1)):
            dp[i] = dp[i+1] + dp[i + 2]
        return dp[0]
```

**DP Top down Approach**

```python
def climbStairs(self, n: int) -> int:
        
      if n < 2:
          return n

      dp = [-1] * (n+1)
      dp[0] = dp[1] = 1

      for i in range(2,(n+1)):
          dp[i] = dp[i-1] + dp[i-2]

      return dp[n]
```