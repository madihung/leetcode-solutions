## 1249. Minimum Remove to Make Valid Parentheses

[Leetcode Problem](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/)

```markdown
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in 
any positions ) so that the resulting parentheses string is valid and return 
any valid string.

Formally, a parentheses string is valid if and only if:
- It is the empty string, contains only lowercase characters, or
- It can be written as AB (A concatenated with B), where A and B are valid 
strings
- It can be written as (A), where A is a valid string.
```

<aside>
☝ Tip: Evaluating validity of a string ⇒ consider using a stack

</aside>

---

**Stack Implementation**

- We iterate through s, counting the ( parentheses, `openCount`
    - add each character from s onto a result stack
    - If a ) parenthesis is encountered
        - If `openCount > 0`, decrement the `openCount` as we have found a complete `()` pair
        - If openCount == 0, do not include ) parenthesis in result as it’s an incomplete pair
- We perform the same process on the result stack, this time tracking ), `closeCount`
    - utilize the stack’s ability to pop(), in order to iterate through the stack backwards
- Since the string was read backwards, the result has to be reversed to get the solution

```python
def minRemoveToMakeValid(self, s: str) -> str:
		if len(s) == 0:
		            return ""
		
	  res = []
	  openCount, closeCount = 0, 0
	  for char in s:
	      res.append(char)
	      if char == ")":
	          if openCount == 0:
	              res.pop()
	          else:
	              openCount -= 1
	      if char == "(":
	          openCount += 1
	  print(res)
	  if openCount == 0:
	      return "".join(res)
	
	  res2 = []
	  while res:
	      res2.append(res.pop())
	      if len(res2) > 0 and res2[-1] == "(":
	          if closeCount == 0:
	              res2.pop()
	          else:
	              closeCount -= 1
	      elif res2[-1] == ")":
	          closeCount += 1          
	
	  return "".join(reversed(res2)
```

**Simplify with a helper**

- tracking openCount and closeCount use very similar code, so the solution code can be abstracted into a helper

```python
def minRemoveToMakeValid(self, s: str) -> str:

        def balance(countParen: str, removeParen: str, stringInput: List[str]):
            count = 0
            sMod = []
            for char in stringInput:
                sMod.append(char)
                if char == countParen:
                    count += 1
                elif char == removeParen:
                    if count > 0:
                        count -= 1
                    else:
                        sMod.pop()
           
            return sMod

        sMod1 = balance("(", ")", s)
        sMod2 = balance(")", "(", reversed(sMod1))
        res = reversed(sMod2)
        
        return "".join(res)
```