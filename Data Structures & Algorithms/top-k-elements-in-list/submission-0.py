class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dicio = {}
        for num in nums:
            dicio[num] = dicio.get(num,0) + 1

        my_arr = []
        for key, val in dicio.items():
            my_arr.append([val, key])
        my_arr.sort()

        res = []
        while len(res) < k:
            res.append(my_arr.pop()[1]) 
        return res