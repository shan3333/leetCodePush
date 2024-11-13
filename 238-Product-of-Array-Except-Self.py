class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre_production = 1
        post_production = 1

        for i in range(l):
            