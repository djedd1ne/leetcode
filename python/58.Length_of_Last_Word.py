class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = 1; j = 0
        if (len(s) == 0):
            return 0
        while (i <= len(s)) and s[len(s) - i] == ' ':
            i +=1
        while ((len(s) - i) - j >= 0) and (s[(len(s) - i) - j] != ' '):
            j +=1
        return j
    
#a = Solution()
#print(a.lengthOfLastWord("    h     "))