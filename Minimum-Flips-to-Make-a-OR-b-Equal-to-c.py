1class Solution:
2    def minFlips(self, a: int, b: int, c: int) -> int:
3        flips = 0
4        while a or b or c:
5            bi_a, bi_b, bi_c = a & 1, b & 1, c & 1
6            if bi_c == 0:
7                if bi_a != 0: flips += 1
8                if bi_b != 0: flips += 1
9            else:
10                if bi_a == 0 and bi_b == 0:
11                    flips += 1
12            a >>= 1
13            b >>= 1
14            c >>= 1
15        return flips