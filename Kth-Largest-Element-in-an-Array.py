1import heapq
2
3class Solution:
4    def findKthLargest(self, nums: List[int], k: int) -> int:
5        return heapq.nlargest(k, nums)[k-1]
6        