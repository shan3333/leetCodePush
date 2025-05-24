class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = {}
        for k, v in enumerate(nums):
            if target-v in l.keys():
                return [k, l[target-v]]
            else:
                l[v] = k