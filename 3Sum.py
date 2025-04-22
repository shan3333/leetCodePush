class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = []
        sortedNums = sorted(nums)
        for i in range(len(sortedNums)):
            j = i+1
            k = len(nums) - 1
            # skip to next number when the number is same as previous
            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue
            # return empty if number i is greater than 0
            if sortedNums[i] > 0:
                break
            while j<k:
                total = sortedNums[j] + sortedNums[k] + sortedNums[i]
                # increase index j if the sum of 3 numbers is smaller than 0
                if total < 0:
                    j += 1
                # decrease index k if the sum of 3 numbers is greater than 0
                elif total > 0:
                    k -= 1
                else:
                    r.append([sortedNums[i], sortedNums[j], sortedNums[k]])
                    while j<k and sortedNums[j] == sortedNums[j+1]:
                        j += 1
                    while j<k and sortedNums[k] == sortedNums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        return r