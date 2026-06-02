class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ''
        for c in s:
            newstr += c.lower() if c.isalnum() else ''
        return newstr == newstr[::-1]