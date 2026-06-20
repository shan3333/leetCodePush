1class TrieNode:
2    def __init__(self):
3        self.childNodes = [None] * 26
4        self.suggestions = []
5
6class Trie:
7    def __init__(self):
8        self.root = TrieNode()
9
10    def insert(self, word):
11        curr = self.root
12        for i in word:
13            index = ord(i) - ord('a')
14
15            if not curr.childNodes[index]:
16                curr.childNodes[index] = TrieNode()
17            curr = curr.childNodes[index]
18
19            if len(curr.suggestions) < 3:
20                curr.suggestions.append(word)
21        
22    def startWith(self, searchWord):
23        curr = self.root
24        for i in searchWord:
25            index = ord(i) - ord('a')
26
27            if not curr.childNodes[index]:
28                return None
29            curr = curr.childNodes[index]
30        return curr
31
32class Solution:
33    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
34        ans = []
35        trie = Trie()
36        products.sort()
37        for p in products:
38            trie.insert(p)
39        
40        for i, v in enumerate(searchWord):
41            s = searchWord[:i+1]
42            n = trie.startWith(s)
43            if n:
44                ans.append(n.suggestions)
45            else:
46                ans.append([])
47        return ans