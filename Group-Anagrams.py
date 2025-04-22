class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r = defaultdict(list)
        for i in strs:
            key = "".join(sorted(i))
            r[key].append(i)
        return list(r.values())