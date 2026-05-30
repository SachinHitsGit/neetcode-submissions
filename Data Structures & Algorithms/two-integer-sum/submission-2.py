class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicio = {}

        for i, n in enumerate(nums):
            dif = target - n

            if dif in dicio:
                return [dicio[dif], i]
            
            dicio[n] = i








        # for i in nums:
        #     if target-i in nums:
        #         return [nums.index(i), nums.index(target-i)]
