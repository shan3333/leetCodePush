1# The guess API is already defined for you.
2# @param num, your guess
3# @return -1 if num is higher than the picked number
4#          1 if num is lower than the picked number
5#          otherwise return 0
6# def guess(num: int) -> int:
7
8class Solution:
9    def guessNumber(self, n: int) -> int:
10        left, right = 1, n
11        while left <= right:
12            my_guess = (left + right) // 2
13            check = guess(my_guess)
14
15            if check == -1:
16                right = my_guess - 1
17            elif check == 1:
18                left = my_guess + 1
19            else:
20                return my_guess