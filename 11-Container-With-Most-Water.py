class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        s = 0
        r_height = 0
        l_height = 0

        while right > left:
            if r_height > height[right]:
                right -= 1
                continue
            elif l_height > height[left]:
                left += 1
                continue
            r_height = height[right]
            l_height = height[left]
            cal = min(r_height, l_height) * (right - left)
            s = max(s, cal)
            if r_height >= l_height and left + 1 < len(height):
                left += 1
            elif r_height < l_height and right - 1 >= 0:
                right -= 1
        return s
                

                