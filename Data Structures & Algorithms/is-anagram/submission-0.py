class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ch_dict = {}

        for i in s:
            ch_dict[i] = ch_dict.get(i,0) + 1
        for i in t:
            ch_dict[i] = ch_dict.get(i,0) - 1
        
        for v in ch_dict.values():
            if v != 0:
                return False 

        return True