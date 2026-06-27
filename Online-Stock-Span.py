1class StockSpanner:
2
3    def __init__(self):
4        self.stack = []
5        self.curr_index = 0
6
7    def next(self, price: int) -> int:
8        prev_index = 0
9        self.curr_index += 1
10        while self.stack:
11            top = self.stack[-1]
12            if top[1] <= price:
13                pop = self.stack.pop()
14                continue
15            else:
16                prev_index = top[0]
17                break
18
19        self.stack.append((self.curr_index, price))
20        return self.curr_index - prev_index
21        
22
23
24# Your StockSpanner object will be instantiated and called as such:
25# obj = StockSpanner()
26# param_1 = obj.next(price)