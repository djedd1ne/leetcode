class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i].isalnum() == 0:
                i += 1
            elif s[j].isalnum() == 0:
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True
    
# Test
#a = Solution()
#print(a.isPalindrome("A man, a plan, a canal: Panama"))
#print(a.isPalindrome(" "))
#print(a.isPalindrome("race a car"))