class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for k,v in enumerate(nums):
            if target-v in d:
                return [k,d[target-v]]
            d[v] = k
        