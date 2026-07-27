class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        nums.sort()
        res = 0
        i = 0
        curr, streak = nums[0], 0
        while i < n:
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < n and curr == nums[i]:
                i += 1
            streak += 1
            curr += 1
            res = max(res, streak)
        return res