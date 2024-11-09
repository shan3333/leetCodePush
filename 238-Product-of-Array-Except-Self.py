class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre_product = 1
        post_product = 1
        output = [1]*l

        for i in range(l):
            output[i] *= pre_product
            pre_product *= nums[i]
        
        for i in range(l-1, -1, -1):
            output[i] *= post_product
            post_product *= nums[i]
        return output 