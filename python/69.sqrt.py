class Solution:
    def mySqrt(seld, x:int) -> int:
        sqrt = 1
        while (sqrt * sqrt <= x):
            sqrt += 1
        return sqrt - 1

# Test
#a = Solution()
#print(a.mySqrt(8))
        