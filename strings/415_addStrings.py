## 415. Add Strings
# https://leetcode.com/problems/add-strings/description/

## Problem
# Given two non-negative integers, num1 and num2 represented as string, return 
# the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling 
# large integers (such as BigInteger). You must also not convert the inputs to 
# integers directly.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []

        carry = 0
        p1, p2 = len(num1) - 1, len(num2) - 1

        while p1 >= 0 or p2 >= 0:
            d1 = 0 if p1 < 0 else ord(num1[p1]) - ord('0')
            d2 = 0 if p2 < 0 else ord(num2[p2]) - ord('0')

            total = (d1 + d2 + carry) % 10
            carry = (d1 + d2 + carry) // 10
            res.append(str(total))

            p1 -= 1
            p2 -= 1

        if carry > 0:
            res.append(str(carry))

        return  "".join(reversed(res))