1# The guess API is already defined for you.
2# @param num, your guess
3# @return -1 if num is higher than the picked number
4#          1 if num is lower than the picked number
5#          otherwise return 0
6# def guess(num: int) -> int:
7
8class Solution:
9    def guessNumber(self, n: int) -> int:
10        def binaryGuess(left: int, right: int) -> int:
11            my_guess = (left + right) // 2
12            check = guess(my_guess)
13            if check == -1:
14                return binaryGuess(left, my_guess - 1)
15            elif check == 0:
16                return my_guess
17            else:
18                return binaryGuess(my_guess + 1, right)
19        
20        return binaryGuess(1, n)