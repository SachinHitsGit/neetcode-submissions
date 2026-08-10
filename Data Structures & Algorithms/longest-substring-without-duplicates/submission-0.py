class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        r,l = 0,0
        max_count = 0
        n = len(s)
        sub = set()
        while r < n:
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            max_count = max(max_count,r-l+1)
            r += 1
        return max_count