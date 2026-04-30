1import heapq
2
3class SmallestInfiniteSet:
4
5    def __init__(self):
6        self.current = 1
7        self.heap = []
8        self.set = set()
9
10    def popSmallest(self) -> int:
11        if self.heap:
12            s = heapq.heappop(self.heap)
13            self.set.remove(s)
14            return s
15
16        s = self.current
17        self.current += 1
18        return s
19
20    def addBack(self, num: int) -> None:
21        if num < self.current and num not in self.set:
22            heapq.heappush(self.heap, num)
23            self.set.add(num)
24
25
26# Your SmallestInfiniteSet object will be instantiated and called as such:
27# obj = SmallestInfiniteSet()
28# param_1 = obj.popSmallest()
29# obj.addBack(num)