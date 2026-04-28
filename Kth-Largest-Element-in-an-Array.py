1import random
2
3class Solution:
4    def findKthLargest(self, nums: List[int], k: int) -> int:
5        target = k - 1
6        l = len(nums)
7
8        def quickSort(start, end):
9            pivot_index = random.randint(start, end)
10            pivot = nums[pivot_index]
11            i = start
12            gt = start
13            lt = end
14
15            while i<=lt:
16                if nums[i] > pivot:
17                    nums[i], nums[gt] = nums[gt], nums[i]
18                    i += 1
19                    gt += 1
20                
21                elif nums[i] == pivot:
22                    i += 1
23
24                else:
25                    nums[i], nums[lt] = nums[lt], nums[i]
26                    lt -= 1
27
28            if gt <= target and target <= lt:
29                return pivot
30            
31            elif target < gt:
32                return quickSort(start, gt - 1)
33            else:
34                return quickSort(lt + 1, end)
35            
36        return quickSort(0, l - 1)