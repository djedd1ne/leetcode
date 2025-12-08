class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        i = 1
        while (i <= n):
            if (i % 3 == 0 and i % 5 == 0):
                answer.append("FizzBuzz")
            elif not(i % 3):
                answer.append("Fizz")
            elif not(i % 5):
                answer.append("Buzz")
            else:
                answer.append(str(i))
            i += 1

        return (answer)
    
#test
#a = Solution()
#print(a.fizzBuzz(5))

