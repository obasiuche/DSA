class Solution:
    def fib(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        if (n < 2) : return n

        a, b = 0, 1

        for i in range(1, n):
            a, b = b, a + b
        return b


n = input("Enter a Number to find it's Fibo: ")
solution = Solution()
result = solution.fib(int(n))
print(result)
