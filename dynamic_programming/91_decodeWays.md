# 91. Decode Ways

A message containing letters from `A-Z` can be **encoded** into numbers using the following mapping:

```
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
```

To **decode** an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, `"11106"` can be mapped into:

- `"AAJF"` with the grouping `(1 1 10 6)`
- `"KJF"` with the grouping `(11 10 6)`

Note that the grouping `(1 11 06)` is invalid because `"06"` cannot be mapped into `'F'` since `"6"` is different from `"06"`.

Given a string `s` containing only digits, return *the **number** of ways to **decode** it*.

**DP Problem**

<aside>
☝ A DP solution can be used as we are building our solution off the soln to previous subproblems

Ex) to solve `s = “226”`, we first solve `s = “2”` then `s = “22”`

</aside>

The DP array should hold the number of ways the previous string could be decoded 

- `dp[i]` will hold the number of ways `s[0:(i-1)]` could be decoded
- Note: the i-th digit in s is `s[i-1]` which is why `dp[i]` holds the solution for `s[0:(i-1)]`

```python
def numDecodings(self, s: str) -> int:
        
        dp = [0] * (len(s) + 1)

				# Base Cases
        dp[0] = 1
        dp [1] = 1 if s[0] != "0" else 0
        
        for i in range(2, len(dp)):
						# if s[i-1] == 0, it cannot stand alone 
						# so decode combinations in s[0:(i-2)] won't be possible 
            if s[i-1] != "0":
                dp[i] = dp[i-1]
						
						# If s[i-2]s[i-1] digit does not correspond to a valid letter
						# the decode combinations for s[0:(i-3)] are not possible
            twoDigit = s[i-2] + s[i-1]
            if int(twoDigit) < 27 and int(twoDigit) > 9:
                dp[i] += dp[i-2]

        return dp[len(s)]
```