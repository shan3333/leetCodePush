1class TrieNode:
2    def __init__(self):
3        self.childNodes = [None] * 26
4        self.isEnd = False
5        self.word = None
6
7class Trie:
8    def __init__(self):
9        self.root = TrieNode()
10
11    def insert(self, word):
12        curr = self.root
13        for i in word:
14            index = ord(i) - ord('a')
15            if not curr.childNodes[index]:
16                curr.childNodes[index] = TrieNode()
17            curr = curr.childNodes[index]
18        curr.word = word
19        curr.isEnd = True
20
21    def startWith(self, searchWord): 
22        curr = self.root
23        for i in searchWord:
24            index = ord(i) - ord('a')
25            if not curr.childNodes[index]:
26                return None
27            curr = curr.childNodes[index]
28        return curr
29            
30
31class Solution:
32    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
33        ans = []
34        trie = Trie()
35        for p in products:
36            trie.insert(p)
37        
38        def dfs(node, suggestions):
39            if len(suggestions) == 3:
40                return
41            if node.isEnd:
42                suggestions.append(node.word)
43            
44            for child in node.childNodes:
45                if child:
46                    dfs(child, suggestions)
47                if len(suggestions) == 3:
48                    return
49        
50        for i, v in enumerate(searchWord):
51            s = searchWord[:i+1]
52            n = trie.startWith(s)
53
54            suggestions = []
55            if n:
56                dfs(n, suggestions)
57            ans.append(suggestions)
58        
59        return ans