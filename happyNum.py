class Solution:
    def happyNum(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 4:
            return False
        if n == 0:
            return False

        res = 0
        for i in str(n):
            res += int(i) ** 2

        print("current value of n:", n)

        n = res
        return self.happyNum(n)


solution = Solution()
result = solution.happyNum(9999999)
print("Result:", result)
