class Solution:
    def addBinary(self, a:str, b:str) -> str:
        tmp = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        result = ""

        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            tmp.append(str(total % 2))
            if (total == 2 or total == 3):
                carry = 1
            else:
                carry = 0
        for digit in tmp[::-1]:
            result += digit
        return result
    

# Test
#a = Solution()
#print (a.addBinary("11111","1"))