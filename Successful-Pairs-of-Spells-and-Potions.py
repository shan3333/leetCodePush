1class Solution:
2    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
3        pairs = []
4        potions.sort()
5        m = len(potions)
6
7        # Return the index of potions that are at least success
8        def findSuccess(spell: int) -> int:
9            left, right = 0, m - 1
10            while left <= right:
11                mid = (left + right) // 2
12                product = spell * potions[mid]
13                if product >= success:
14                    right = mid - 1
15                else:
16                    left = mid + 1
17            return left
18
19        for v in spells:
20            res = findSuccess(v)
21            pairs.append(m - res)
22        return pairs