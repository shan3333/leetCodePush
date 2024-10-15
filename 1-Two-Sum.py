class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = dict()
        l = len(nums)
        for i in range(l):
            complement = target - nums[i]
            if complement in hm:
                return [hm[complement], i]
            hm[nums[i]] = i
        
        return []