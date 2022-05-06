""" 
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
 

Constraints:

1 <= s.length <= 105
2 <= k <= 104
s only contains lower case English letters.
"""

Initial Attempt - Brute Force - Time Limit Exceeded:

class Solution:
    def removeDuplicates(self, s):
        for i,(a,b) in enumerate(pairwise(s)):
            if a == b: return self.removeDuplicates(s[:i] + s[i+2:])
        return s
Solution - Stack:

class Solution:
    def removeDuplicates(self, s):
        stack = []
        for c in s:
            if stack and c == stack[-1]: stack.pop()
            else: stack.append(c)
        return "".join(stack)
Solution - Two Pointer:

class Solution:
    def removeDuplicates(self, s):
        lst, n = list(s), len(s)
        l, r = 0, 1
        while r < n:
            if l >= 0 and lst[l] == lst[r]:
                l -= 1
                r += 1
            else:
                l += 1
                lst[l] = lst[r]
                r += 1
        return "".join(lst[:l+1])

