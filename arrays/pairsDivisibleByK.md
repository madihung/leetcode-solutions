# **Count pairs in array whose sum is divisible by K**

```markdown
You are given an array of integers a and an integer k. Your task is to 
calculate the number of ways to pick two different indices i < j, such that 
a[i] + a[j] is divisible by k.
```

**Example**

- For **a = [1, 2, 3, 4, 5]** and **k = 3**, the output should be **solution(a, k) = 4**.
    
    There are **4** pairs of numbers that sum to a multiple of **k = 3**:
    
    - a[0] + a[1] = 1 + 2 = 3
    - a[0] + a[4] = 1 + 5 = 6
    - a[1] + a[3] = 2 + 4 = 6
    - a[3] + a[4] = 4 + 5 = 9

**Constraints**

- 1 ≤ a.length ≤ 105
- 1 ≤ a[i] ≤ 109
- 1 ≤ k ≤ 109

---

**********************************Brute Force Approach**********************************

```python
def solution(a, k):
    if len(a) == 1:
        return 0

    res = 0
    for i in range(len(a)):
				for aj in a[i + 1:]:
            if (a[i] + aj) % k == 0:
								res += 1
    return res
```

- Time Complexity = O(n^2) → nested for loop
- Space = O(1)

---

**********Hashing Technique**********

- `x % k = a number in range[0, k-1]`
- create an array or hashmap with k entries, to track the occurrences of remainders

```python
def solution(a, k):
	if len(a) == 1:
		return 0

	modArr = [0[ * k
	res = 0
	
	for num in a:
		# add occurence to array
		modArr[num % k] += 1
		
		# find which numbers when added to num would sum to a multiple of k
		# any number in array a that has a reaminder of (k - (num % k) % k works
		modOfPair = (k - (num % k)) % k
		res += modArr[modPair]
```

- Time = O(n)
- Space = O(k) for the array holding remainder occurences