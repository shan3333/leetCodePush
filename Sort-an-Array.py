class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            res = []
            l = len(nums)
            if l <= 1:
                return nums

            mid = l//2
            left_list = merge_sort(nums[:mid])
            right_list = merge_sort(nums[mid:])

            left_pointer, right_pointer = 0, 0
            while left_pointer < len(left_list) and right_pointer < len(right_list):
                if left_list[left_pointer] < right_list[right_pointer]:
                    res.append(left_list[left_pointer])
                    left_pointer += 1
                
                else:
                    res.append(right_list[right_pointer])
                    right_pointer += 1
            
            res.extend(left_list[left_pointer:])
            res.extend(right_list[right_pointer:])
            
            return res
        
        return merge_sort(nums)