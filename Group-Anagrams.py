class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = []
        r = []
        for i in strs:
            sortedI = sorted(i)
            if sortedI in l:
                r[l.index(sortedI)].append(i)
            else:
                r.append([i])
                l.append(sortedI)
        return r