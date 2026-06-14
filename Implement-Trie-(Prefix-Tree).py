1class TrieNode:
2    def __init__(self):
3        self.children = [None] * 26
4        self.isLeaf = False
5
6class Trie:
7    def __init__(self):
8        self.root = TrieNode()
9
10    def insert(self, word: str) -> None:
11        curr = self.root
12        for i in word:
13            index = ord(i) - ord('a')
14            if curr.children[index] is None:
15                curr.children[index] = TrieNode()
16            curr = curr.children[index]
17        curr.isLeaf = True
18
19    def search(self, word: str) -> bool:
20        curr = self.root
21        for i in word:
22            index = ord(i) - ord('a')
23            if curr.children[index] is None:
24                return False
25            curr = curr.children[index]
26        return curr.isLeaf
27
28    def startsWith(self, prefix: str) -> bool:
29        curr = self.root
30        for i in prefix:
31            index = ord(i) - ord('a')
32            if curr.children[index] is None:
33                return False
34            curr = curr.children[index]
35        return True
36        
37
38
39# Your Trie object will be instantiated and called as such:
40# obj = Trie()
41# obj.insert(word)
42# param_2 = obj.search(word)
43# param_3 = obj.startsWith(prefix)