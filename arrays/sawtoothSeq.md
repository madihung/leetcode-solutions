```markdown
## Sawtooth Sequence

A sawtooth sequence is a sequence of numbers that alternate between increasing 
and decreasing. In other words, each element is either strictly greater than 
its neighbouring elements or strictly less than its neighbouring elements.

Given an array of integers arr, your task is to count the number of contiguous 
subarrays that represent a sawtooth sequence of at least two elements.
```

**Example**

- For **arr = [9, 8, 7, 6, 5]**, the output should be **solution(arr) = 4**.
    
    Since all the elements are arranged in decreasing order, it won't be possible to form any sawtooth subarrays of length **3** or more. There are **4** possible subarrays containing two elements, so the answer is **4**.
    
- For **arr = [10, 10, 10]**, the output should be **solution(arr) = 0**.
    
    Since all of the elements are equal, none of subarrays can be sawtooth, so the answer is **0**.
    
- For **arr = [1, 2, 1, 2, 1]**, the output should be **solution(arr) = 10**.
    
    All contiguous subarrays containing at least two elements satisfy the condition of problem. There are **10** possible contiguous subarrays containing at least two elements, so the answer is **10**.
    

**Input/Output**

- 2 ≤ arr.length ≤ 105
- 109 ≤ arr[i] ≤ 109

**Solution**

- each time the array flips, the number of contiguous arrays goes up by the current streak of flips

![sawtoothSeq.jpeg](/images/sawtoothSeq.jpeg)

```python
def solution(arr):
	if len(arr) < 2:
		return 0
	
	streak = 0
	prevInc = None
	res = 0

	for i in length range(1, len(arr)):
		# if not increasing or decreasing, reset 
		if arr[i] == arr[i-1]:
			prevInc = None
			streak = 0
		else:
			if arr[i] > arr[i-1]:
				currInc = True
				# check the direction has flipped
				if prevInc != currInc:
					streak += 1
					prevInc = currInc
				else:
					streak = 1
				
				res += streak

	return res
```

Time - O(n)

Space - O(1)