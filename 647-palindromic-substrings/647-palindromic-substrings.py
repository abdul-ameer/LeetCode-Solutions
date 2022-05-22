class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindrome(s):
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j] : return False
                i += 1
                j -= 1
            return True
        
        arr = []
        for i in range(len(s)):
            for j in range(0,i+1):
                arr.append(s[j:i+1])
        
        count = 0
        for i in arr:
            if isPalindrome(i) == True:count += 1
        
        return count
        